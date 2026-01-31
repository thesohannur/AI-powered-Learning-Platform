"""
Main FastAPI application entry point.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# Create FastAPI app
app = FastAPI(
    title="AI-Powered Learning Platform API",
    description="Backend API for intelligent course content management and generation",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "message": "AI-Powered Learning Platform API",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Import and include routers (will be added in Phase 1)
# from app.api.routes import auth, cms, search, generation, chat
# app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
# app.include_router(cms.router, prefix="/api/cms", tags=["cms"])
# app.include_router(search.router, prefix="/api/search", tags=["search"])
# app.include_router(generation.router, prefix="/api/generate", tags=["generation"])
# app.include_router(chat.router, prefix="/api/chat", tags=["chat"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
