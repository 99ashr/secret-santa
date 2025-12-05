# 🎄 Secret Santa - Complete Deployment Guide

## 📋 Table of Contents

1. [Quick Summary](#quick-summary)
2. [Free Hosting Options](#free-hosting-options)
3. [Step-by-Step Render Deployment](#step-by-step-render-deployment)
4. [GitHub Setup](#github-setup)
5. [After Deployment](#after-deployment)

---

## Quick Summary

Your Secret Santa app is **ready to deploy for FREE** in 5 minutes!

**What you have:**

- ✅ Complete Django application
- ✅ Database ready
- ✅ API endpoints working
- ✅ Beautiful UI
- ✅ 34 team members configured

**What you need:**

- GitHub account (free)
- Render account (free)
- 5 minutes of your time

---

## Free Hosting Options

| Platform           | Cost  | Setup Time | Database   | Always On     | Best For        |
| ------------------ | ----- | ---------- | ---------- | ------------- | --------------- |
| **Render** ⭐      | Free  | 5 min      | PostgreSQL | ❌ Spins down | Teams up to 100 |
| **Railway**        | $5/mo | 5 min      | PostgreSQL | ✅ Yes        | More usage      |
| **PythonAnywhere** | Free  | 10 min     | Limited    | ❌ Limited    | Learning        |
| **Fly.io**         | Free  | 10 min     | PostgreSQL | ⚠️ Limited    | Advanced        |

**Recommendation: Use Render** - Best balance of free tier, ease of use, and performance.

---

## Step-by-Step Render Deployment

### Phase 1: Prepare Your Code (Already Done ✅)

We already created these files:

- ✅ `Procfile` - tells Render how to run your app
- ✅ `runtime.txt` - Python version
- ✅ `requirements.txt` - updated with production dependencies
- ✅ `.gitignore` - excludes unnecessary files

### Phase 2: Push to GitHub (5 minutes)

**Option A: Use the automated script**

```bash
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa
bash GITHUB_SETUP.sh
```

**Option B: Manual setup**

```bash
# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"

# Initialize and commit
git init
git add .
git commit -m "Secret Santa - Ready for deployment"

# Create repo on github.com first, then:
git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git
git branch -M main
git push -u origin main
```

### Phase 3: Deploy on Render (2 minutes)

1. **Create Render Account**

   - Go to https://render.com
   - Click "Sign up"
   - Select "Sign up with GitHub"
   - Authorize Render to access GitHub

2. **Create Web Service**

   - Click "New +" button (top right)
   - Select "Web Service"
   - Click "Connect Repository"
   - Select your `secret-santa` repo
   - Click "Connect"

3. **Configure Deployment**

   - **Name**: `secret-santa`
   - **Environment**: `Python 3`
   - **Build Command**:
     ```
     pip install -r requirements.txt && python manage.py migrate && python manage.py populate_participants && python manage.py collectstatic --noinput
     ```
   - **Start Command**:
     ```
     gunicorn secret_santa_config.wsgi
     ```
   - Click "Create Web Service"

4. **Wait for Deployment**
   - Render deploys automatically (2-3 minutes)
   - You'll see deployment logs
   - When done, you get a URL like: `https://secret-santa-xxxxx.onrender.com`

### Phase 4: Create Admin User (1 minute)

1. Go to your Render dashboard
2. Click on your `secret-santa` service
3. Go to "Shell" tab
4. Run this command:
   ```bash
   python manage.py createsuperuser
   ```
5. Follow prompts:
   - Username: `admin`
   - Email: `your@email.com`
   - Password: (enter twice)

### Phase 5: Test Your App

Visit these URLs:

- Admin Dashboard: `https://your-app.onrender.com/`
- Participant Reveal: `https://your-app.onrender.com/participant/`
- Django Admin: `https://your-app.onrender.com/admin/`

**Test workflow:**

1. Go to admin dashboard
2. Click "Generate Secret Santa Draw"
3. See success message
4. Click "Show Tokens"
5. Copy any token
6. Go to participant page
7. Paste token and click "Reveal"
8. See confetti celebration! 🎉

---

## GitHub Setup

### Create GitHub Account (if needed)

1. Go to https://github.com
2. Click "Sign up"
3. Enter email, password, username
4. Verify your email
5. Done!

### Push Your Code

**Method 1: Command Line (Fastest)**

```bash
# Navigate to project
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa

# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"

# Initialize repo
git init

# Add all files
git add .

# Create commit
git commit -m "Secret Santa Django App"

# Create new repository on github.com first!
# Name it: secret-santa
# Then get the URL and run:

git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git
git branch -M main
git push -u origin main
```

**Method 2: GitHub Desktop (Easiest Visual Way)**

1. Download GitHub Desktop (github.com/desktop)
2. Open your project folder
3. Click "Publish repository"
4. Sign in with your GitHub account
5. Done! Your code is pushed

---

## After Deployment

### Share with Your Team

Send them this link:

```
https://your-app.onrender.com/participant/
```

### How Team Members Use It

1. Open the link
2. Enter their 6-character token
3. Click the gift box
4. See their recipient name
5. Celebrate! 🎉

### Update Participants (Future Years)

1. Login to `/admin/` on your live app
2. Go to "Participants" section
3. Edit/add/delete as needed
4. No need to redeploy!

### Monitor Your App

- **Render Dashboard**: See traffic, logs, errors
- **View Logs**: Click on service → "Logs"
- **View Deployments**: Click on service → "Deployments"

### Custom Domain (Optional)

Want `secretsanta.com` instead of `secret-santa-xxxxx.onrender.com`?

1. Buy domain on GoDaddy, Namecheap, etc. (~$12/year)
2. Get CNAME target from Render
3. Update DNS settings on your domain registrar
4. Wait 24 hours for propagation
5. Done!

---

## Troubleshooting

### ❌ "Build failed"

- Check build logs in Render dashboard
- Make sure `requirements.txt` has all dependencies
- Verify `Procfile` and `runtime.txt` exist

### ❌ "Database error"

- Check if migrations ran: look at build logs
- Render automatically creates PostgreSQL
- Try re-deploying from "Deployments" tab

### ❌ "Can't create superuser"

- Go to Render dashboard → Shell
- Run: `python manage.py createsuperuser`
- Follow prompts

### ❌ "Static files not loading"

- Already handled by `collectstatic` command
- Check if CSS/JS load in browser
- View source to see what URLs it's trying

### ❌ "Participants not showing"

- Go to Shell and run: `python manage.py shell`
- Type: `from secret_santa.models import Participant; print(Participant.objects.count())`
- Should show 34
- If not, run: `python manage.py populate_participants`

---

## Cost Breakdown

| Service                     | Price                 |
| --------------------------- | --------------------- |
| **Render free tier**        | $0                    |
| **Domain** (optional)       | $12/year              |
| **Custom email** (optional) | $0 (Gmail) or $6/year |
| **Total**                   | **$0 - $12/year**     |

### Optional Upgrades (if you need better performance)

| Service      | Price       | Benefits                        |
| ------------ | ----------- | ------------------------------- |
| Render Pro   | $7/month    | Always running (no cold starts) |
| Railway paid | $5-20/month | Higher usage limits             |
| Heroku Eco   | $7/month    | Industry standard               |

---

## Security Notes

✅ **Already configured:**

- HTTPS/SSL (automatic on Render)
- Environment variables for secrets
- CSRF protection
- SQL injection prevention
- Password hashing for admin

✅ **Production settings:**

- DEBUG = False (no sensitive errors shown)
- ALLOWED_HOSTS configured
- Secure cookies enabled

---

## Performance Notes

**Free tier performance:**

- Response time: 200-500ms
- Concurrent users: Easily handles 34 people
- Requests per second: 10+ (plenty for your team)
- Cold starts: ~30 seconds after 15 min inactivity

**Is it fast enough?** YES! Perfect for internal team use.

---

## Next Steps Checklist

- [ ] Read this guide completely
- [ ] Create GitHub account (if needed)
- [ ] Push code to GitHub
- [ ] Create Render account
- [ ] Deploy on Render
- [ ] Create superuser account
- [ ] Generate test draw
- [ ] Test participant reveal
- [ ] Share link with team
- [ ] Celebrate! 🎉

---

## Quick Links

- **Render**: https://render.com
- **GitHub**: https://github.com
- **Django Docs**: https://docs.djangoproject.com/
- **Render Docs**: https://render.com/docs

---

## Support

Need help?

1. **Read docs first**: FREE_HOSTING_GUIDE.md, DEPLOYMENT_CHECKLIST.md
2. **Check Render logs**: Your app dashboard → Logs
3. **Common issues**: See "Troubleshooting" above
4. **Render support**: https://render.com/support

---

**You've got this! Your Secret Santa app will be live soon! 🎄✨**

Questions? Don't hesitate to reach out!
