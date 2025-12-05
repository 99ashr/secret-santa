# 🎅 Secret Santa - Quick Start Guide

## Current Status ✅

- ✅ Django project scaffolded
- ✅ Models created (Participant, DrawMapping)
- ✅ Views implemented (admin, participant, API endpoints)
- ✅ URLs configured
- ✅ Templates created (beautiful festive design)
- ✅ Database migrations applied
- ✅ 34 participants pre-populated
- ✅ Admin interface configured
- ✅ System check passed

## What's Included

### Backend

- **Django 6.0** web framework
- **SQLite3** database (auto-created)
- **Derangement algorithm** for fair Secret Santa draw
- **Token-based reveal system** with validation
- **RESTful API** endpoints for draw management

### Frontend

- **Admin Dashboard** - Generate draws, view tokens, print for distribution
- **Participant Page** - Enter token, reveal recipient with animation
- **Festive Design** - Snow effects, SVG garland, confetti celebration
- **Responsive** - Works on desktop, tablet, and mobile

### Features

✨ Beautiful UI with animations
🎁 Interactive gift unwrap animation
❄️ Snowfall background effect
🎉 Confetti celebration on reveal
📋 Print-friendly token distribution
🔒 Server-side token validation
📱 Mobile responsive design

## First Time Setup

### 1. Create a Superuser (Required for Admin)

```bash
# Activate virtual environment first
source venv/bin/activate

# Create admin account
python manage.py createsuperuser

# Enter username (e.g., "admin")
# Enter email (e.g., "admin@example.com")
# Enter password (enter it twice)
```

### 2. Start Development Server

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate

# Start server
python manage.py runserver

# Output will show: Starting development server at http://127.0.0.1:8000/
```

### 3. Access the Application

**Admin Dashboard** (Main page)

- URL: http://127.0.0.1:8000/
- Generate draws, view tokens, print for distribution

**Django Admin** (Manage data)

- URL: http://127.0.0.1:8000/admin/
- Login with superuser credentials
- Add/edit/delete participants and draws

**Participant Page** (For Secret Santa participants)

- URL: http://127.0.0.1:8000/participant/
- Enter token to reveal recipient
- Share this link with participants after generating draw

## Workflow

### Step 1: Generate Draw (Admin)

1. Go to http://127.0.0.1:8000/
2. Click "🎁 Generate Secret Santa Draw"
3. You'll see success message with token count
4. Click "📋 Show All Tokens" to view the generated tokens

### Step 2: Distribute Tokens

1. Click "🖨️ Print Tokens for Distribution"
2. Print or screenshot the list
3. Distribute each token to the corresponding "giver" listed
4. Example: Token ABC123 goes to "Alice Johnson"

### Step 3: Participants Reveal

1. Share the participant page link: http://127.0.0.1:8000/participant/
2. Each participant enters their token
3. Click the gift or "Reveal" button
4. See who their Secret Santa recipient is! 🎉

## Key URLs

| Page                | URL                                | Purpose                    |
| ------------------- | ---------------------------------- | -------------------------- |
| Admin Dashboard     | http://127.0.0.1:8000/             | Generate & manage draws    |
| Django Admin        | http://127.0.0.1:8000/admin/       | Manage participants & data |
| Participant Reveal  | http://127.0.0.1:8000/participant/ | Enter token & reveal       |
| API - Generate Draw | /api/generate-draw/                | POST endpoint              |
| API - Show Tokens   | /api/show-tokens/                  | GET endpoint               |
| API - Clear Draw    | /api/clear-draw/                   | POST endpoint              |
| API - Reveal        | /api/reveal/                       | POST endpoint              |

## Database

The SQLite database (`db.sqlite3`) is automatically created and includes:

**Participants Table**

- 34 pre-loaded names
- Email field (optional)

**DrawMapping Table**

- Unique 6-character tokens
- Giver & Recipient relationships
- Reveal status tracking
- Created & Revealed timestamps

### Reset Database (if needed)

```bash
# Delete the database file
rm db.sqlite3

# Recreate from scratch
python manage.py migrate
python manage.py populate_participants
```

## Customization

### Add More Participants

Edit `secret_santa/management/commands/populate_participants.py`:

1. Find the `participants` list
2. Add more names to the list
3. Run: `python manage.py populate_participants --force`

### Change Colors

Edit the CSS in templates:

- `templates/secret_santa/admin.html` - Admin panel colors
- `templates/secret_santa/participant.html` - Participant page colors

Look for color codes like:

- `#0b3b2e` (dark green) - Primary color
- `#06B6D4` (cyan) - Accent color
- `#FF6B6B`, `#6BCB77`, etc. - Festive colors

### Change Participant List

1. Go to http://127.0.0.1:8000/admin/
2. Click "Participants"
3. Add/edit/delete as needed
4. New participants will be included in next draw

## Deployment Notes

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Set `ALLOWED_HOSTS` appropriately
3. Use a production database (PostgreSQL recommended)
4. Use gunicorn or similar WSGI server
5. Collect static files: `python manage.py collectstatic`
6. Set environment variables for SECRET_KEY
7. Use HTTPS

## Troubleshooting

**Q: Server won't start**

- Check if port 8000 is available
- Try: `python manage.py runserver 8080` (different port)

**Q: Can't login to admin**

- Make sure you ran `python manage.py createsuperuser`
- Check superuser was created: `python manage.py shell` then `from django.contrib.auth.models import User; User.objects.all()`

**Q: Database errors**

- Reset: `rm db.sqlite3 && python manage.py migrate && python manage.py populate_participants`

**Q: Static files warning**

- Can be ignored for development
- For production: `python manage.py collectstatic`

## Next Steps

1. ✅ Start the server
2. ✅ Create superuser
3. ✅ Generate a test draw
4. ✅ Test participant reveal
5. ✅ Customize if needed
6. ✅ Have fun! 🎉

---

**Enjoy your Secret Santa draw! 🎄✨**
