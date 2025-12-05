# 🚀 Deploy Secret Santa App to Render.com (Complete Step-by-Step Guide)

## Overview

You're deploying a Django 6.0 app with 34 team members to Render.com (free tier). Total time: ~10 minutes.

**What you get:**

- Live URL: `https://your-app-name.onrender.com`
- Free tier PostgreSQL database
- Automatic HTTPS/SSL
- Auto-deployment on every GitHub push
- No credit card required (free tier)

---

## Prerequisites

Before you start:

- ✅ GitHub account (you have one: @99ashr)
- ✅ GitHub repository created: `secret-santa` (at https://github.com/99ashr/secret-santa)
- ✅ Code pushed to GitHub (you need to complete this first if not done)
- ✅ Django project files ready (Procfile, runtime.txt, requirements.txt)

### If your code is NOT yet on GitHub:

Before going further, push to GitHub:

```bash
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa

# Sync with remote (resolve any conflicts)
git pull --rebase origin main

# Stage everything
git add -A

# Commit
git commit -m "Production-ready Django setup for Render"

# Push
git push -u origin main
```

If you get a Git error, reply with the error and I'll help fix it. Otherwise, continue below.

---

## STEP 1: Sign Up / Log In to Render

1. Go to https://render.com
2. Click **"Sign up"** (or sign in if you already have an account)
3. Choose **"Continue with GitHub"**
4. Click **"Authorize render-oss"** to allow Render to access your GitHub repos
5. You're now on the Render Dashboard

---

## STEP 2: Create a New Web Service

1. On the Render Dashboard, click **"New +"** (top right)
2. Click **"Web Service"**
3. Click **"Connect Repository"**
   - You'll see a list of your GitHub repos
   - Find and click **"secret-santa"**
   - Click "Connect"

---

## STEP 3: Configure the Web Service

Once your repo is connected, fill in the deployment settings:

### Name

- **Name:** `secret-santa` (or any name you like, e.g., `team-secret-santa`)
- This becomes part of your URL: `https://secret-santa-xxxxx.onrender.com`

### Environment

- **Environment:** Python 3

### Build Command

- Leave as default: `pip install -r requirements.txt`
  (or explicitly copy-paste this)

### Start Command

```
gunicorn secret_santa_config.wsgi
```

(This tells Render how to run your Django app)

### Plan

- Select **Free** (bottom left)

---

## STEP 4: Add Environment Variables

Scroll down to **"Environment Variables"** and add these (Render will provide the database URL automatically):

| Key             | Value                               |
| --------------- | ----------------------------------- |
| `SECRET_KEY`    | Generate a new one (see below)      |
| `DEBUG`         | `False`                             |
| `ALLOWED_HOSTS` | `*` (or your specific domain later) |

### Generate a New SECRET_KEY (recommended for production)

Open a terminal and run:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output (looks like: `k&x%jn9f#z@x2q!r$9v*w+z^a3b&4c5d6e7f8g9h0i1j2k3l4`)

Paste it into the `SECRET_KEY` environment variable in Render.

### About DATABASE_URL

Render automatically provides `DATABASE_URL` after the service is created. You don't need to add it manually—it will be set up for PostgreSQL.

---

## STEP 5: Create the Service

After filling in all fields:

1. Scroll to the bottom
2. Click **"Create Web Service"**
3. Render starts building your app (you'll see a build log stream)
4. Wait for the log to show: ✅ `Build successful`

This takes 2–3 minutes. You'll see:

```
...
Build completed successfully
Deploying...
```

Once deployment finishes, you should see: ✅ `Service is live`

---

## STEP 6: Run Database Migrations

Once the service is live, you need to create the database tables and a superuser:

1. In the Render Dashboard (for your service), scroll down to find **"Shell"** button
2. Click **"Shell"** to open the interactive console
3. Run these commands:

```bash
# Create database tables
python manage.py migrate

# Create a superuser (admin account)
python manage.py createsuperuser
```

When you run `createsuperuser`, it will prompt you:

```
Username: (enter a username, e.g., "admin")
Email address: (enter your email)
Password: (enter a password)
Password (again): (re-enter password)
Superuser created successfully.
```

After running these, exit the shell (`exit` or Ctrl+C).

---

## STEP 7: Populate Initial Data (Optional but Recommended)

Still in the Render Shell:

```bash
# Load your 34 team members
python manage.py populate_participants
```

You should see:

```
Successfully created 34 participants
```

Exit the shell.

---

## STEP 8: Test Your Live App

Get your live URL from Render:

1. Go to your service page on Render Dashboard
2. At the top, you'll see the URL: `https://secret-santa-xxxxx.onrender.com`
3. Copy it

### Test URLs

Open these in your browser:

**Admin Dashboard (manage draws):**

```
https://secret-santa-xxxxx.onrender.com/
```

- Username/Password: credentials you created with `createsuperuser`
- Click "Generate Draw" to create assignments
- Copy tokens for team members

**Participant Page (reveal gift):**

```
https://secret-santa-xxxxx.onrender.com/participant/
```

- Enter a token from the admin dashboard
- Click "Unwrap Gift" to see recipient name
- Confetti animation should play ✨

**Django Admin Panel:**

```
https://secret-santa-xxxxx.onrender.com/admin/
```

- Manage participants and draws
- View past draws and history

---

## STEP 9: Share with Your Team

Send this link to your 34 team members:

```
https://secret-santa-xxxxx.onrender.com/participant/
```

Each person:

1. Opens the link
2. Enters their token (provided by you)
3. Clicks "Unwrap Gift"
4. Sees their Secret Santa recipient name 🎉

---

## Troubleshooting

### Problem: App crashes with "ModuleNotFoundError"

**Solution:**

1. Go to Render Shell
2. Run: `pip install -r requirements.txt`
3. Restart the service: Dashboard → "Restart Service"

### Problem: "No such table: secret_santa_participant"

**Solution:**

1. Go to Render Shell
2. Run: `python manage.py migrate`

### Problem: Static files (CSS/images) not loading

**Solution:**

1. Go to Render Shell
2. Run: `python manage.py collectstatic --noinput`
3. Restart the service

### Problem: "SECRET_KEY" not found

**Solution:**

1. Go back to Render Dashboard
2. Click your service
3. Scroll to "Environment Variables"
4. Make sure `SECRET_KEY` is added with a value
5. Click "Save & Deploy"

### Problem: 500 Server Error

**Solution:**

1. Go to Render Dashboard
2. Click your service
3. Check the "Logs" tab to see what went wrong
4. Look for error messages
5. Fix locally, push to GitHub, Render auto-deploys

### Problem: Database connection error

**Solution:**

1. Render automatically creates `DATABASE_URL` after deployment
2. Go to Render Shell and check: `echo $DATABASE_URL`
3. If empty, your service may not have finished deploying yet
4. Wait a few minutes and try again
5. If still empty, manually set it (Render support can help)

---

## After Deployment

### Auto-Deploy on Push

Every time you push to GitHub, Render auto-deploys:

```bash
# Make a change locally
# ...

git add -A
git commit -m "Update something"
git push
```

Render detects the push and re-deploys in 1–2 minutes. Check the "Logs" tab to see progress.

### Upgrading to Render Pro (Optional)

- Free tier apps sleep after 15 minutes of inactivity (cold start on next visit)
- Render Pro ($7/month) keeps app always running
- For a team of 34 using this occasionally, free tier is fine

### Custom Domain (Optional)

To use your own domain (e.g., `secret-santa.company.com`):

1. In Render Dashboard, go to your service
2. Click "Settings" → "Custom Domain"
3. Follow Render's DNS setup instructions

---

## Checklists

### Pre-Deployment

- [ ] Code pushed to GitHub
- [ ] Procfile exists with: `web: gunicorn secret_santa_config.wsgi`
- [ ] runtime.txt exists with: `python-3.11.7`
- [ ] requirements.txt has Django, gunicorn, psycopg2, whitenoise, dj-database-url
- [ ] SECRET_KEY is strong (generated randomly)
- [ ] DEBUG is set to False in environment

### Post-Deployment

- [ ] Service shows "Live" on Render Dashboard
- [ ] Database migrations ran successfully
- [ ] Superuser created
- [ ] Team members populated (34 people loaded)
- [ ] Admin dashboard loads (`/`)
- [ ] Participant page loads (`/participant/`)
- [ ] Admin login works
- [ ] Generate Draw button works
- [ ] Token reveal works with confetti animation
- [ ] Links shared with team

---

## Quick Reference

| Step      | Time        | Action                            |
| --------- | ----------- | --------------------------------- |
| 1-2       | 1 min       | Sign up to Render, connect GitHub |
| 3         | 2 min       | Configure web service settings    |
| 4         | 1 min       | Add environment variables         |
| 5         | 3 min       | Create service & wait for build   |
| 6         | 2 min       | Run migrations & create superuser |
| 7         | 1 min       | Populate team members             |
| 8         | 2 min       | Test all URLs                     |
| 9         | 1 min       | Share with team                   |
| **Total** | **~15 min** | **Live app!**                     |

---

## Support & Resources

- **Render Docs:** https://render.com/docs
- **Django Deployment:** https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/
- **GitHub Docs:** https://docs.github.com

---

## Summary

After following these steps, you'll have:

✅ A live Django app at `https://secret-santa-xxxxx.onrender.com`  
✅ PostgreSQL database (auto-provided by Render)  
✅ 34 team members pre-loaded  
✅ Admin dashboard to manage draws  
✅ Participant page for team to reveal gifts  
✅ Auto-deployment on every GitHub push  
✅ FREE hosting (Render free tier)

**Cost: $0/month** 💰

**Next:** Follow STEP 1–9 above and your app will be live in ~15 minutes! 🎉
