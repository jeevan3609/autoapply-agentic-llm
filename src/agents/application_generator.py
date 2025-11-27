from src.llm_client import call_llm

def generate_application_materials(resume_text, jd_summary, recs):
    system_prompt = (
        "You write tailored resume bullets and outreach emails."
    )

    user_prompt = (
        "JD Summary:\n"
        f"{jd_summary}\n\nResume:\n{resume_text}\n\nRecommendations:\n{recs}\n\n"
        "Output: 1) 4-8 resume bullet points, 2) Outreach email."
    )

    return "=== APPLICATION MATERIALS OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
