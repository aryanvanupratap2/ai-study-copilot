from llm import llm

def detect_intent(state):
    prompt = f"""
    Classify the student's intent into ONE of:
    - concept_doubt
    - assignment_problem
    - exam_preparation
    - revision

    Only return the label.

    Input: {state['input']}
    """

    state["intent"] = llm.invoke(prompt).content.strip().lower()
    return state