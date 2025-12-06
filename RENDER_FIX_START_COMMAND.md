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

### Step 3: Clear the Start Command Field

- Select ALL the text in the **Start Command** field
- Delete it (leave it EMPTY)
- Click **"Save"**

This tells Render: "Use the Procfile instead of this field"

---

## What Happens

1. Render will auto-restart your service
2. Render reads your `Procfile` (which you pushed)
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
CLEAR the field (delete all text)
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
- If it doesn't find a Procfile or misreads it, it sets default Start Command
- When you specify a custom Start Command in UI, it overrides the Procfile
- Solution: Leave Start Command empty, let Procfile control everything

---

## Troubleshooting

**If you still see "ModuleNotFoundError: No module named 'app'" after clearing:**

1. Go to Settings
2. Scroll to "Build Command" and "Start Command"
3. Make sure BOTH are empty (let Procfile control)
4. Click "Save"
5. Render may ask to confirm — click "Restart Service"
6. Wait 3-5 minutes

**If it still fails:**
- Check Logs tab
- Paste the error here
- I'll help debug

---

## Quick Checklist

- [ ] Open Render Dashboard
- [ ] Go to secret-santa service
- [ ] Click Settings tab
- [ ] Find "Start Command" field
- [ ] DELETE all text in it (leave EMPTY)
- [ ] Click "Save"
- [ ] Wait 2-3 min for restart
- [ ] Check Logs for "Service is live"
- [ ] If live, open app URL
- [ ] If error, paste error here

**Do this now and your app should go live!** 🚀
