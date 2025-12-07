from src.llm_client import call_llm


def generate_application_materials(
    jd_summary: str, resume_text: str, analysis_text: str
) -> str:
    """
    Generate tailored resume bullets and an outreach email for this specific JD.
    """
    system_prompt = (
        "You are an expert career writer who creates strong resume bullets and "
        "professional outreach emails tailored to a specific job."
    )

    user_prompt = f"""
Job description summary:
\"\"\"{jd_summary}\"\"\"

Candidate resume:
\"\"\"{resume_text}\"\"\"

Analysis of strengths and gaps:
\"\"\"{analysis_text}\"\"\"

1. Write 5–8 strong, action-impact resume bullet points tailored to this role.
2. Then write a short outreach email to the hiring manager expressing interest
   in the position and highlighting the most relevant skills.

Use clear headings: "Resume Bullet Points" and "Outreach Email".
"""

    return "=== APPLICATION MATERIALS OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
