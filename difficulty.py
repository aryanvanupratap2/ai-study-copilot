from llm import llm

def detect_difficulty(state):
    prompt = f"""
    Classify difficulty: easy / medium / hard

    Only return one word.

    Input: {state['input']}
    """

    state["difficulty"] = llm.invoke(prompt).content.strip().lower()
    return state