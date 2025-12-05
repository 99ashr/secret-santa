# 🔧 Fix: "ModuleNotFoundError: No module named 'app'" on Render

## Problem

Render is trying to run:

```
gunicorn app:app
```

But your Django project doesn't have an `app:app` module. It has `secret_santa_config.wsgi`.

## Solution

### Option 1: Fix in Render Dashboard (Recommended)

1. Go to Render Dashboard → your **"secret-santa"** service
2. Click **"Settings"** (usually at top or side menu)
3. Find **"Start Command"** field
4. **Replace the current command** with:
   ```
   gunicorn secret_santa_config.wsgi:application
   ```
5. Click **"Save"** or **"Deploy"**
6. Render will restart and should work now ✅

### Option 2: Update Procfile (Backup)

If Render still doesn't respect the start command, update your Procfile:

Your current Procfile:

```
web: gunicorn secret_santa_config.wsgi
```

Change it to:

```
web: gunicorn secret_santa_config.wsgi:application --bind 0.0.0.0:$PORT
```

Then:

```bash
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa
git add Procfile
git commit -m "Fix Procfile for Render deployment"
git push
```

Render will auto-deploy the new Procfile.

---

## Why This Happens

- Your Django project is in the `secret_santa_config/wsgi.py` file
- Django creates a `application` object in that file
- Gunicorn needs to know the exact path: `secret_santa_config.wsgi:application`
- Render sometimes auto-detects `app:app` for Flask apps (not Django)
- That's why it's looking for an `app` module that doesn't exist

---

## Quick Fix (Do This Now)

### In Render Dashboard:

1. Go to your service
2. Settings → Start Command
3. Change to: `gunicorn secret_santa_config.wsgi:application`
4. Save & Deploy
5. Wait 2-3 minutes for restart
6. Check Logs tab — should say ✅ "Service is live"

---

## Test After Fix

Open your browser:

```
https://secret-santa-xxxxx.onrender.com/
```

You should see the admin dashboard (no error page).

If you still get an error, the logs will show a different error message (then I can help with that).

---

## Checklist

- [ ] Go to Render Settings
- [ ] Find "Start Command" field
- [ ] Change to: `gunicorn secret_santa_config.wsgi:application`
- [ ] Click Save or Deploy
- [ ] Wait for "Service is live"
- [ ] Open app URL
- [ ] See admin dashboard ✅
