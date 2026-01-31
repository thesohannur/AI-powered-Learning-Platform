# Backend - AI-Powered Learning Platform

FastAPI backend for content management, intelligent search, AI generation, and chat.

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL + SQLAlchemy
- **Vector DB:** ChromaDB
- **LLM:** Ollama (Llama 3.1, Mistral, CodeLlama)
- **AI Framework:** LangChain
- **Task Queue:** Celery + Redis

## Project Structure

```
backend/
├── app/
│   ├── api/              # API routes
│   │   ├── routes/       # Endpoint definitions
│   │   └── deps.py       # Dependencies
│   ├── core/             # Core configuration
│   │   ├── config.py     # Settings
│   │   ├── database.py   # DB connection
│   │   └── security.py   # Auth utilities
│   ├── models/           # SQLAlchemy models
│   ├── services/         # Business logic
│   │   ├── cms/          # Content management
│   │   ├── search/       # RAG & search
│   │   ├── generation/   # AI generation
│   │   └── validation/   # Content validation
│   ├── utils/            # Helper functions
│   └── main.py           # App entry point
├── tests/                # Test suite
├── requirements.txt      # Python dependencies
└── .env.example          # Environment template
```

## Setup Instructions

### Prerequisites

- Python 3.10+
- PostgreSQL 15+
- Redis
- Ollama installed locally

### Installation

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment:**
```bash
cp .env.example .env
# Edit .env with your configurations
```

4. **Install Ollama models:**
```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
ollama pull codellama:7b
```

5. **Set up database:**
```bash
# Create PostgreSQL database
createdb learning_platform

# Run migrations (when available)
alembic upgrade head
```

### Running the Server

**Development mode:**
```bash
uvicorn app.main:app --reload --port 8000
```

**Production mode:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

## Development Guidelines

### Code Style
- Follow PEP 8
- Use type hints
- Format with Black
- Lint with Flake8

### Testing
```bash
pytest tests/ -v
```

### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## API Endpoints (Planned)

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/refresh` - Refresh token

### CMS (Phase 1)
- `POST /api/cms/upload` - Upload files
- `GET /api/cms/materials` - List materials
- `PUT /api/cms/materials/{id}` - Update material
- `DELETE /api/cms/materials/{id}` - Delete material

### Search (Phase 2)
- `POST /api/search` - Semantic search
- `GET /api/search/suggestions` - Search suggestions

### Generation (Phase 3)
- `POST /api/generate/notes` - Generate reading notes
- `POST /api/generate/slides` - Generate slides
- `POST /api/generate/code` - Generate code

### Validation (Phase 4)
- `POST /api/validate/code` - Validate code
- `POST /api/validate/content` - Validate theory content

### Chat (Phase 5)
- `POST /api/chat` - Send chat message
- `GET /api/chat/history` - Get chat history
- `WS /api/chat/ws` - WebSocket for streaming

## Environment Variables

See `.env.example` for all available configurations.

## Troubleshooting

**Ollama not connecting:**
```bash
# Check Ollama is running
ollama list

# Restart Ollama service
# macOS: brew services restart ollama
```

**Database connection issues:**
```bash
# Check PostgreSQL is running
pg_isready

# Check connection string in .env
```

## License

See LICENSE file in root directory.
