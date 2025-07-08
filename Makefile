.PHONY: help install install-backend install-frontend dev dev-backend dev-frontend dev-docker build test lint format clean docker-up docker-down docker-build docker-logs

help:
	@echo "Available commands:"
	@echo "  install         - Install dependencies for both backend and frontend"
	@echo "  install-backend - Install Python dependencies"
	@echo "  install-frontend- Install Node.js dependencies"
	@echo "  dev             - Start development servers using Docker (recommended)"
	@echo "  dev-backend     - Start Django development server locally"
	@echo "  dev-frontend    - Start Next.js development server locally"
	@echo "  dev-docker      - Start development servers using Docker"
	@echo "  build           - Build the frontend application"
	@echo "  test            - Run tests for both backend and frontend"
	@echo "  lint            - Run linters for both backend and frontend"
	@echo "  format          - Format code for both backend and frontend"
	@echo "  clean           - Clean build artifacts and cache"
	@echo "  docker-up       - Start Docker services"
	@echo "  docker-down     - Stop Docker services"
	@echo "  docker-build    - Build Docker images"
	@echo "  docker-logs     - Show Docker logs"

# =============================================================================
# 依存関係のインストール
# =============================================================================

install: install-backend install-frontend

install-backend:
	cd backend && pip install -r requirements.txt

install-frontend:
	cd frontend && npm install

# =============================================================================
# 開発環境の起動
# =============================================================================

dev: docker-up
	@echo ""
	@echo "🚀 Development environment is starting..."
	@echo "📊 Backend API: http://localhost:8000"
	@echo "🌐 Frontend App: http://localhost:3000"
	@echo "🗄️  Database: http://localhost:5432"
	@echo ""
	@echo "📝 Useful commands:"
	@echo "  make docker-logs    - View logs"
	@echo "  make docker-down    - Stop services"
	@echo "  make clean          - Clean up"
	@echo ""
	@echo "⏳ Waiting for services to be ready..."
	@sleep 10
	@echo "✅ Services are ready! Open http://localhost:3000 in your browser"

dev-backend:
	cd backend && python manage.py runserver

dev-frontend:
	cd frontend && npm run dev

dev-docker: docker-up
	@echo "Docker development environment started"
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:3000"

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

# =============================================================================
# ビルドとテスト
# =============================================================================

build:
	cd frontend && npm run build

test:
	cd backend && python manage.py test
	cd frontend && npm test

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
