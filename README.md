<<<<<<< HEAD
# secret-santa
Secret Santa Draw Application
=======
# 🎅 Secret Santa Django Application

A festive web application for managing Secret Santa draws with a beautiful, interactive UI.

## Features

✨ **Admin Panel**

- Generate Secret Santa draws using derangement algorithm (no one gets themselves)
- View and print tokens for distribution
- Clear and manage existing draws
- Beautiful admin dashboard with real-time statistics

🎁 **Participant Page**

- Enter token to reveal Secret Santa recipient
- Interactive gift unwrap animation
- Confetti celebration animation
- Mobile-friendly design

❄️ **Design**

- Festive theme with snow animation
- Responsive design (desktop & mobile)
- Smooth animations and transitions
- 34 pre-configured participants

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone or navigate to project directory**

   ```bash
   cd "Christmas Secret Santa"
   ```

2. **Activate virtual environment**

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup** (already done, but if needed):

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py populate_participants
   ```

5. **Create superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

### Running the Application

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate

# Run development server
python manage.py runserver
```

Server will be available at: `http://127.0.0.1:8000/`

## Access the Application

### Admin Panel

- **URL**: `http://127.0.0.1:8000/`
- **Features**:
  - Generate draws
  - View all tokens
  - Print tokens
  - Clear draws

### Django Admin Interface

- **URL**: `http://127.0.0.1:8000/admin/`
- **Login**: Use superuser credentials created above
- **Manage**: Participants, Draw Mappings

### Participant Reveal Page

- **URL**: `http://127.0.0.1:8000/participant/`
- **How to use**:
  1. Enter the 6-character token provided by admin
  2. Click the gift box or "Reveal" button
  3. See who your Secret Santa recipient is! 🎉

## Project Structure

```
.
├── manage.py                          # Django management script
├── requirements.txt                    # Python dependencies
├── db.sqlite3                         # SQLite database (auto-created)
├── venv/                              # Virtual environment
├── secret_santa_config/               # Project configuration
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
├── secret_santa/                      # Main app
│   ├── models.py                      # Participant & DrawMapping models
│   ├── views.py                       # View functions
│   ├── urls.py                        # App URL routing
│   ├── admin.py                       # Django admin configuration
│   ├── management/
│   │   └── commands/
│   │       └── populate_participants.py  # Management command
│   ├── migrations/                    # Database migrations
│   └── __init__.py
├── templates/
│   └── secret_santa/
│       ├── admin.html                 # Admin dashboard
│       └── participant.html           # Participant reveal page
└── static/                            # Static files (CSS, JS, images)
```

## API Endpoints

### POST `/api/generate-draw/`

Generate a new Secret Santa draw for all participants.

**Response**:

```json
{
  "success": true,
  "message": "Draw generated successfully for X participants",
  "count": X
}
```

### GET `/api/show-tokens/`

Get all generated tokens and assignments.

**Response**:

```json
{
  "success": true,
  "tokens": [
    {
      "token": "ABC123",
      "giver": "Alice Johnson",
      "created_at": "2024-12-05 15:30:00"
    }
  ],
  "total": X
}
```

### POST `/api/clear-draw/`

Delete all current draws and tokens.

**Response**:

```json
{
  "success": true,
  "message": "Cleared X draw mappings"
}
```

### POST `/api/reveal/`

Reveal the recipient for a given token.

**Request**:

```json
{
  "token": "ABC123"
}
```

**Response**:

```json
{
  "success": true,
  "recipient": "Bob Smith",
  "message": "Your Secret Santa recipient is: Bob Smith! 🎄"
}
```

## Customization

### Adding/Modifying Participants

1. Access Django admin: `http://127.0.0.1:8000/admin/`
2. Go to "Participants" section
3. Add, edit, or delete participants as needed

### Changing Colors/Theme

Edit the CSS in:

- `templates/secret_santa/admin.html` (Admin panel styling)
- `templates/secret_santa/participant.html` (Participant page styling)

Look for the `<style>` section and modify the color values:

- Primary color: `#0b3b2e` (dark green)
- Accent color: `#06B6D4` (cyan)
- Success color: `#10B981` (green)

## Features in Detail

### Derangement Algorithm

The application uses a sophisticated derangement algorithm to ensure:

- No person is assigned themselves
- Random shuffling for fairness
- Fallback logic for edge cases (up to 5000 attempts)

### Token System

- 6-character alphanumeric tokens (e.g., "ABC123")
- Unique token generation
- Server-side token validation
- One-time reveal tracking

### Security Features

- CSRF protection on all POST requests
- Token-based reveal (prevents guessing)
- Sensitive recipient info only shown after valid token
- Django admin protection

## Troubleshooting

### "Page not found" errors

- Make sure development server is running: `python manage.py runserver`
- Check URL spelling (case-sensitive)

### Database errors

- Reset database: `python manage.py migrate --run-syncdb`
- Repopulate participants: `python manage.py populate_participants`

### Static files warning

- This warning can be ignored for development
- For production, run: `python manage.py collectstatic`

## Support

For issues or questions, check the Django documentation:

- Django Official Docs: https://docs.djangoproject.com/

## License

This is a festive application created for fun! Use and modify as needed.

---

**Happy Secret Santa! 🎄✨**
>>>>>>> d994aee (Secret Santa Project)
