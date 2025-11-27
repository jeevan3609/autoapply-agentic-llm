from src.llm_client import call_llm

def recommend_improvements(analysis_text: str) -> str:
    system_prompt = (
        "You suggest resume improvements based on strengths and gaps."
    )

    user_prompt = (
        "Analysis:\n"
        f"{analysis_text}\n\n"
        "Provide: 1) What to emphasize now, 2) Future improvements."
    )

    return "=== GAP RECOMMENDER OUTPUT ===\n" + call_llm(system_prompt, user_prompt)
