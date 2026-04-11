import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.skills_db import FIELDS, ALL_SKILLS, ALIASES
from app.detector import normalize, apply_aliases, detect_both_fields


def extract_skills(text: str, field_name: str) -> dict:
    """
    Extract skills from text — but ONLY skills relevant to the detected field.

    Why field-specific extraction?
    Yesterday's matcher extracted ALL skills from ALL fields.
    That caused false positives — a marketing resume would
    get credit for "html" just because it appeared once.

    Today we only look for skills that belong to the detected field.
    Much more accurate.

    Example:
    field = "Marketing"
    text = "Managed SEO, Google Ads, HubSpot campaigns"
    → found: {"digital_marketing": ["seo", "google ads"],
               "tools": ["hubspot"]}

    NOT found: python, docker, kubernetes (wrong field)
    """
    text_normalized = apply_aliases(normalize(text))

    # Get skills for this specific field only
    if field_name not in FIELDS:
        # Fall back to all skills if field unknown
        field_skills = {}
        for item in ALL_SKILLS:
            field_skills.setdefault(item["category"], []).append(item["skill"])
    else:
        field_skills = FIELDS[field_name]["skills"]

    found = {}

    # Sort by length — match longer phrases first
    # e.g. "machine learning" before "machine"
    all_field_skills = []
    for category, skills in field_skills.items():
        for skill in skills:
            all_field_skills.append({"skill": skill, "category": category})

    sorted_skills = sorted(
        all_field_skills,
        key=lambda x: len(x["skill"]),
        reverse=True
    )

    for item in sorted_skills:
        skill = item["skill"]
        category = item["category"]

        # Skip single character skills
        if len(skill) <= 1:
            continue

        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text_normalized):
            if skill not in found:
                found[skill] = category

    # Group by category
    by_category = {}
    for skill, category in found.items():
        by_category.setdefault(category, []).append(skill)

    return by_category


def compute_tfidf_similarity(resume: str, job_desc: str) -> float:
    """
    TF-IDF cosine similarity between resume and JD.
    Same as yesterday but with better error handling.
    """
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        min_df=1
    )
    try:
        tfidf_matrix = vectorizer.fit_transform([resume, job_desc])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        return float(similarity[0][0])
    except Exception:
        return 0.0


def generate_tips(
    matched: set,
    missing: set,
    bonus: set,
    field_name: str,
    final_score: float,
    job_flat: set
) -> list:
    """
    Generate field-specific actionable tips.

    This is what makes Universal Job Matcher genuinely useful —
    instead of generic "add missing skills" advice, we give
    tips that are specific to each field.

    Example for Marketing:
    "Google Analytics certification is free and highly valued."

    Example for Finance:
    "CFA or CPA certifications significantly boost your profile."

    Example for Software Engineering:
    "Quantify your impact — 'reduced load time by 40%' beats 'improved performance'."
    """
    tips = []

    # No skills detected in JD
    if len(job_flat) == 0:
        tips.append(
            "No specific skills detected in this job description. "
            "Try pasting the full job description for better results."
        )
        return tips

    # Missing skills tip — field specific
    if missing:
        top_missing = list(missing)[:5]
        tips.append(
            f"Add these missing skills to your resume if you have them: "
            f"{', '.join(top_missing)}"
        )

    # Low score tip
    if final_score < 40:
        tips.append(
            "Your match score is low. Try tailoring your resume to use "
            "the exact keywords from this job description."
        )

    # Matched skills tip
    if len(matched) > 0 and len(job_flat) > 0:
        tips.append(
            f"You match {len(matched)} out of {len(job_flat)} required skills. "
            f"Make sure these are prominently listed on your resume."
        )

    # Bonus skills tip
    if len(bonus) > 3:
        tips.append(
            f"You have {len(bonus)} additional skills beyond what's required. "
            f"These show depth and can help you stand out."
        )

    # Field-specific tips
    if field_name in FIELDS:
        field_tips = FIELDS[field_name]["tips"]
        tips.append(field_tips.get("general", ""))

    return [t for t in tips if t]  # remove empty strings


def match(resume_text: str, job_text: str) -> dict:
    """
    Main matching function — universal version.

    Key differences from yesterday:
    1. Detects field automatically
    2. Extracts skills specific to that field
    3. Generates field-specific tips
    4. Warns if resume and JD fields don't match
    5. Shows field detection results to user

    Flow:
    Resume + JD text
          ↓
    detect_both_fields() → finds fields for both
          ↓
    extract_skills() → field-specific skill extraction
          ↓
    Set comparison → matched / missing / bonus
          ↓
    TF-IDF similarity → contextual score
          ↓
    Weighted final score
          ↓
    generate_tips() → field-specific advice
          ↓
    Return complete result dict
    """

    # ── Step 1: Validate input length ───────────────────────────
    warning = None

    if len(job_text.split()) < 20:
        warning = "Job description is too short. Paste the full JD for accurate results."
        return {
            "final_score": 0.0,
            "skill_score": 0.0,
            "tfidf_score": 0.0,
            "grade": "Incomplete",
            "grade_color": "red",
            "matched_skills": [],
            "missing_skills": [],
            "bonus_skills": [],
            "resume_skills": {},
            "job_skills": {},
            "tips": [warning],
            "total_jd_skills": 0,
            "total_matched": 0,
            "warning": warning,
            "resume_field": "Unknown",
            "job_field": "Unknown",
            "resume_confidence": 0.0,
            "job_confidence": 0.0,
            "fields_match": False,
            "mismatch_warning": None,
        }

    # ── Step 2: Detect fields ────────────────────────────────────
    field_result = detect_both_fields(resume_text, job_text)

    resume_field = field_result["resume_field"]
    job_field = field_result["job_field"]
    primary_field = field_result["primary_field"]
    mismatch_warning = field_result["mismatch_warning"]

    # ── Step 3: Extract skills (field-specific) ──────────────────
    resume_skills = extract_skills(resume_text, primary_field)
    job_skills = extract_skills(job_text, primary_field)

    # Flatten to sets
    resume_flat = set()
    for skills in resume_skills.values():
        resume_flat.update(skills)

    job_flat = set()
    for skills in job_skills.values():
        job_flat.update(skills)

    # ── Step 4: Compare skill sets ───────────────────────────────
    matched = resume_flat & job_flat
    missing = job_flat - resume_flat
    bonus   = resume_flat - job_flat

    # ── Step 5: Calculate scores ─────────────────────────────────
    if len(job_flat) > 0:
        skill_score = len(matched) / len(job_flat) * 100
    else:
        skill_score = 0.0

    tfidf_score = compute_tfidf_similarity(resume_text, job_text) * 100

    # Cap TF-IDF if no skills detected
    if len(job_flat) == 0:
        tfidf_score = tfidf_score * 0.1

    # Weighted final score
    final_score = round((skill_score * 0.7) + (tfidf_score * 0.3), 1)

    # ── Step 6: Grade ────────────────────────────────────────────
    if final_score >= 75:
        grade = "Strong Match"
        grade_color = "green"
    elif final_score >= 50:
        grade = "Good Match"
        grade_color = "blue"
    elif final_score >= 30:
        grade = "Partial Match"
        grade_color = "amber"
    else:
        grade = "Weak Match"
        grade_color = "red"

    # ── Step 7: Generate tips ────────────────────────────────────
    tips = generate_tips(
        matched, missing, bonus,
        primary_field, final_score, job_flat
    )

    # Add mismatch warning at top if exists
    if mismatch_warning:
        tips.insert(0, f"⚠️ {mismatch_warning}")

    # ── Step 8: Return everything ────────────────────────────────
    return {
        "final_score":        final_score,
        "skill_score":        round(skill_score, 1),
        "tfidf_score":        round(tfidf_score, 1),
        "grade":              grade,
        "grade_color":        grade_color,
        "matched_skills":     sorted(list(matched)),
        "missing_skills":     sorted(list(missing)),
        "bonus_skills":       sorted(list(bonus)),
        "resume_skills":      resume_skills,
        "job_skills":         job_skills,
        "tips":               tips,
        "total_jd_skills":    len(job_flat),
        "total_matched":      len(matched),
        "warning":            warning,
        "resume_field":       resume_field,
        "job_field":          job_field,
        "resume_confidence":  field_result["resume_confidence"],
        "job_confidence":     field_result["job_confidence"],
        "fields_match":       field_result["fields_match"],
        "mismatch_warning":   mismatch_warning,
    }