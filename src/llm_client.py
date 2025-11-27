from textwrap import shorten

# Set to True to run without API (dummy mode)
DUMMY_MODE = True

def call_llm(system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
    if DUMMY_MODE:
        sys_preview = shorten(system_prompt.replace("\n", " "), width=80)
        usr_preview = shorten(user_prompt.replace("\n", " "), width=80)
        return (
            "DUMMY_LLM_RESPONSE\n\n"
            f"[system_prompt_preview]: {sys_preview}\n"
            f"[user_prompt_preview]: {usr_preview}\n\n"
            "Note: DUMMY_MODE is ON. This is not real AI reasoning."
        )

    # -------------------------------------
    # REAL LLM CALL (we will activate later)
    # -------------------------------------
    raise NotImplementedError(
        "DUMMY_MODE is off. Add your real LLM API call in llm_client.py."
    )
