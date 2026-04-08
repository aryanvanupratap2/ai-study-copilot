from llm import llm

def generate_practice(state):

    prompt = f"""
    Generate exactly 3 practice questions.

    Topic: {state['topic']}
    Difficulty: {state['difficulty']}

    Return as:
    1. ...
    2. ...
    3. ...
    """

    response = llm.invoke(prompt).content.strip()

    state["practice_questions"] = [
        q.strip() for q in response.split("\n") if q.strip()
    ]

    return state