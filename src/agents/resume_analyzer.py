from src.llm_client import call_llm

def analyze_resume(resume_text: str, jd_summary: str) -> str:
    system_prompt = (
        "You compare resumes with job descriptions and identify strengths and gaps."
    )

    user_prompt = (
        "JD Summary:\n"
        f"{jd_summary}\n\nResume:\n{resume_text}\n\n"
        "List: 1) Strengths, 2) Gaps, 3) Fit rating."
    )

    return "=== RESUME ANALYZER OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
