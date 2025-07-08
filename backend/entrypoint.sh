#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Django backend setup..."

# Wait for database to be ready
echo "⏳ Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done
echo "✅ Database is ready!"

# Run migrations
echo "📦 Running database migrations..."
python manage.py migrate

# Create superuser if it doesn't exist
echo "👤 Creating superuser (if not exists)..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@example.com').exists():
    User.objects.create_superuser(
        email='admin@example.com',
        username='admin',
        password='admin',
        university_name='Example University',
        category='学生',
        faculty='工学部',
        department='情報工学科',
        admission_year=2024
    )
    print('Superuser created: admin@example.com/admin')
else:
    print('Superuser already exists')
"

# Collect static files (optional)
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput || echo "⚠️  Static files collection failed, continuing..."

echo "✅ Django backend setup complete!"

# Start the development server
echo "🌐 Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000
