# 🚀 Secret Santa - Production Deployment Checklist

## Before You Deploy

### ✅ Step 1: Update settings.py for Production

Edit `secret_santa_config/settings.py` and make these changes:

```python
# At the top of the file, add:
import os
from pathlib import Path

# ... existing code ...

# Change DEBUG
DEBUG = False  # ⚠️ CRITICAL: Must be False

# Add your hosting domain
ALLOWED_HOSTS = ['your-app.render.com', 'yourdomain.com']

# Generate a new secret key (use online generator)
SECRET_KEY = 'django-insecure-GENERATE-A-NEW-ONE'

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Whitenoise for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ADD THIS
    # ... rest of middleware ...
]

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Database - use environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', 'postgres'),
        'USER': os.getenv('DATABASE_USER', 'postgres'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}
```

### ✅ Step 2: Create .env File (for local testing)

Create `.env` file in project root:

```
DEBUG=False
SECRET_KEY=your-new-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
DATABASE_URL=sqlite:///db.sqlite3
```

### ✅ Step 3: Update requirements.txt

Make sure your `requirements.txt` has:

```
Django==6.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
python-decouple==3.8
```

### ✅ Step 4: Create Procfile

Create `Procfile` (no extension) in project root:

```
web: gunicorn secret_santa_config.wsgi
release: python manage.py migrate && python manage.py populate_participants && python manage.py collectstatic --noinput
```

### ✅ Step 5: Create runtime.txt

Create `runtime.txt` in project root:

```
python-3.11.7
```

### ✅ Step 6: Prepare for Git

Create/update `.gitignore`:

```
*.pyc
__pycache__/
*.sqlite3
.env
venv/
staticfiles/
*.egg-info/
dist/
build/
.DS_Store
```

### ✅ Step 7: Push to GitHub

```bash
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa

# Initialize git (if not already done)
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .
git commit -m "Secret Santa - Ready for production deployment"

# Create new repo on github.com first, then:
git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git
git branch -M main
git push -u origin main
```

## Deploy on Render

### Step 1: Create Render Account

- Go to https://render.com
- Sign up with GitHub

### Step 2: Connect Repository

- Click "New +" → "Web Service"
- Click "Connect Repository"
- Select your secret-santa repo

### Step 3: Configure Deployment

- **Name**: secret-santa
- **Environment**: Python 3
- **Build Command**:
  ```
  pip install -r requirements.txt && python manage.py migrate && python manage.py populate_participants && python manage.py collectstatic --noinput
  ```
- **Start Command**:
  ```
  gunicorn secret_santa_config.wsgi
  ```

### Step 4: Add Environment Variables

Click "Environment" and add:

```
DEBUG=False
SECRET_KEY=generate-long-random-string
ALLOWED_HOSTS=*.render.com,yourdomain.com
DATABASE_URL=your-postgres-url
```

### Step 5: Deploy

Click "Create Web Service" and wait for deployment (2-5 minutes)

### Step 6: Create Admin User

- In Render dashboard, go to "Shell"
- Run: `python manage.py createsuperuser`
- Enter: username, email, password

### Step 7: Test

- Visit your app URL
- Login to admin
- Generate a test draw

## Environment Variables Explained

| Variable        | Purpose                           | Example                           |
| --------------- | --------------------------------- | --------------------------------- |
| `DEBUG`         | Show errors (False in production) | False                             |
| `SECRET_KEY`    | Django security key               | long-random-string                |
| `ALLOWED_HOSTS` | Allowed domains                   | \*.render.com,yourdomain.com      |
| `DATABASE_URL`  | PostgreSQL connection             | postgres://user:pass@host:5432/db |

## Security Checklist

- [ ] DEBUG = False
- [ ] SECRET_KEY is unique and long (50+ characters)
- [ ] ALLOWED_HOSTS has your domains
- [ ] SECURE_SSL_REDIRECT = True
- [ ] SESSION_COOKIE_SECURE = True
- [ ] CSRF_COOKIE_SECURE = True
- [ ] Database is PostgreSQL (not SQLite)
- [ ] Admin user created with strong password
- [ ] Static files collected (`collectstatic`)

## Troubleshooting Deployment

### App keeps crashing?

- Check build logs in Render dashboard
- Look for syntax errors in settings.py
- Verify all dependencies in requirements.txt

### Database not migrating?

- Check "Shell" tab in Render
- Run: `python manage.py migrate`
- Check: `python manage.py showmigrations`

### Static files not loading?

- Run: `python manage.py collectstatic --noinput`
- Check STATIC_ROOT and STATIC_URL settings
- Verify WhiteNoise middleware is in MIDDLEWARE list

### Can't login to admin?

- In Shell: `python manage.py createsuperuser`
- Check admin URL: `/admin/`

## After Deployment

1. **Test the app**

   - Generate a draw
   - Test participant reveal page
   - Check admin interface

2. **Monitor performance**

   - Render dashboard shows metrics
   - Check for errors in logs

3. **Set up custom domain** (optional)

   - Add in Render settings
   - Update DNS on your registrar

4. **Enable auto-deploys**

   - Already enabled by default
   - Pushes to main branch auto-deploy

5. **Backup data** (optional)
   - Render provides automatic backups
   - Export data periodically

## Upgrading from Free Tier

If you need better performance:

- Render Pro: $7/month (always running)
- Railway: $5/month + usage
- Both support paid database upgrades

## Getting Help

- **Render Support**: https://render.com/support
- **Django Docs**: https://docs.djangoproject.com/
- **Common Issues**: Check Render dashboard logs

---

**Your app will be live in 5-10 minutes! 🎄✨**
