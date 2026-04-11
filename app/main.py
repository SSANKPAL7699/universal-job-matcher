from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.matcher import match
from typing import Optional
import PyPDF2
import io

app = FastAPI(
    title="Universal Job Matcher",
    description="Match your resume against any job description — works for ALL fields, not just tech.",
    version="2.0.0"
)

templates = Jinja2Templates(directory="templates")


def extract_pdf_text(file_bytes: bytes) -> str:
    """
    Extract text from PDF bytes.
    Same as yesterday — PyPDF2 reads page by page.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Could not read PDF: {str(e)}")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the home page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/match", response_class=HTMLResponse)
async def match_form(
    request: Request,
    resume_text: Optional[str] = Form(default=""),
    resume_file: Optional[UploadFile] = File(default=None),
    job_description: Optional[str] = Form(default="")
):
    """
    Handle form submission.

    New in v2.0:
    - Returns field detection results (resume field + JD field)
    - Returns field confidence scores
    - Returns field mismatch warning if needed
    - Field-specific tips in results
    """
    final_resume = ""
    error = None

    # Validate job description
    if not job_description or not job_description.strip():
        error = "Please paste a job description."
    else:
        # Try PDF first
        if resume_file and resume_file.filename and resume_file.filename != "":
            if not resume_file.filename.lower().endswith(".pdf"):
                error = "Please upload a PDF file only."
            else:
                try:
                    file_bytes = await resume_file.read()
                    if file_bytes:
                        final_resume = extract_pdf_text(file_bytes)
                        if not final_resume:
                            error = "Could not read PDF. Try pasting your resume instead."
                    else:
                        error = "Uploaded file is empty."
                except Exception as e:
                    error = str(e)
        elif resume_text and resume_text.strip():
            final_resume = resume_text.strip()
        else:
            error = "Please upload a PDF or paste your resume text."

    if error:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": error,
            "job_description": job_description or ""
        })

    # Run the universal matcher
    result = match(final_resume, job_description)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "resume": final_resume[:500] + "..." if len(final_resume) > 500 else final_resume,
        "job_description": job_description
    })


@app.post("/api/match")
async def match_api(payload: dict):
    """
    JSON API endpoint.

    New in v2.0 — response includes field detection:
    {
        "final_score": 72.3,
        "resume_field": "Software Engineering",
        "job_field": "Software Engineering",
        "resume_confidence": 85.0,
        "job_confidence": 92.0,
        "fields_match": true,
        "matched_skills": [...],
        "missing_skills": [...],
        ...
    }
    """
    resume = payload.get("resume", "")
    job_description = payload.get("job_description", "")
    if not resume or not job_description:
        return {"error": "Both resume and job_description are required"}
    return match(resume, job_description)


@app.get("/fields")
async def get_fields():
    """
    New endpoint — returns all supported fields.
    Useful for developers building on top of our API.

    GET /fields
    Response: ["Software Engineering", "Marketing", "Finance", ...]
    """
    from app.skills_db import FIELDS
    return {
        "fields": list(FIELDS.keys()),
        "total_fields": len(FIELDS),
        "description": "Universal Job Matcher supports all these fields"
    }


@app.get("/health")
async def health():
    return {"status": "ok", "version": "2.0.0"}