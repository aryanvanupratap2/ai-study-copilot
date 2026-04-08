from llm import llm

def detect_subject_topic(state):
    prompt = f"""
    Extract:
    Subject and Topic

    Format:
    subject: <subject>
    topic: <topic>

    Input: {state['input']}
    """

    response = llm.invoke(prompt).content.strip().lower()

    try:
        lines = response.split("\n")
        subject = lines[0].split(":")[1].strip()
        topic = lines[1].split(":")[1].strip()
    except:
        subject = "general"
        topic = state["input"]

    state["subject"] = subject
    state["topic"] = topic
    return state