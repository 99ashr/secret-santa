# 📤 How to Upload Your Project to GitHub

## Option 1: Using Command Line (Fastest & Easiest) ⭐

### Step 1: Create GitHub Account (if you don't have one)

1. Go to https://github.com
2. Click "Sign up"
3. Enter your email
4. Create a password
5. Choose a username
6. Click "Create account"
7. Verify your email

### Step 2: Create a New Repository on GitHub

1. Go to https://github.com (logged in)
2. Click the **+** icon (top right)
3. Click "New repository"
4. Fill in:
   - **Repository name**: `secret-santa`
   - **Description**: `Secret Santa Draw Application`
   - **Public**: (leave checked)
   - Do NOT check "Initialize with README"
5. Click "Create repository"

### Step 3: Upload Your Entire Folder to GitHub

**Option A: Automatic Script (Easiest)**

```bash
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa
bash GITHUB_SETUP.sh
```

This script will:

- Configure Git
- Add all files
- Commit them
- Push to GitHub automatically
- Done! ✅

**Option B: Manual Commands**

Run these commands in your terminal:

```bash
# Navigate to your project
cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa

# Configure Git (first time only)
git config --global user.name "Your Full Name"
git config --global user.email "your.email@gmail.com"

# Initialize git repository
git init

# Add all files (the entire folder!)
git add .

# Create a commit
git commit -m "Secret Santa Django App - Ready for Render deployment"

# Get your repo URL from GitHub and run:
# (Replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git

# Set main branch
git branch -M main

# Upload everything to GitHub
git push -u origin main
```

---

## Option 2: Using GitHub Desktop (Visual Way)

If you prefer clicking instead of typing:

### Step 1: Install GitHub Desktop

1. Go to https://desktop.github.com
2. Download GitHub Desktop
3. Install it
4. Launch it

### Step 2: Add Your Folder

1. Click "File" → "Add Local Repository"
2. Navigate to: `/Users/ashr/Documents/MaProjects/Christmas Secret Santa`
3. Click "Add Repository"

### Step 3: Commit Your Files

1. In GitHub Desktop, you'll see all your files listed
2. Click on the checkbox next to each folder/file (or "Select All")
3. At the bottom, enter commit message: `Secret Santa Django App`
4. Click "Commit to main"

### Step 4: Publish to GitHub

1. Click "Publish repository" (top right)
2. Name: `secret-santa`
3. Check "Keep this code private" (optional)
4. Click "Publish Repository"
5. Done! ✅

---

## Option 3: Drag & Drop (Simplest)

### Step 1: Create Repo on GitHub (as above)

### Step 2: Use GitHub's Web Upload

1. Go to your new repository: `https://github.com/YOUR_USERNAME/secret-santa`
2. Click "Add file" → "Upload files"
3. Drag and drop your entire project folder
4. Click "Commit changes"

**Note:** This uploads files but folders are flattened. Not ideal for your project structure.

---

## 🎯 What Gets Uploaded

When you upload your project, GitHub will receive:

```
secret-santa/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── db.sqlite3                    ← Database file
├── .gitignore                    ← Ignores unnecessary files
├── README.md
├── DEPLOY_NOW.md
├── HOW_TO_USE.md
├── FREE_HOSTING_GUIDE.md
├── DEPLOYMENT_CHECKLIST.md
├── GITHUB_SETUP.sh
│
├── secret_santa_config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
│
├── secret_santa/                 ← Your main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── populate_participants.py
│   └── __pycache__/ (ignored)
│
├── templates/
│   └── secret_santa/
│       ├── admin.html
│       └── participant.html
│
├── static/                       ← Empty (for CSS/JS)
│
└── venv/                         ← NOT uploaded (ignored by .gitignore)
```

✅ **All important files uploaded**
❌ **venv folder NOT uploaded** (good - Render will create its own)
❌ ****pycache** NOT uploaded** (good - auto-generated)

---

## 📋 Step-by-Step Summary

### Quick Start (3 steps):

1. **Create GitHub Repo**

   - https://github.com/new
   - Name: `secret-santa`
   - Click "Create"

2. **Copy Your Repo URL**

   - From GitHub, copy the HTTPS URL (looks like: `https://github.com/YOUR_USERNAME/secret-santa.git`)

3. **Run Upload Commands**
   ```bash
   cd /Users/ashr/Documents/MaProjects/Christmas\ Secret\ Santa
   git config --global user.name "Your Name"
   git config --global user.email "your@email.com"
   git init
   git add .
   git commit -m "Secret Santa App"
   git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git
   git branch -M main
   git push -u origin main
   ```

---

## ✅ Verify Upload Success

After running the commands:

1. Go to https://github.com/YOUR_USERNAME/secret-santa
2. You should see:
   - ✅ All your files listed
   - ✅ Folders like `secret_santa/`, `templates/`, etc.
   - ✅ Files like `manage.py`, `requirements.txt`, etc.
   - ✅ Green checkmark showing successful push

---

## 🚀 After Uploading to GitHub

Once your code is on GitHub:

1. Go to https://render.com
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Click "Connect Repository"
5. Select your `secret-santa` repo
6. Render will auto-deploy! ✅

---

## ❓ Common Questions

**Q: Will my entire folder be uploaded?**
A: Yes! All files and subfolders (except those in .gitignore)

**Q: Is my venv folder uploaded?**
A: No, .gitignore excludes it. Render creates its own. ✅

**Q: Is my database file uploaded?**
A: Yes, but Render will create a new PostgreSQL database

**Q: Can I upload it without GitHub?**
A: Not really - Render specifically asks for GitHub for auto-deployment

**Q: Do I need to upload the venv folder?**
A: No! Keep it local only. Render will install dependencies from requirements.txt

**Q: What if I make changes locally?**
A: Just push to GitHub again and Render auto-deploys!

```bash
git add .
git commit -m "Updated participants"
git push
```

---

## 🎓 Understanding Git

**What is Git?**

- A tool to track changes to your code
- Allows collaboration
- Required for Render deployment

**What is GitHub?**

- A website that hosts your Git repositories
- Cloud storage for your code
- Free to use

**Workflow:**

1. Make changes locally
2. Add files: `git add .`
3. Commit: `git commit -m "message"`
4. Push: `git push` (uploads to GitHub)
5. Render auto-deploys!

---

## 🎯 Next Steps

1. **Create GitHub account** (if needed) - 2 minutes
2. **Create repository** - 1 minute
3. **Upload your project** - 1 minute
4. **Deploy on Render** - 5 minutes

**Total: ~9 minutes to live app! 🚀**

---

## 📞 Troubleshooting

**Error: "fatal: not a git repository"**

- Solution: Run `git init` first

**Error: "fatal: 'origin' does not appear to be a 'git' repository"**

- Solution: Run `git remote add origin https://github.com/YOUR_USERNAME/secret-santa.git`

**Error: "Permission denied (publickey)"**

- Solution: Set up SSH keys (easier: use HTTPS instead)

**Nothing appears in GitHub**

- Check: Did you get a success message after `git push`?
- Try: Wait 30 seconds and refresh GitHub

**Too many files?**

- Don't worry! All files should go up
- Check that .gitignore is properly set

---

**Ready to upload? Start with creating your GitHub account!** 🎉
