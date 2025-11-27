from src.llm_client import call_llm

def parse_job_description(job_text: str) -> str:
    system_prompt = (
        "You extract structured information from job descriptions "
        "and return responsibilities and skills."
    )

    user_prompt = (
        "Job description:\n\n"
        f"{job_text}\n\nSummarize into: Title, Responsibilities, "
        "Required Skills, Nice-to-have Skills."
    )

    return "=== JD PARSER OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
