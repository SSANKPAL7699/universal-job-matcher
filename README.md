# Universal Job Matcher

Match your resume against any job description — works for ALL fields, not just tech.

## Live Demo
👉 [Coming soon after deployment]

## Supported Fields
- Software Engineering
- Data Science & Analytics
- Marketing
- Finance
- Design
- Sales
- Healthcare
- Operations
- Legal
- Human Resources

## What makes it different
- **Field auto-detection** — automatically detects what field your resume and JD belong to
- **Field mismatch warning** — alerts you if you're applying to the wrong field
- **Field-specific tips** — advice tailored to your industry, not generic suggestions
- **300+ skills** across 10 fields
- **Free & open source** — no signup, no paywall, no credit card

## Tech Stack
Python · FastAPI · scikit-learn (TF-IDF) · Docker · GitHub Actions

## Run Locally
```bash
docker-compose up --build
```
Open http://localhost:8000

## API Usage
```bash
# Match resume to job description
curl -X POST https://your-url/api/match \
  -H "Content-Type: application/json" \
  -d '{"resume": "Python developer...", "job_description": "Looking for..."}'

# Get all supported fields
curl https://your-url/fields
```

## Author
Shreya Sankpal · [LinkedIn](https://linkedin.com/in/shreya-sankpal) · [GitHub](https://github.com/SSANKPAL7699)