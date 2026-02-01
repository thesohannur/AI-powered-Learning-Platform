"""
Celery worker configuration and tasks.
"""
from celery import Celery
from app.core.config import settings

# Create Celery app
celery_app = Celery(
    "learning_platform",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

# Configure Celery
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
)

# Auto-discover tasks from app.tasks module
celery_app.autodiscover_tasks(['app.tasks'])


# Example task (can be removed later)
@celery_app.task(name="app.worker.test_task")
def test_task(message: str):
    """Simple test task to verify Celery is working."""
    return f"Task completed: {message}"
