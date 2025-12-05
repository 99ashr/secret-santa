# 🎄 Secret Santa - Free Hosting Guide

## Free Hosting Options for Django Apps

### **Option 1: Render (RECOMMENDED - Easiest) ⭐**

**Pros:**

- ✅ Free tier with automatic deployments from GitHub
- ✅ PostgreSQL database included free
- ✅ Custom domain support
- ✅ Automatic SSL certificates
- ✅ Simple setup (5 minutes)

**Cons:**

- Free tier spins down after 15 minutes of inactivity (cold starts ~30 seconds)

**Steps:**

1. **Create Render Account**

   - Go to https://render.com
   - Sign up with GitHub account

2. **Push Project to GitHub**

   ```bash
   # Initialize git repo
   git init
   git add .
   git commit -m "Secret Santa Django App"

   # Create new repo on github.com
   # Then push:
   git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Render**

   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `secret-santa` repo
   - Configuration:
     - **Name**: secret-santa
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py populate_participants`
     - **Start Command**: `gunicorn secret_santa_config.wsgi`
   - Click "Create Web Service"

4. **Configure Environment Variables**

   - In Render dashboard → Settings → Environment
   - Add these variables:
     ```
     DEBUG=False
     SECRET_KEY=your-random-secret-key
     ALLOWED_HOSTS=*.render.com,yourdomain.com
     DATABASE_URL=postgres://...  (auto-provided)
     ```

5. **Create Superuser**
   - Go to "Shell" in Render dashboard
   - Run: `python manage.py createsuperuser`

---

### **Option 2: Railway (Also Easy)**

**Pros:**

- ✅ $5 free credits monthly (usually enough for this app)
- ✅ GitHub integration
- ✅ PostgreSQL included
- ✅ Very user-friendly dashboard

**Steps:**

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your secret-santa repository
5. Railway auto-detects it's a Django app
6. Add PostgreSQL plugin
7. Done! (Railway deploys automatically)

---

### **Option 3: Heroku (Was Free, Now Paid but Cheapest)**

**Pros:**

- ✅ Reliable, industry standard
- ✅ Excellent documentation
- ✅ Eco Dyno ($7/month - very cheap)

**Cons:**

- Not free anymore (was free before 2022)

---

### **Option 4: PythonAnywhere (Free Tier Available)**

**Pros:**

- ✅ Completely free tier
- ✅ No credit card required
- ✅ Good for learning

**Cons:**

- Limited bandwidth
- Slower performance
- Limited customization

**Steps:**

1. Go to https://www.pythonanywhere.com
2. Create free account
3. Upload your project
4. Configure WSGI file
5. Set up static files

---

### **Option 5: Fly.io (Generous Free Tier)**

**Pros:**

- ✅ Free tier with good resources
- ✅ Global deployment
- ✅ PostgreSQL available

**Cons:**

- Slightly more technical setup

---

## 🎯 **RECOMMENDED: Deploy on Render (Step-by-Step)**

### Prerequisites

- GitHub account
- Render account (free signup)

### Step 1: Prepare Your Project for Production

Create a `Procfile` in your project root:

```
web: gunicorn secret_santa_config.wsgi
```

Update `requirements.txt` to include gunicorn:

```bash
pip install gunicorn
pip freeze > requirements.txt
```

Update `secret_santa_config/settings.py`:

```python
DEBUG = False  # IMPORTANT!
ALLOWED_HOSTS = ['*.render.com', 'yourdomain.com']  # Add your domain

# Add this for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### Step 2: Push to GitHub

```bash
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa

# Initialize git
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .
git commit -m "Secret Santa Django App - Ready for deployment"

# Create repo on github.com manually first, then:
git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render

1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Select "Deploy existing repository" or connect your GitHub
4. Select the secret-santa repo
5. Fill in configuration:

   - **Name**: secret-santa
   - **Environment**: Python 3
   - **Root Directory**: (leave empty)
   - **Build Command**:
     ```
     pip install -r requirements.txt && python manage.py migrate && python manage.py populate_participants && python manage.py collectstatic --noinput
     ```
   - **Start Command**:
     ```
     gunicorn secret_santa_config.wsgi
     ```

6. Click "Create Web Service"
7. Render will deploy automatically!

### Step 4: Create Admin User

Once deployed:

- In Render dashboard, go to "Shell"
- Run: `python manage.py createsuperuser`
- Enter username, email, password

### Step 5: Add Custom Domain (Optional)

- In Render dashboard → Settings → Custom Domains
- Add your domain
- Follow DNS configuration steps

---

## 📊 Comparison Table

| Feature                | Render         | Railway        | Heroku         | PythonAnywhere | Fly.io         |
| ---------------------- | -------------- | -------------- | -------------- | -------------- | -------------- |
| **Free Tier**          | ✅ Yes         | ✅ $5/mo       | ❌ Paid ($7+)  | ✅ Limited     | ✅ Yes         |
| **PostgreSQL**         | ✅ Free        | ✅ Free        | ❌ Paid        | ❌ Limited     | ✅ Free        |
| **GitHub Integration** | ✅ Auto Deploy | ✅ Auto Deploy | ✅ Auto Deploy | ⚠️ Manual      | ✅ Auto Deploy |
| **Ease of Setup**      | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐       | ⭐⭐⭐         | ⭐⭐⭐⭐       |
| **Performance**        | Good           | Excellent      | Excellent      | Fair           | Excellent      |
| **Always Running**     | ⚠️ Spins down  | ✅ Yes         | ✅ Yes         | ⚠️ Limited     | ✅ Yes         |

---

## ⚙️ Production Settings Checklist

Before deploying, make sure to update `settings.py`:

```python
# ❌ Change this
DEBUG = True
# ✅ To this
DEBUG = False

# ✅ Add your domain
ALLOWED_HOSTS = ['your-app.render.com', 'yourdomain.com']

# ✅ Use strong secret key (generate one)
SECRET_KEY = 'generate-a-long-random-string'

# ✅ Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# ✅ HTTPS (important)
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ✅ Database (will be set by hosting provider)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': '5432',
    }
}
```

---

## 🔧 Files You Need to Add/Update

### 1. `Procfile` (new file)

```
web: gunicorn secret_santa_config.wsgi
```

### 2. `requirements.txt` (update)

Add to your existing requirements.txt:

```
Django==6.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
python-decouple==3.8
```

### 3. `runtime.txt` (new file, optional)

```
python-3.11.7
```

### 4. `.gitignore` (already exists, make sure it has)

```
*.pyc
__pycache__/
*.sqlite3
.env
venv/
staticfiles/
```

---

## 🚀 URL After Deployment

Once deployed on Render, your app will be at:

- **Admin Dashboard**: `https://secret-santa.render.com`
- **Participant Page**: `https://secret-santa.render.com/participant`
- **Admin Login**: `https://secret-santa.render.com/admin`

Share the participant link with your team! 🎉

---

## 📱 Using a Custom Domain

If you have a domain (like `secretsanta.com`):

1. **On your domain registrar** (GoDaddy, Namecheap, etc.):

   - Go to DNS settings
   - Find CNAME record settings

2. **On Render dashboard**:

   - Settings → Custom Domains
   - Add your domain
   - Get the CNAME target value
   - Add CNAME record pointing to Render

3. **Wait 24 hours** for DNS propagation

---

## 💡 Tips

✅ **Free tier considerations:**

- Render free tier spins down after 15 minutes
- First request after spin-down takes ~30 seconds
- Still good for internal team use!

✅ **Upgrade later:**

- If you need always-running: Render Pro ($7/month)
- Or Railway/Heroku for more performance

✅ **Backup your data:**

- Render provides automatic backups
- Download database regularly if needed

✅ **Update participants easily:**

- After deploying, edit in Django admin (`/admin`)
- No need to redeploy!

---

## 🎯 Next Steps

1. **Create GitHub account** (if you don't have one)
2. **Create Render account**
3. **Push your code** to GitHub
4. **Deploy** on Render (5 minutes)
5. **Share link** with your team!

---

## 📞 Support

- **Render Docs**: https://render.com/docs
- **Django Deployment**: https://docs.djangoproject.com/en/6.0/howto/deployment/
- **Railway Docs**: https://docs.railway.app/

---

**Your Secret Santa app will be live in minutes! 🎄✨**
