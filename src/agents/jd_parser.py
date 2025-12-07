from src.llm_client import call_llm


def parse_job_description(job_text: str) -> str:
    """
    Ask the LLM to extract a structured summary of the job description.
    """
    system_prompt = (
        "You are a helpful assistant that extracts structured information from "
        "job descriptions for data/analytics roles."
    )

    user_prompt = f"""
Read the following job description and summarize it in a structured way.

Return sections with:
- Job Title
- Responsibilities (bulleted)
- Required Skills (bulleted)
- Nice-to-Have Skills (bulleted)

Job description:
\"\"\"{job_text}\"\"\"
"""

    return "=== JD PARSER OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
