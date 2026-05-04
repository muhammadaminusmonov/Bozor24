# Bozor24 🛒

> **A Multi-vendor E-commerce Marketplace Platform for Uzbekistan**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.16.0-red.svg)](https://www.django-rest-framework.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://www.postgresql.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bozor24 is a comprehensive multi-vendor marketplace platform designed for the Uzbekistan market, supporting **Food, Grocery, eCommerce, Pharmacy & Parcel delivery services**. Built with Django and Django REST Framework, it provides a scalable backend API for web and mobile applications.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Documentation](#-api-documentation)
- [Configuration](#-configuration)
- [Development](#-development)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🛍️ Marketplace Core
- **Multi-vendor Support**: Sellers can register, manage stores, and list products
- **Product Management**: Categories, attributes, variants, inventory tracking
- **Advanced Search & Filtering**: By category, region, price, attributes
- **Reviews & Comments**: User-generated content for products

### 🛒 Shopping Experience
- **Shopping Cart**: Persistent cart with quantity management
- **Order Management**: Order creation, status tracking, history
- **Multiple Payment Methods**: Integrated payment gateway support
- **Regional Delivery**: Location-based shipping to Uzbekistan regions

### 👥 User Features
- **Authentication**: JWT-based auth with refresh tokens
- **User Profiles**: Buyer and seller account management
- **Notifications**: Real-time order and system notifications
- **Support Chat**: Integrated customer support messaging

### ⚙️ Admin & Operations
- **Django Admin**: Enhanced with Jazzmin theme for intuitive management
- **Media Handling**: Image upload and optimization with Pillow
- **API-First Design**: RESTful endpoints for mobile/web clients

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.10+, Django 5.2 |
| **API** | Django REST Framework 3.16.0, SimpleJWT 5.5.0 |
| **Database** | PostgreSQL 12+ (psycopg2-binary) |
| **Admin UI** | Django Jazzmin 3.0.1 |
| **Templating** | Jinja2 3.1.6 |
| **Media** | Pillow 11.2.1 |
| **Filters** | django-filter 25.1 |
| **Utilities** | PyJWT, sqlparse, tzdata |

---

## 📁 Project Structure

```
Bozor24/
├── src/
│   ├── bozor/              # Main project settings & config
│   ├── api/                # API views, serializers, URLs
│   ├── user/               # Authentication & user profiles
│   ├── product/            # Product models & logic
│   ├── category/           # Category management
│   ├── attribute/          # Product attributes & variants
│   ├── cart/               # Shopping cart functionality
│   ├── orders/             # Order processing & management
│   ├── payment/            # Payment gateway integration
│   ├── region/             # Geographic regions (Uzbekistan)
│   ├── review/             # Product reviews & ratings
│   ├── comment/            # Product comments
│   ├── notification/       # User notification system
│   ├── supportchat/        # Customer support chat
│   ├── media/              # Uploaded media files
│   ├── manage.py           # Django management script
│   └── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Virtual environment tool (venv, virtualenv, or conda)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/muhammadaminusmonov/Bozor24.git
cd Bozor24
```

2. **Create and activate virtual environment**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n bozor24 python=3.10
conda activate bozor24
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
# Create .env file in src/ directory
cp src/.env.example src/.env  # If template exists
```

Edit `src/.env` with your configuration:
```env
# Database
DATABASE_NAME=bozor24_db
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# JWT
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440

# Media
MEDIA_URL=/media/
MEDIA_ROOT=media/
```

5. **Run database migrations**
```bash
cd src
python manage.py migrate
```

6. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

7. **Start development server**
```bash
python manage.py runserver
```

🎉 The API server will be available at `http://localhost:8000`

---

## 📚 API Documentation

### Authentication Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login & receive JWT tokens |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| POST | `/api/auth/logout/` | Logout user |

### Core Resources
| Resource | Base Endpoint | Methods |
|----------|--------------|---------|
| Products | `/api/products/` | GET, POST |
| Categories | `/api/categories/` | GET |
| Cart | `/api/cart/` | GET, POST, PUT, DELETE |
| Orders | `/api/orders/` | GET, POST |
| Reviews | `/api/reviews/` | GET, POST, PUT, DELETE |
| Regions | `/api/regions/` | GET |

### Example: Fetch Products
```bash
curl -X GET http://localhost:8000/api/products/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example: Create Order
```bash
curl -X POST http://localhost:8000/api/orders/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "items": [{"product_id": 1, "quantity": 2}],
    "delivery_address": "Tashkent, Uzbekistan",
    "payment_method": "card"
  }'
```

> 🔐 Most endpoints require authentication. Include the JWT token in the `Authorization` header.

---

## ⚙️ Configuration

### Database Setup (PostgreSQL)
```sql
-- Create database and user
CREATE DATABASE bozor24_db;
CREATE USER bozor_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE bozor24_db TO bozor_user;
```

### Static & Media Files
```bash
# Collect static files for production
python manage.py collectstatic

# Ensure media directory exists and is writable
mkdir -p src/media
chmod -R 755 src/media
```

### Django Settings Highlights
- **Custom User Model**: Extended for buyer/seller roles
- **REST Framework**: Configured with JWT authentication, pagination, filtering
- **CORS**: Configured for frontend/mobile app integration
- **Logging**: Structured logging for debugging and monitoring

---

## 👨‍💻 Development

### Running Tests
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test product

# With coverage
coverage run manage.py test
coverage report
```

### Code Style & Linting
```bash
# Install dev dependencies (if available)
pip install black flake8 isort

# Format code
black src/
isort src/

# Lint
flake8 src/
```

### Making Migrations
```bash
# After model changes
python manage.py makemigrations
python manage.py migrate
```

### API Schema Generation
```bash
# Generate OpenAPI schema (if drf-spectacular installed)
python manage.py spectacular --file schema.yml
```

---

## 🚢 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure proper `SECRET_KEY` and environment variables
- [ ] Set up PostgreSQL with production credentials
- [ ] Configure static file serving (WhiteNoise, CDN, or S3)
- [ ] Set up HTTPS with proper SSL certificates
- [ ] Configure Gunicorn/Uvicorn as WSGI/ASGI server
- [ ] Set up reverse proxy (Nginx/Apache)
- [ ] Enable database backups and monitoring

### Docker (Optional)
```dockerfile
# Example Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
EXPOSE 8000

CMD ["gunicorn", "bozor.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Environment Variables for Production
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:pass@prod-db:5432/bozor24
ALLOWED_HOSTS=bozor24.com,www.bozor24.com
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
