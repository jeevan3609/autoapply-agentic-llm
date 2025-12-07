from src.llm_client import call_llm


def recommend_gaps(analysis_text: str) -> str:
    """
    Take the resume analysis and suggest what to emphasize now and
    what to improve in the future.
    """
    system_prompt = (
        "You are a practical mentor who turns a resume-vs-JD analysis into "
        "concrete recommendations."
    )

    user_prompt = f"""
Here is an analysis comparing a resume to a job description:

\"\"\"{analysis_text}\"\"\"

Write two sections:

1. "What to Emphasize Now" – bullet points the candidate should highlight
   in their current resume for this job.
2. "Future Improvements" – bullet points with skills, tools, or experiences
   the candidate should work on over the next 6–12 months.

Be specific and concise.
"""

    return "=== GAP RECOMMENDER OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
