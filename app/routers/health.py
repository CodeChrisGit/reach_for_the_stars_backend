import os
import psycopg2
from fastapi import APIRouter, Response, status
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/v1", tags=["Health"])

def check_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME", "reach_for_the_stars_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres"),
            connect_timeout=3
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        cursor.close()
        conn.close()
        return True
    except Exception:
        return False

@router.get("/health")
def health_check(response: Response):
    if check_db():
        return {"status": "ok", "database": "ok"}
    else:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"error": {"code": "DATABASE_DOWN", "message": "Database connection failed."}}