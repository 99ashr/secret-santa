# 🔍 Debugging Render Deployment Error

You got: **"Exited with status 1 while running your code"**

This is a generic error. To fix it, we need to see the **full error logs from Render**.

---

## How to Find the Error Details

### In Render Dashboard:

1. Go to your **"secret-santa"** service
2. Click the **"Logs"** tab (at the top)
3. Scroll through the logs and look for:
   - RED text (errors)
   - Lines that say `ERROR`, `Exception`, `Traceback`, or `ModuleNotFoundError`
   - The last few lines before it says "Exited with status 1"

4. **Copy the error message and paste it here**

---

## Common Causes (Try These First)

### Problem 1: Missing Environment Variables

**Error message might say:**
```
KeyError: 'SECRET_KEY'
```

**Fix:**
- Go to your Render service → Environment Variables
- Make sure these are set:
  - `SECRET_KEY` = (your generated string)
  - `DEBUG` = `False`
  - `ALLOWED_HOSTS` = `*`

### Problem 2: Missing Database URL

**Error message might say:**
```
OperationalError: could not connect to server
```

**Fix:**
1. In Render Shell, run:
```bash
echo $DATABASE_URL
```
2. If it's empty, Render hasn't finished setting up PostgreSQL
3. Wait 2-3 minutes and try again
4. Or manually add it:
   - Go to Environment Variables
   - Add: `DATABASE_URL` = `postgresql://...` (Render support will provide)

### Problem 3: Missing Python Packages

**Error message might say:**
```
ModuleNotFoundError: No module named 'django'
```

**Fix:**
1. In Render Shell, run:
```bash
pip install -r requirements.txt
```
2. Restart service: Dashboard → "Restart Service"

### Problem 4: Database Not Migrated

**Error message might say:**
```
no such table: secret_santa_participant
```

**Fix:**
1. In Render Shell, run:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_participants
```

### Problem 5: Static Files Issue

**Error message might say:**
```
ERROR: STATIC_ROOT and STATIC_URL are misconfigured
```

**Fix:**
1. In Render Shell, run:
```bash
python manage.py collectstatic --noinput
```
2. Restart service

---

## Quick Diagnostics (Run These in Render Shell)

1. Check Python version:
```bash
python --version
```
Should show: `Python 3.11.x`

2. Check if Django is installed:
```bash
python -m django --version
```
Should show: `6.0`

3. Check if all packages are installed:
```bash
pip list | grep -i django
pip list | grep -i gunicorn
pip list | grep -i psycopg2
```

4. Check environment variables are set:
```bash
echo "SECRET_KEY: $SECRET_KEY"
echo "DEBUG: $DEBUG"
echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "DATABASE_URL: $DATABASE_URL"
```

5. Try running Django directly:
```bash
python manage.py check
```
Should show: `System check identified no issues (0 silenced).`

---

## How to Access Render Shell

1. Render Dashboard → your service → scroll down
2. Look for **"Shell"** or **"Console"** button
3. Click it
4. You'll get a terminal where you can run commands

---

## Next Steps

**Please:**

1. Open Render Logs tab
2. Find the RED error text
3. **Copy the full error and paste it here**
4. Or run the diagnostics above and share the output

Then I can give you the exact fix! 

---

## Common Error Examples

**If you see this:**
```
SECRET_KEY is not set
```
→ You forgot to add `SECRET_KEY` environment variable

**If you see this:**
```
OperationalError at /
could not connect to server: Name or service not known
```
→ Database isn't set up yet (wait or check DATABASE_URL)

**If you see this:**
```
ModuleNotFoundError: No module named 'whitenoise'
```
→ Run: `pip install -r requirements.txt` in Render Shell

**If you see this:**
```
ERROR: DATABASES configuration is invalid
```
→ DATABASE_URL isn't set; wait for Render to provision PostgreSQL

---

**The faster you share the exact error, the faster I can fix it!** 🚀
