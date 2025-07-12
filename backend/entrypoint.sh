#!/bin/bash

# Exit on any error
set -e

# Environment detection
if [ "$DJANGO_SETTINGS_MODULE" != "core.settings_production" ]; then
    echo "🚀 Starting Django backend setup (Development)..."
    ENVIRONMENT="development"
else
    echo "🚀 Starting Django backend setup (Production)..."
    ENVIRONMENT="production"
fi

# Wait for database (only in development)
if [ "$ENVIRONMENT" = "development" ]; then
    echo "⏳ Waiting for database..."
    while ! nc -z db 5432; do
      sleep 1
    done
    echo "✅ Database is ready!"
else
    echo "🌐 Production environment detected - skipping database wait (using Supabase)"
fi

# Run migrations
echo "📦 Running database migrations..."
python manage.py migrate

# Create superuser (only in development)
if [ "$ENVIRONMENT" = "development" ]; then
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
fi

# Collect static files
echo "📁 Collecting static files..."
if [ "$ENVIRONMENT" = "development" ]; then
    python manage.py collectstatic --noinput || echo "⚠️  Static files collection failed, continuing..."
else
    python manage.py collectstatic --noinput
fi

echo "✅ Django backend setup complete!"

# Start server based on environment
if [ "$ENVIRONMENT" = "development" ]; then
    echo "🌐 Starting Django development server..."
    exec python manage.py runserver 0.0.0.0:8000
else
    echo "🌐 Starting Django production server with gunicorn..."
    exec gunicorn --bind 0.0.0.0:$PORT core.wsgi:application
fi
