from src.llm_client import call_llm


def analyze_resume(jd_summary: str, resume_text: str) -> str:
    """
    Compare resume with JD summary and return strengths, gaps, and a fit rating.
    """
    system_prompt = (
        "You are a career coach who compares resumes to job descriptions "
        "and explains strengths and weaknesses clearly."
    )

    user_prompt = f"""
Job description summary:
\"\"\"{jd_summary}\"\"\"

Candidate resume:
\"\"\"{resume_text}\"\"\"

1. List strengths (where the resume matches the JD).
2. List gaps (missing or weak areas).
3. Give an overall fit rating out of 10 and one short sentence explaining why.
Format the response with clear headings.
"""

    return "=== RESUME ANALYZER OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
