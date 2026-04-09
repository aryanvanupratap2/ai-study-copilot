from langgraph.graph import StateGraph, END
from typing import TypedDict
from llm import llm


# ---- STATE ----
class State(TypedDict):
    input: str
    prompt: str
    raw_output: str
    answer: str
    practice_questions: list


# ---- NODE 1: PREPARE PROMPT ----
def prepare_prompt(state: State):
    prompt = f"""
    You are a helpful college tutor.

    Question:
    {state['input']}

    Explain clearly in simple terms (max 150 words).

    Then generate exactly 3 practice questions.

    Format:

    explanation:
    <text>

    practice:
    1. ...
    2. ...
    3. ...
    """

    state["prompt"] = prompt
    return state


# ---- NODE 2: LLM CALL ----
def call_llm(state: State):
    response = llm.invoke(state["prompt"])
    state["raw_output"] = response.content
    return state


# ---- NODE 3: PARSE OUTPUT ----
def parse_output(state: State):
    text = state["raw_output"]

    parts = text.split("practice:")

    explanation = parts[0].replace("explanation:", "").strip()

    practice = []
    if len(parts) > 1:
        practice = [
            q.strip() for q in parts[1].split("\n") if q.strip()
        ]

    state["answer"] = explanation
    state["practice_questions"] = practice

    return state


# ---- BUILD GRAPH ----
def build_graph():

    builder = StateGraph(State)

    builder.add_node("prepare", prepare_prompt)
    builder.add_node("llm", call_llm)
    builder.add_node("parse", parse_output)

    builder.set_entry_point("prepare")

    builder.add_edge("prepare", "llm")
    builder.add_edge("llm", "parse")
    builder.add_edge("parse", END)

    return builder.compile()


# ---- RUN FUNCTION ----
graph = build_graph()


def run_graph(user_input: str):

    state = {
        "input": user_input,
        "prompt": "",
        "raw_output": "",
        "answer": "",
        "practice_questions": []
    }

    result = graph.invoke(state)
    return result
    
