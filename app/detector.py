import re
from app.skills_db import FIELDS, ALIASES


def normalize(text: str) -> str:
    """Clean text for analysis"""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def apply_aliases(text: str) -> str:
    """Replace shorthand with full form"""
    words = text.split()
    result = []
    for word in words:
        result.append(ALIASES.get(word, word))
    return " ".join(result)


def detect_field(text: str) -> tuple:
    """
    Detect which field a document belongs to.

    How it works:
    1. We clean the text
    2. For each field we count how many of its keywords appear
    3. We also count how many of its skills appear
    4. Combined score tells us the field

    Returns:
    - field_name: "Software Engineering", "Marketing" etc.
    - confidence: 0-100% how confident we are
    - all_scores: scores for every field (for debugging)

    Example:
    text = "Python developer with React and AWS experience"
    → field = "Software Engineering"
    → confidence = 92%
    """
    text_normalized = apply_aliases(normalize(text))

    field_scores = {}

    for field_name, field_data in FIELDS.items():
        score = 0

        # Score 1: keyword matches (weighted higher)
        # Keywords are strong signals — "marketing" in a JD
        # almost certainly means it's a marketing role
        keyword_matches = 0
        for keyword in field_data["keywords"]:
            if keyword in text_normalized:
                keyword_matches += 1

        # Each keyword match = 3 points
        score += keyword_matches * 3

        # Score 2: skill matches
        # Skills are supporting evidence
        skill_matches = 0
        for category, skills in field_data["skills"].items():
            for skill in skills:
                if len(skill) <= 1:
                    continue
                pattern = r"\b" + re.escape(skill) + r"\b"
                if re.search(pattern, text_normalized):
                    skill_matches += 1

        # Each skill match = 1 point
        score += skill_matches

        field_scores[field_name] = {
            "score": score,
            "keyword_matches": keyword_matches,
            "skill_matches": skill_matches
        }

    # Find the winning field
    best_field = max(field_scores, key=lambda x: field_scores[x]["score"])
    best_score = field_scores[best_field]["score"]

    # Calculate confidence
    # Max possible score = 10 keywords × 3 + 50 skills × 1 = 80
    # We normalize to 0-100%
    max_possible = 80
    confidence = min(round(best_score / max_possible * 100, 1), 100.0)

    # If score is too low, we're not confident about any field
    if best_score < 3:
        return "General", 0.0, field_scores

    return best_field, confidence, field_scores


def detect_both_fields(resume_text: str, job_text: str) -> dict:
    """
    Detect fields for both resume and job description.

    Why detect both separately?
    Because we want to warn the user if they're applying
    to the wrong field entirely.

    Example:
    Resume field:  "Software Engineering" (85% confident)
    JD field:      "Marketing" (90% confident)
    → Warning: "Your resume appears to be for Software Engineering
                but this job is in Marketing"

    This is genuinely useful — it catches cases where someone
    accidentally pastes the wrong job description.
    """
    resume_field, resume_confidence, resume_scores = detect_field(resume_text)
    job_field, job_confidence, job_scores = detect_field(job_text)

    # Check if fields match
    fields_match = resume_field == job_field

    # Generate field mismatch warning
    mismatch_warning = None
    if not fields_match and resume_confidence > 30 and job_confidence > 30:
        mismatch_warning = (
            f"Your resume appears to be for {resume_field} "
            f"but this job is in {job_field}. "
            f"Make sure you're applying to the right role!"
        )

    return {
        "resume_field": resume_field,
        "resume_confidence": resume_confidence,
        "job_field": job_field,
        "job_confidence": job_confidence,
        "fields_match": fields_match,
        "mismatch_warning": mismatch_warning,
        "primary_field": job_field,  # we match based on what the JD needs
    }