.PHONY: help install install-backend install-frontend dev dev-backend dev-frontend build test lint format clean

help:
	@echo "Available commands:"
	@echo "  install         - Install dependencies for both backend and frontend"
	@echo "  install-backend - Install Python dependencies"
	@echo "  install-frontend- Install Node.js dependencies"
	@echo "  dev             - Start development servers for both backend and frontend"
	@echo "  dev-backend     - Start Django development server"
	@echo "  dev-frontend    - Start Next.js development server"
	@echo "  build           - Build the frontend application"
	@echo "  test            - Run tests for both backend and frontend"
	@echo "  lint            - Run linters for both backend and frontend"
	@echo "  format          - Format code for both backend and frontend"
	@echo "  clean           - Clean build artifacts and cache"

install: install-backend install-frontend

install-backend:
	cd backend && pip install -r requirements.txt

install-frontend:
	cd frontend && npm install

dev:
	@echo "Starting development servers..."
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:3000"
	$(MAKE) -j2 dev-backend dev-frontend

dev-backend:
	cd backend && python manage.py runserver

dev-frontend:
	cd frontend && npm run dev

build:
	cd frontend && npm run build

test:
	cd backend && python manage.py test
	cd frontend && npm test

lint:
	cd backend && flake8 .
	cd frontend && npm run lint

format:
	cd backend && black . && isort .
	cd frontend && npm run format

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf frontend/node_modules
	rm -rf frontend/.next
	rm -rf frontend/out