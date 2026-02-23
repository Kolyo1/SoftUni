# Vinyl Collection Manager

A Django-based web application for managing your personal vinyl record collection. Keep track of your albums, artists, wishlist items, and maintain a comprehensive catalog of your vinyl library.

## Features

### 🎵 Collection Management
- **Album Catalog**: Add, edit, delete, and view your vinyl collection
- **Artist Directory**: Manage artist information and view their discography
- **Genre System**: Categorize albums by musical genres
- **Album Details**: Track release year, condition, speed, catalog numbers, and personal notes
- **Search & Filter**: Find albums quickly with built-in filtering options

### 📝 Wishlist System
- **Wishlist Management**: Keep track of albums you want to acquire
- **Priority Levels**: Set urgency levels (Low, Medium, High, Urgent)
- **Availability Tracking**: Mark when items become available for purchase
- **Price Tracking**: Set maximum price limits for wishlist items
- **Quick Actions**: Move wishlist items directly to your collection
- **Temporary Artists**: Add items for artists not yet in your database

### 🎨 Modern UI/UX
- **Clean Design**: Modern, casual interface with glass morphism effects
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Smooth Interactions**: Hover effects, transitions, and micro-animations
- **No Emojis**: Clean, professional-looking interface without emoji decorations
- **Custom CSS**: Fully custom styling without Bootstrap dependencies

### 📊 Statistics & Organization
- **Collection Stats**: View total albums and artists in your collection
- **Wishlist Overview**: Track items you're looking for
- **Priority Management**: Focus on most wanted items first
- **Multiple Views**: Grid and list layouts for different preferences

## Technology Stack

- **Backend**: Django 6.0.2
- **Database**: PostgreSQL (psycopg2-binary)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design principles
- **Architecture**: Model-View-Template (MVT) pattern

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database
- pip package manager

### Setup Instructions

1. **Clone the repository**
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

4. **Database Setup**
   - Create a PostgreSQL database named `vinyl_collection`
   - Update database settings in `vinyl_collection/settings.py`

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
vinyl_collection/
├── vinyl_collection/          # Main Django project
│   ├── settings.py            # Project settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
├── records/                   # Album management app
│   ├── models.py             # Album, Artist, Genre models
│   ├── views.py              # Album CRUD views
│   ├── urls.py               # Album URLs
│   ├── forms.py              # Album forms
│   └── templates/records/    # Album templates
├── wishlist/                  # Wishlist management app
│   ├── models.py             # WishlistItem model
│   ├── views.py              # Wishlist CRUD views
│   ├── urls.py               # Wishlist URLs
│   ├── forms.py              # Wishlist forms
│   └── templates/wishlist/   # Wishlist templates
├── templates/                 # Base templates
│   └── base.html             # Main layout template
├── static/                    # Static files
│   └── css/
│       └── style.css         # Custom styles
├── media/                     # Media files (uploads)
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Models Overview

### Album Model
- **Title**: Album name
- **Artist**: Foreign key to Artist model
- **Genre**: Many-to-many relationship with Genre
- **Release Year**: Year of release
- **Condition**: Vinyl condition (Mint, Near Mint, etc.)
- **Speed**: RPM (33, 45, 78)
- **Catalog Number**: Record label catalog number
- **Notes**: Personal notes about the album
- **Date Added**: When album was added to collection
- **Last Played**: Date album was last played

### Artist Model
- **Name**: Artist name
- **Bio**: Artist biography/description
- **Formed Year**: Year artist was formed
- **Country**: Country of origin

### WishlistItem Model
- **Album Title**: Desired album name
- **Artist**: Existing artist (optional)
- **Temporary Artist**: Artist name for new entries
- **Priority**: Urgency level (Low, Medium, High, Urgent)
- **Max Price**: Maximum willing to pay
- **Notes**: Additional notes
- **Is Available**: Whether item is available for purchase

## Usage Guide

### Managing Your Collection

1. **Adding Albums**
   - Click "Add Album" in the navigation
   - Fill in album details including artist, genre, and condition
   - Save to add to your collection

2. **Managing Artists**
   - Navigate to Artists section
   - View all artists and their albums
   - Add new artists when needed

3. **Using the Wishlist**
   - Click "Add to Wishlist" to add desired albums
   - Set priority levels to focus on important items
   - Mark items as available when you find them
   - Move items to collection when purchased

### Features Tips

- **Quick Actions**: Use the "Add to Collection" button on wishlist items to quickly move them
- **Priority Management**: Set urgency levels to organize your wishlist effectively
- **Temporary Artists**: Add wishlist items for artists not yet in your database
- **Search & Filter**: Use the filtering options to find specific albums or artists

## Customization

### Styling
The application uses custom CSS located in `static/css/style.css`. Key features:
- Glass morphism effects
- Gradient backgrounds
- Smooth transitions
- Responsive design
- Modern color palette

### Adding New Features
The project follows Django's app structure:
- Create new apps for additional functionality
- Follow the existing model-view-template pattern
- Use the established CSS classes for consistent styling

## Deployment

### Production Considerations
- Update `DEBUG = False` in settings.py
- Configure proper database settings
- Set up static files serving
- Configure security settings (SECRET_KEY, ALLOWED_HOSTS)
- Set up proper logging

### Environment Variables
Consider using environment variables for sensitive settings:
- Database credentials
- Secret key
- Debug settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or feature requests:
- Check the existing documentation
- Review the code comments
- Test in the development environment
- Consider Django's official documentation for framework-specific questions

## Future Enhancements

Potential features for future versions:
- User authentication and multiple collections
- Album cover image uploads
- Import/export functionality
- Advanced search and filtering
- Collection statistics and analytics
- Social features (sharing collections)
- Integration with music APIs (Discogs, Spotify)
- Mobile app companion

---

**Made with love for vinyl enthusiasts** 🎵

Enjoy building and managing your vinyl collection!
