from llm import llm

def generate_answer(state):

    prompt = f"""
    You are a helpful college tutor.

    Strategy: {state['strategy']}
    Subject: {state['subject']}
    Topic: {state['topic']}

    Instructions:
    - Be clear and structured
    - Use examples if needed
    - Keep it easy to understand

    Student Question:
    {state['input']}
    """

    state["answer"] = llm.invoke(prompt).content.strip()
    return state