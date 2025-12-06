# 🔧 Fix Render Start Command Override

## The Problem

Render is running: `gunicorn app:app` (WRONG)  
But your Procfile says: `gunicorn secret_santa_config.wsgi:application` (RIGHT)

**Reason:** Render's Settings UI has a **Start Command** field that overrides your Procfile.

---

## The Solution (3 Steps)

### Step 1: Go to Render Dashboard

Open: https://dashboard.render.com

Find your **secret-santa** service.

### Step 2: Go to Settings

Click **"Settings"** at the top of your service page.

Scroll down to find **"Start Command"** field.

### Step 3: Set the Correct Start Command

- Select ALL the text in the **Start Command** field
- **Replace it with:**
  ```
  gunicorn secret_santa_config.wsgi:application --bind 0.0.0.0:$PORT
  ```
- Click **"Save"**

This tells Render to run your Django WSGI application correctly.

---

## What Happens

1. Render will auto-restart your service
2. Render uses your **Start Command** field (now pointing to correct WSGI)
3. Render runs: `gunicorn secret_santa_config.wsgi:application --bind 0.0.0.0:$PORT` ✅
4. Your app starts successfully!

---

## Visual Steps

**In Render Dashboard:**

```
Service: secret-santa
  ↓
Click "Settings" tab
  ↓
Scroll to "Start Command" field
  ↓
REPLACE text with: gunicorn secret_santa_config.wsgi:application --bind 0.0.0.0:$PORT
  ↓
Click "Save" button
  ↓
Wait 2-3 min for restart
  ↓
Check Logs for "Service is live" ✅
```

---

## After It Works

1. Open: `https://secret-santa-xxxxx.onrender.com/`
2. You should see the admin dashboard (no error)
3. Then you can:
   - Set environment variables (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
   - Restart service once more
   - Test the app

---

## Why This Happens

- Render tries to auto-detect your app type (Flask, Django, etc.)
- It mistakenly guesses `gunicorn app:app` (Flask format) instead of Django
- The **Start Command field in the UI overrides your Procfile**
- Solution: Set Start Command to the correct Django WSGI path

---

## Troubleshooting

**If you still see "ModuleNotFoundError: No module named 'app'" after setting Start Command:**

1. Go to Settings
2. Check "Start Command" field — make sure it says:
   ```
   gunicorn secret_santa_config.wsgi:application --bind 0.0.0.0:$PORT
   ```
3. If it's different, replace it with the above
4. Click "Save"
5. Render restarts automatically
6. Wait 3-5 minutes

**If it still fails:**

- Check Logs tab for new error message
- Paste the error here
- I'll help debug

---

## Quick Checklist

- [ ] Open Render Dashboard
- [ ] Go to secret-santa service
- [ ] Click Settings tab
- [ ] Find "Start Command" field
- [ ] Replace with: `gunicorn secret_santa_config.wsgi:application --bind 0.0.0.0:$PORT`
- [ ] Click "Save"
- [ ] Wait 2-3 min for restart
- [ ] Check Logs for "Service is live"
- [ ] If live, open app URL: `https://secret-santa-xxxxx.onrender.com/`
- [ ] If error, paste error here

**Do this now and your app should go live!** 🚀
