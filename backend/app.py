"""
AI Management Agent - FastAPI Backend
با پشتیبانی از دو زبان فارسی و انگلیسی
"""
import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from config import settings
from services.llm_service import get_llm_service
from services.report_service import ReportService
from models import FinalReport
from exceptions import ManagementAgentError
import database


# ===== Global State =====
report_service: ReportService = None


# ===== Lifespan (Startup/Shutdown) =====
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize services on startup."""
    global report_service
    try:
        database.init_db()
        llm_service = get_llm_service()
        report_service = ReportService(llm_service)
        print(f"✓ Database initialized")
        print(f"✓ LLM Service initialized with model: {settings.llm_model}")
    except Exception as e:
        print(f"✗ Failed to initialize services: {e}")
        raise
    yield


# ===== FastAPI App =====
app = FastAPI(
    title="AI Management Agent API",
    description="Generates comprehensive management reports from Persian or English topics",
    version="2.0.0",
    lifespan=lifespan,
)


# ===== CORS Middleware =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://your-app.vercel.app",  
        "https://your-app.vercel.app/*",
        "https://.*\\.vercel\\.app",  
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===== Request/Response Models =====

class GenerateReportRequest(BaseModel):
    """Request model for generating a management report."""
    topic: str = Field(..., min_length=5, max_length=2000, description="Management topic")
    language: str = Field(
        default="fa",
        pattern="^(fa|en)$",
        description="Output language: 'fa' for Persian, 'en' for English"
    )


class GenerateReportResponse(BaseModel):
    """Response model containing the generated report."""
    final_report: FinalReport
    topic_en: str
    analysis_en: dict
    report_id: str


class UpdateTitleRequest(BaseModel):
    """Request model for updating report title."""
    title: str = Field(..., min_length=1, max_length=200)


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    model: str
    version: str


class DeleteResponse(BaseModel):
    """Delete confirmation response."""
    status: str
    id: str


# ===== Health Check Endpoint =====

@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    """Check if the API is running."""
    return {
        "status": "ok",
        "model": settings.llm_model,
        "version": "2.0.0"
    }


# ===== Report Generation Endpoint =====

@app.post("/api/generate-report", response_model=GenerateReportResponse)
async def generate_report(request: GenerateReportRequest):
    """
    Generate a comprehensive management report.
    
    - Accepts topic in Persian or English
    - Analyzes using 4 management functions (Planning, Organizing, Leading, Controlling)
    - Returns report in the requested language
    - Auto-saves to database
    """
    topic = request.topic.strip()
    language = request.language

    # Validation
    if len(topic) < 5:
        raise HTTPException(
            status_code=400,
            detail="موضوع بسیار کوتاه است. لطفاً توضیحات بیشتری وارد کنید." if language == "fa"
                   else "Topic is too short. Please provide more details."
        )

    if len(topic) > settings.max_input_chars:
        raise HTTPException(
            status_code=400,
            detail=f"طول ورودی بیش از حد مجاز ({settings.max_input_chars} کاراکتر) است." if language == "fa"
                   else f"Input exceeds maximum length ({settings.max_input_chars} characters)."
        )

    try:
        # Generate report with language support
        final_report, topic_en, analysis_json_str, report_id = report_service.generate_report(
            topic=topic,
            language=language
        )
        analysis_en = json.loads(analysis_json_str)

        return GenerateReportResponse(
            final_report=final_report,
            topic_en=topic_en,
            analysis_en=analysis_en,
            report_id=report_id,
        )
    except ManagementAgentError as e:
        error_msg = str(e)
        # Provide bilingual error messages
        if language == "fa":
            raise HTTPException(status_code=502, detail=f"خطا در پردازش: {error_msg}")
        else:
            raise HTTPException(status_code=502, detail=f"Processing error: {error_msg}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        if language == "fa":
            raise HTTPException(status_code=500, detail="خطای غیرمنتظره در سرور.")
        else:
            raise HTTPException(status_code=500, detail="Unexpected server error.")


# ===== Reports CRUD Endpoints =====

@app.get("/api/reports")
async def list_reports():
    """
    Get all saved reports (metadata only).
    Returns list sorted by creation date (newest first).
    """
    try:
        return database.get_all_reports()
    except Exception as e:
        print(f"[ERROR] Failed to list reports: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve reports.")


@app.get("/api/reports/{report_id}")
async def get_report(report_id: str):
    """
    Get a single report by its ID.
    Returns full report data including analysis and final output.
    """
    report = database.get_report(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="گزارش یافت نشد. / Report not found.")
    return report


@app.delete("/api/reports/{report_id}", response_model=DeleteResponse)
async def delete_report_endpoint(report_id: str):
    """
    Delete a report by its ID.
    Returns confirmation with deleted report ID.
    """
    deleted = database.delete_report(report_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="گزارش یافت نشد. / Report not found.")
    return DeleteResponse(status="deleted", id=report_id)


@app.put("/api/reports/{report_id}/title")
async def update_report_title(report_id: str, request: UpdateTitleRequest):
    """
    Update the project title of a saved report.
    Returns the updated report data.
    """
    new_title = request.title.strip()
    if not new_title:
        raise HTTPException(status_code=400, detail="عنوان نمی‌تواند خالی باشد. / Title cannot be empty.")
    
    updated = database.update_report_title(report_id, new_title)
    if not updated:
        raise HTTPException(status_code=404, detail="گزارش یافت نشد. / Report not found.")
    return updated


# ===== Error Handlers =====

@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {"detail": "Endpoint not found"}


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {"detail": "Internal server error"}


# ===== Main Entry Point =====

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("🌊 AI Management Agent - Backend Server")
    print("="*60)
    print(f"📍 Running on: http://127.0.0.1:8000")
    print(f"📚 API Docs:    http://127.0.0.1:8000/docs")
    print(f"🤖 Model:       {settings.llm_model}")
    print("="*60 + "\n")
    
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )