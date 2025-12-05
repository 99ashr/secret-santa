# 🎄 Secret Santa on Render — Quick Start (5 min)

Your Django app is ready for Render! Here's the fastest path to live:

## 🚀 Go Live in 5 Steps

### Step 1: Go to Render (1 min)
- Open https://render.com
- Click **"Sign up"** → **"Continue with GitHub"**
- Authorize Render to access your GitHub
- You're on the Dashboard

### Step 2: Connect Your Repo (1 min)
- Click **"New +"** → **"Web Service"**
- Click **"Connect Repository"** → find **"secret-santa"** → **"Connect"**

### Step 3: Configure (1 min)
- **Name:** `secret-santa`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn secret_santa_config.wsgi`
- **Plan:** Select **Free**

### Step 4: Add Environment Variables (1 min)

Add these:
| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*` |

### Step 5: Create & Wait (2 min)
- Click **"Create Web Service"**
- Watch the build log (takes 2–3 minutes)
- Wait for ✅ **"Service is live"** message

---

## 🗄️ Set Up Database (2 min after service is live)

### In Render Shell:
```bash
# Run migrations
python manage.py migrate

# Create admin
python manage.py createsuperuser
# Follow prompts for username, email, password

# Load 34 team members
python manage.py populate_participants
```

---

## ✅ Test Your App (1 min)

Get your URL from Render Dashboard (top of page): `https://secret-santa-xxxxx.onrender.com`

Open in browser:
- **Admin dashboard:** `https://secret-santa-xxxxx.onrender.com/`
- **Participant reveal page:** `https://secret-santa-xxxxx.onrender.com/participant/`
- **Django admin:** `https://secret-santa-xxxxx.onrender.com/admin/`

---

## 📤 Share with Team (1 min)

Send this to your 34 team members:
```
https://secret-santa-xxxxx.onrender.com/participant/
```

Each person:
1. Opens link
2. Enters their token (you provide from admin dashboard)
3. Clicks "Unwrap Gift"
4. Sees recipient name + confetti 🎉

---

## 📖 Full Details

Read the complete guide: **RENDER_DEPLOYMENT_GUIDE.md** (in your project folder)

Contains:
- Detailed troubleshooting
- Custom domain setup (optional)
- Auto-deploy on Git push
- Admin panel walkthrough

---

## ⏱️ Timeline

| Step | Time |
|------|------|
| Render signup + connect repo | 2 min |
| Configure service | 1 min |
| Add env vars | 1 min |
| Build & deploy | 3 min |
| Database setup | 2 min |
| Test app | 1 min |
| **Total** | **~10 min** |

---

## 💰 Cost

**$0/month** (Render free tier)

- App hosting: Free
- Database: Free PostgreSQL
- SSL/HTTPS: Free
- Custom domain: Optional ($12/year)

---

## 🎉 You're Done!

Your Secret Santa app is live on the internet! 

Next: Follow Steps 1–5 above to deploy on Render.

Questions? Check RENDER_DEPLOYMENT_GUIDE.md for detailed explanations and troubleshooting.

Happy Secret Santa! 🎄✨
