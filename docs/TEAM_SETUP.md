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

---

## 📋 Step 2: Install Ollama

### macOS
```bash
brew install ollama
ollama serve  # Starts service
```

### Windows
1. Download: https://ollama.ai/download/windows
2. Run **OllamaSetup.exe**
3. Verify:
```powershell
ollama --version
```

### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve
```

---

## 📋 Step 3: Install Git, Node.js, Python

### macOS
```bash
brew install git node@18 python@3.11
```

### Windows
1. **Git:** https://git-scm.com/download/win (use defaults)
2. **Node.js:** https://nodejs.org/ (LTS version)
3. **Python:** https://www.python.org/ (**✅ Check "Add to PATH"**)

### Linux
```bash
sudo apt install git nodejs npm python3.11 python3-pip python3-venv
```

---

## 🚀 Step 4: Clone & Setup Project

### All Platforms
```bash
git clone <repository-url>
cd AI-powered-Learning-Platform
```

---

## 🤖 Step 5: Download AI Models (~10GB)

### macOS/Linux
```bash
ollama pull llama3.1:8b        # 4.7GB
ollama pull nomic-embed-text    # 274MB
ollama pull codellama:7b        # 3.8GB
```

### Windows
```powershell
ollama pull llama3.1:8b
ollama pull nomic-embed-text
ollama pull codellama:7b
```

**Verify:**
```bash
ollama list
```

---

## 🐳 Step 6: Start Everything with Docker

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

**Test Ollama:**
```bash
ollama run llama3.1:8b "Hello!"
```

---

## 🛠️ Manual Setup (No Docker)

If you prefer to skip Docker:

### Backend

**macOS/Linux:**
```bash
cd backend
python -m venv venv
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

**macOS/Linux:**
```bash
ollama list
ollama run llama3.1:8b "test"
pkill ollama && ollama serve  # Restart
```

**Windows:**
```powershell
ollama list
ollama run llama3.1:8b "test"
# Restart: System tray → Right-click Ollama → Restart
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

- [ ] Docker Desktop installed
- [ ] Ollama installed
- [ ] Git, Node.js, Python installed
- [ ] Repository cloned
- [ ] Models downloaded (ollama list shows 3 models)
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
