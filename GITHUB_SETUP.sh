#!/bin/bash

# 🎄 Secret Santa - Quick GitHub Setup Script

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║   🎄 SECRET SANTA - GITHUB SETUP 🎄                           ║"
echo "║                                                                ║"
echo "║         Push Your Project to GitHub (2 minutes)                ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install it first."
    echo "   For macOS: brew install git"
    exit 1
fi

echo "📍 Current directory: $(pwd)"
echo ""

# Step 1: Configure Git
echo "Step 1️⃣  Configure Git Locally"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Enter your name:"
read GIT_NAME
echo ""
echo "Enter your email:"
read GIT_EMAIL
echo ""

git config --global user.name "$GIT_NAME"
git config --global user.email "$GIT_EMAIL"

echo "✅ Git configured with:"
echo "   Name: $GIT_NAME"
echo "   Email: $GIT_EMAIL"
echo ""

# Step 2: Initialize Git Repository
echo "Step 2️⃣  Initialize Git Repository"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ -d ".git" ]; then
    echo "✅ Git repository already initialized"
else
    git init
    echo "✅ Git repository initialized"
fi

echo ""

# Step 3: Add Files
echo "Step 3️⃣  Add All Files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

git add .
echo "✅ All files added"
echo ""

# Step 4: Create Initial Commit
echo "Step 4️⃣  Create Initial Commit"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

git commit -m "Secret Santa Django App - Ready for deployment"
echo "✅ Commit created"
echo ""

# Step 5: Instructions for GitHub
echo "Step 5️⃣  Create Repository on GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Next, go to GitHub.com and:"
echo "  1. Sign in to your account (create one if needed)"
echo "  2. Click '+' → 'New repository'"
echo "  3. Name it: secret-santa"
echo "  4. Add description: Secret Santa Draw Application"
echo "  5. Click 'Create repository'"
echo ""
echo "Then come back here and enter your GitHub username:"
read GITHUB_USER
echo ""

# Step 6: Add Remote and Push
echo "Step 6️⃣  Push to GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

REPO_URL="https://github.com/$GITHUB_USER/secret-santa.git"

git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"
git branch -M main
git push -u origin main

echo ""
echo "✅ Successfully pushed to GitHub!"
echo ""

# Step 7: Next Steps
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 NEXT STEP: Deploy on Render"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Your repository is now at:"
echo "   $REPO_URL"
echo ""
echo "Now deploy on Render:"
echo "  1. Go to https://render.com"
echo "  2. Sign up with GitHub"
echo "  3. Click 'New +' → 'Web Service'"
echo "  4. Select your secret-santa repository"
echo "  5. Follow the deployment guide in FREE_HOSTING_GUIDE.md"
echo ""
echo "🎄 Your app will be live in 5 minutes! 🎄"
echo ""
