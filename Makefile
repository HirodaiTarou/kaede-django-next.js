.PHONY: help setup dev dev-backend dev-frontend dev-docker install install-backend install-frontend build test test-docker test-backend test-frontend test-contacts test-users test-lectures test-reviews lint format clean docker-up docker-down docker-build docker-logs migrate makemigrations generate-schema schema

# =============================================================================
# メイン実行コマンド
# =============================================================================

# プロジェクトの初期セットアップ
setup: docker-build docker-up
	@echo "⏳ Waiting for services to be ready..."
	@sleep 20
	@echo ""
	@echo "🎉 Setup completed successfully!"
	@echo "📊 Backend API: http://localhost:8000"
	@echo "🌐 Frontend App: http://localhost:3000"
	@echo "🗄️  Database: http://localhost:5432"
	@echo ""
	@echo "✅ Services are ready! Open http://localhost:3000 in your browser"

# 開発環境の起動（ローカル環境で両方を並列実行）
dev: docker-up
	@echo ""
	@echo "🚀 Starting development servers..."
	@echo "📊 Backend API: http://localhost:8000"
	@echo "🌐 Frontend App: http://localhost:3000"
	@echo ""
	@echo "📝 Useful commands:"
	@echo "  Ctrl+C to stop both servers"
	@echo "  make dev-backend    - Start Django only"
	@echo "  make dev-frontend   - Start Next.js only"
	@echo ""
	@echo "⏳ Starting servers in parallel..."

stop: docker-stop
	@echo "✅ All Docker containers stopped"

# ヘルプの表示
help:
	@echo "Available commands:"
	@echo "  setup           - Initial project setup (install deps, build, migrate)"
	@echo "  dev             - Start development servers (requires setup first)"
	@echo "  dev-backend     - Start Django development server locally"
	@echo "  dev-frontend    - Start Next.js development server locally"
	@echo ""
	@echo "  install         - Install dependencies for both backend and frontend"
	@echo "  install-backend - Install Python dependencies"
	@echo "  install-frontend- Install Node.js dependencies"
	@echo "  build           - Build the frontend application"
	@echo ""
	@echo "  test            - Run tests for both backend and frontend (local)"
	@echo "  test-docker     - Run tests for both backend and frontend (Docker)"
	@echo "  test-backend    - Run backend tests (Docker)"
	@echo "  test-frontend   - Run frontend tests (Docker)"
	@echo "  test-contacts   - Run contacts app tests (Docker)"
	@echo "  test-users      - Run users app tests (Docker)"
	@echo "  test-lectures   - Run lectures app tests (Docker)"
	@echo "  test-reviews    - Run reviews app tests (Docker)"
	@echo ""
	@echo "  lint            - Run linters for both backend and frontend"
	@echo "  format          - Format code for both backend and frontend"
	@echo "  clean           - Clean build artifacts and cache"
	@echo "  docker-up       - Start Docker services"
	@echo "  docker-down     - Stop Docker services"
	@echo "  docker-build    - Build Docker images"
	@echo "  docker-logs     - Show Docker logs"
	@echo "  migrate         - Run database migrations"
	@echo "  makemigrations  - Create database migrations"
	@echo "  generate-schema - Generate OpenAPI schema file"
	@echo "  schema          - Alias for generate-schema"

# =============================================================================
# 依存関係のインストール
# =============================================================================

install: install-backend install-frontend

install-backend:
	cd backend && pip install -r requirements.txt

install-frontend:
	cd frontend && npm install

# =============================================================================
# Docker環境の管理
# =============================================================================

docker-up:
	@echo "🐳 Starting Docker services..."
	docker compose up -d
	@echo "✅ Docker services started"

docker-down:
	@echo "🛑 Stopping Docker services..."
	docker compose down
	@echo "✅ Docker services stopped"

docker-build:
	@echo "🔨 Building Docker images..."
	docker compose build
	@echo "✅ Docker images built"

docker-logs:
	@echo "📋 Showing Docker logs..."
	docker compose logs -f

docker-stop:
	@echo "🛑 Stopping all Docker containers..."
	docker compose stop
	@echo "✅ All Docker containers stopped"

# =============================================================================
# データベース管理
# =============================================================================

migrate:
	@echo "🔄 Running database migrations..."
	docker compose exec backend python manage.py migrate
	@echo "✅ Database migrations completed"

makemigrations:
	@echo "📝 Creating database migrations..."
	docker compose exec backend python manage.py makemigrations
	@echo "✅ Migrations created"

# =============================================================================
# API仕様書生成
# =============================================================================

generate-schema:
	@echo "📋 Generating OpenAPI schema..."
	docker compose exec backend python manage.py spectacular --file openapi-schema.yml
	@echo "✅ OpenAPI schema generated"

schema: generate-schema

# =============================================================================
# ビルドとテスト
# =============================================================================

build:
	cd frontend && npm run build

# ローカル環境でのテスト（従来通り）
test:
	cd backend && python manage.py test
	cd frontend && npm test

# Docker環境でのテスト
test-docker: test-backend test-frontend
	@echo "✅ All tests completed"

# バックエンドテスト
test-backend:
	@echo "🧪 Running backend tests in Docker..."
	docker compose exec backend python manage.py test
	@echo "✅ Backend tests completed"

# フロントエンドテスト
test-frontend:
	@echo "🧪 Running frontend tests in Docker..."
	docker compose exec frontend npm test
	@echo "✅ Frontend tests completed"

# アプリケーション別テスト
test-contacts:
	@echo "🧪 Running contacts app tests in Docker..."
	docker compose exec backend python manage.py test contacts
	@echo "✅ Contacts tests completed"

test-users:
	@echo "🧪 Running users app tests in Docker..."
	docker compose exec backend python manage.py test users
	@echo "✅ Users tests completed"

test-lectures:
	@echo "🧪 Running lectures app tests in Docker..."
	docker compose exec backend python manage.py test lectures
	@echo "✅ Lectures tests completed"

test-reviews:
	@echo "🧪 Running reviews app tests in Docker..."
	docker compose exec backend python manage.py test reviews
	@echo "✅ Reviews tests completed"

# =============================================================================
# コード品質管理
# =============================================================================

lint:
	cd backend && flake8 .
	cd frontend && npm run lint

format:
	cd backend && black . && isort .
	cd frontend && npm run format

# =============================================================================
# クリーンアップ
# =============================================================================

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf frontend/node_modules
	rm -rf frontend/.next
	rm -rf frontend/out
