# Team Setup Guide - Cross-Platform (macOS, Windows, Linux)

Welcome to the team! This guide covers setup for **all operating systems**.

## ⏱️ Setup Time: 30-60 minutes (includes ~10GB model downloads)

---

## 📋 Step 1: Install Docker Desktop

### macOS
```bash
brew install --cask docker
```
OR download: https://www.docker.com/products/docker-desktop/

### Windows 10/11
1. Download from: https://www.docker.com/products/docker-desktop/
2. Run **Docker Desktop Installer.exe**
3. **Enable WSL 2** when prompted
4. Restart computer
5. Open Docker Desktop

**Requirements:**
- Windows 10 Pro/Enterprise/Education (Build 19041+) OR Windows 11
- WSL 2 enabled
- 4GB+ RAM

### Linux
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

**✅ That's it! Ollama, PostgreSQL, Redis, and ChromaDB are all included in Docker.**

---

## 📋 Step 2: Install Git, Node.js, Python (Optional)

**⚠️ Only needed if you want to run frontend/backend manually (without Docker)**

### macOS
```bash
brew install git node@20 python@3.11
```

### Windows
1. **Git:** https://git-scm.com/download/win (use defaults)
2. **Node.js:** https://nodejs.org/ (LTS version 20+)
3. **Python:** https://www.python.org/ (**✅ Check "Add to PATH"**)

### Linux
```bash
sudo apt install git nodejs npm python3.11 python3-pip python3-venv
```

---

## 🚀 Step 3: Clone Project

### All Platforms
```bash
git clone <repository-url>
cd AI-powered-Learning-Platform
```

---

## 🐳 Step 4: Start Everything with Docker

### All Platforms
```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

---

## ✅ Step 7: Verify Setup

**Open these URLs:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

**Test Ollama (after models downloaded):**
```bash
docker exec learning-platform-ollama ollama run llama3.1:8b "Hello!"
```
# Start all services (PostgreSQL, Redis, ChromaDB, Ollama, Backend, Frontend)
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f
```

**This will download and start:**
- PostgreSQL (database)
- Redis (caching)
- ChromaDB (vector database)
- **Ollama (AI models) - 3GB image**
- Backend API
- Frontend

---

## 🤖 Step 5: Download AI Models (~10GB)

**After Docker services start, download AI models:**

### All Platforms
```bash
# Option 1: Use script
./scripts/pull-models.sh

# Option 2: Manual
docker exec learning-platform-ollama ollama pull llama3.1:8b
docker exec learning-platform-ollama ollama pull nomic-embed-text
docker exec learning-platform-ollama ollama pull codellama:7b
```

**Verify models:**
```bash
docker exec learning-platform-ollama ollama list
```

---

## ✅ Step 6: Verify Setup
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

**Windows (PowerShell):**
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

### Frontend (New Terminal)

**All Platforms:**
```bash
cd frontend
npm install
cp .env.example .env.local  # Windows: copy .env.example .env.local
npm run dev
```

---

## 🔧 Troubleshooting

### Ollama Not Working

**All Platforms:**
```bash
# Check if Ollama container is running
docker compose ps

# View Ollama logs
docker compose logs ollama

# Test Ollama
docker exec learning-platform-ollama ollama list

# Restart Ollama
docker compose restart ollama
```

### Port Already in Use

**macOS/Linux:**
```bash
lsof -i :8000  # Find process
kill -9 <PID>
```

**Windows (PowerShell as Admin):**
```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Docker Issues

```bash
docker-compose restart  # Restart services
docker-compose down -v  # Reset (deletes data)
docker-compose logs backend  # View logs
```

### Windows PowerShell Errors

```powershell
# Fix execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Windows WSL 2 Missing

```powershell
# Run as Administrator
wsl --install
wsl --update
```

---

## 💻 Recommended Tools

### VS Code Extensions (All Platforms)
- Python
- Pylance
- ESLint
- Prettier
- Docker
- GitLens
- Tailwind CSS IntelliSense
- WSL (Windows only)

---

## 📚 Daily Workflow

```bash
# 1. Pull latest code
git pull origin main

# 2. Start services
docker-compose up -d

# 3. Code! (hot reload enabled)

# 4. Check logs if needed
docker-compose logs -f backend

# 5. Stop when done
docker-compose down
```

---

## 📊 System Requirements

**Minimum:**
- 8GB RAM
- 25GB free space
- Dual-core CPU

**Recommended:**
- 16GB+ RAM (for smooth Ollama)
- 50GB free space
- Quad-core+ CPU
- GPU (NVIDIA/Apple Silicon helps)

---

## ✅ Setup Checklist
 and running
- [ ] Repository cloned
- [ ] `docker compose up -d` successful
- [ ] All containers running (`docker compose ps`)
- [ ] AI models downloaded (3 models)st shows 3 models)
- [ ] docker-compose up successful
- [ ] Frontend works at localhost:3000
- [ ] Backend API at localhost:8000/api/docs
- [ ] Ollama test successful

---

## 🆘 Need Help?

1. Check Troubleshooting section above
2. Search GitHub Issues
3. Ask in team chat
4. Create new GitHub Issue

---

## 📖 Next Steps

1. Read [PROJECT_ROADMAP.md](../PROJECT_ROADMAP.md)
2. Read [Backend README](../backend/README.md)
3. Read [Frontend README](../frontend/README.md)
4. Pick a task from GitHub Issues
5. Create feature branch: `git checkout -b feature/your-feature`

**Welcome aboard! 🎉**
