# Getting Started Guide

## Installation Steps

Follow these steps to set up the AI-Powered Learning Platform.

## Prerequisites Checklist

- [ ] Docker Desktop installed
- [ ] Git installed
- [ ] Ollama installed ([Download here](https://ollama.ai))
- [ ] 16GB+ RAM (recommended)
- [ ] 20GB+ free disk space

## Step-by-Step Setup

### 1. Install Ollama

#### macOS
```bash
brew install ollama
ollama serve
```

#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

#### Windows
Download from https://ollama.ai

### 2. Pull Required Models

```bash
# LLM for generation and chat (4.7GB)
ollama pull llama3.1:8b

# Embedding model for search (274MB)
ollama pull nomic-embed-text

# Code generation model (3.8GB)
ollama pull codellama:7b
```

### 3. Clone and Setup

```bash
# Clone repository
git clone <repository-url>
cd AI-powered-Learning-Platform

# Create environment files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
```

### 4. Start Services with Docker

```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### 5. Verify Installation

Open these URLs:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

### 6. Default Login

**Admin Account:**
- Email: `admin@example.com`
- Password: `admin123`

⚠️ **Change password immediately in production!**

## Troubleshooting

### Ollama Connection Issues

```bash
# Check Ollama is running
ollama list

# Test model
ollama run llama3.1:8b "Hello"
```

### Docker Issues

```bash
# Restart services
docker-compose restart

# Rebuild containers
docker-compose up --build

# View specific service logs
docker-compose logs backend
```

### Database Issues

```bash
# Reset database
docker-compose down -v
docker-compose up -d postgres
```

## Next Steps

1. Read the [PROJECT_ROADMAP.md](../PROJECT_ROADMAP.md)
2. Check [Backend README](../backend/README.md) for API details
3. Check [Frontend README](../frontend/README.md) for UI development

## Development Workflow

```bash
# Start services
docker-compose up -d

# Develop backend (with hot reload)
cd backend
source venv/bin/activate
uvicorn app.main:app --reload

# Develop frontend (with hot reload)
cd frontend
npm run dev

# Run tests
cd backend && pytest
cd frontend && npm test
```

## Production Deployment

See deployment guides in `/docs` folder (coming soon).
