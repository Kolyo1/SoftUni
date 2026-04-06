# Vinyl Collection Manager

A Django web application for managing vinyl record collections. Features user authentication, role-based permissions, async tasks, REST API, and comprehensive testing.

## Features

### Collection Management
- **Album Catalog**: Add, edit, delete, and view your vinyl collection
- **Artist Directory**: Manage artist information and view their discography  
- **Genre System**: Categorize albums by musical genres
- **Album Details**: Track release year, condition, speed, catalog numbers, and personal notes
- **Search & Filter**: Find albums quickly with built-in filtering options
- **Track Management**: Add and manage individual album tracks

### Wishlist System
- **Wishlist Management**: Keep track of albums you want to acquire
- **Priority Levels**: Set urgency levels (Low, Medium, High, Urgent)
- **Availability Tracking**: Mark when items become available for purchase
- **Price Tracking**: Set maximum price limits for wishlist items
- **Quick Actions**: Move wishlist items directly to your collection
- **Temporary Artists**: Add items for artists not yet in your database

### User Management & Authentication
- **User Registration**: Complete registration system with email validation
- **Profile System**: Extended user profiles with photos, bio, location, and website
- **Role-Based Permissions**: Three-tier permission system (Admin, Power User, Regular User)
- **Owner-Based Access**: Users can only manage their own content
- **Authentication Flow**: Login, logout, and password management

### Modern UI/UX
- **Clean Design**: Modern interface with responsive design
- **Custom Error Pages**: Beautiful 403, 404, and 500 error pages
- **Template Filters**: Custom template tags for enhanced display
- **Form Validation**: Advanced form validation with disabled/read-only fields
- **Bootstrap Integration**: Professional UI components

### Statistics & Organization
- **Collection Stats**: View total albums and artists in your collection
- **Wishlist Overview**: Track items you're looking for
- **Priority Management**: Focus on most wanted items first
- **Async Processing**: Background tasks for statistics and notifications

### REST API
- **DRF Integration**: Full REST API with Django REST Framework
- **Album Endpoints**: Complete CRUD operations for albums
- **Artist Endpoints**: Read-only access to artist data
- **Review System**: API endpoints for album reviews
- **Authentication**: Session-based API authentication

### Async Processing
- **Celery Integration**: Background task processing with Redis
- **Email Notifications**: Automated emails for wishlist availability and statistics
- **Scheduled Tasks**: Daily statistics generation and cleanup
- **Collection Reports**: Weekly collection summaries

## Technology Stack

- **Backend**: Django 6.0.2
- **Database**: PostgreSQL with psycopg2-binary
- **Task Queue**: Celery with Redis
- **REST API**: Django REST Framework 3.14.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5 with custom CSS
- **Testing**: Django TestCase with comprehensive coverage
- **Authentication**: Django's built-in auth system

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database
- Redis server (for Celery)
- pip package manager

### Setup Instructions

1. **Clone repository**
   ```bash
   git clone <repository-url>
   cd vinyl_collection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Database Setup**
   - Create a PostgreSQL database named `vinyl_db`
   - Update database settings in `.env` file

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create user groups and permissions**
   ```bash
   python manage.py init_groups
   ```

8. **Create superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

9. **Start Redis server** (for Celery)
   ```bash
   redis-server
   ```

10. **Start Celery worker** (in separate terminal)
    ```bash
    celery -A vinyl_collection worker --loglevel=info
    ```

11. **Start Celery beat** (in separate terminal)
    ```bash
    celery -A vinyl_collection beat --loglevel=info
    ```

12. **Run development server**
    ```bash
    python manage.py runserver
    ```

13. **Access the application**
    - Main site: `http://127.0.0.1:8000/`
    - Admin panel: `http://127.0.0.1:8000/admin/`
    - API: `http://127.0.0.1:8000/api/`

## Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Settings
DB_NAME=vinyl_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Celery Settings
CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=Vinyl Collection <noreply@vinylcollection.com>

# Site Settings
SITE_URL=http://127.0.0.1:8000
```

## Testing

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test records
python manage.py test users
python manage.py test api

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Coverage
- **Models**: All model methods and properties
- **Views**: All CRUD operations and permissions
- **Forms**: Form validation and custom methods
- **API**: All endpoints and authentication
- **Tasks**: Async task functionality

## User Roles & Permissions

### Collection Admins
- Full access to all models (add, change, delete, view)
- Can manage all users' content
- Access to admin panel

### Power Users
- Can add and edit content (no delete permissions)
- Can manage their own content fully
- Limited administrative access

### Regular Users
- Can add and edit their own content only
- Cannot delete content
- Basic user permissions

## API Endpoints

### Albums
- `GET /api/albums/` - List user's albums
- `POST /api/albums/` - Create new album
- `GET /api/albums/{id}/` - Get album details
- `PUT /api/albums/{id}/` - Update album
- `DELETE /api/albums/{id}/` - Delete album
- `POST /api/albums/{id}/add_review/` - Add review to album
- `GET /api/albums/{id}/reviews/` - Get album reviews

### Artists
- `GET /api/artists/` - List all artists
- `GET /api/artists/{id}/` - Get artist details

### Reviews
- `GET /api/reviews/` - List reviews
- `POST /api/reviews/` - Create review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review (author only)
- `DELETE /api/reviews/{id}/` - Delete review (author only)

## Django Advanced Exam Compliance

✅ **Architecture**: 5+ Django apps with clear separation
✅ **Authentication**: Complete user auth system with profile extension
✅ **Permissions**: Role-based groups with proper access control
✅ **Models**: 5+ models with required relationships (M2M, M2O)
✅ **Views**: CBV-dominant with owner-based CRUD
✅ **Forms**: 7+ forms with validation and disabled fields
✅ **Templates**: 15+ reachable pages with shared base template
✅ **API**: DRF-powered endpoints with authentication
✅ **Async**: Celery tasks for statistics and notifications
✅ **Tests**: 15+ comprehensive tests covering all functionality
✅ **Configuration**: Environment-based settings with security
✅ **Documentation**: Complete README with setup instructions

## License

This project is open source and available under MIT License.

---

**Built with ❤️ for vinyl enthusiasts and Django developers**
