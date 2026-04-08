from langgraph.graph import StateGraph, END

from intent import detect_intent
from topic import detect_subject_topic
from difficulty import detect_difficulty
from answer import generate_answer
from practice import generate_practice

# router function
def route_by_intent(state):
    intent = state["intent"]

    if "assignment" in intent:
        return "solve"

    elif "exam" in intent:
        return "exam"

    else:
        return "explain"


# conditional nodes

def explain_node(state):
    state["strategy"] = "simple_explanation"
    return generate_answer(state)


def solve_node(state):
    state["strategy"] = "step_by_step_solution"
    return generate_answer(state)


def exam_node(state):
    state["strategy"] = "exam_revision"
    state = generate_answer(state)
    state = generate_practice(state)
    return state


# graph building

def build_graph():

    builder = StateGraph(dict)

    # add nodes
    builder.add_node("intent", detect_intent)
    builder.add_node("topic", detect_subject_topic)
    builder.add_node("difficulty", detect_difficulty)

    builder.add_node("explain", explain_node)
    builder.add_node("solve", solve_node)
    builder.add_node("exam", exam_node)

    builder.add_node("practice", generate_practice)

    # entry
    builder.set_entry_point("intent")

    # linear part
    builder.add_edge("intent", "topic")
    builder.add_edge("topic", "difficulty")

    # conditional routing
    builder.add_conditional_edges(
        "difficulty",
        route_by_intent,
        {
            "explain": "explain",
            "solve": "solve",
            "exam": "exam"
        }
    )

    # after explain/solve → practice
    builder.add_edge("explain", "practice")
    builder.add_edge("solve", "practice")

    # exam already includes practice → go to END
    builder.add_edge("exam", END)

    builder.add_edge("practice", END)

    return builder.compile()


# running the function

graph = build_graph()

def run_graph(user_input: str):

    state = {
        "input": user_input,
        "intent": "",
        "subject": "",
        "topic": "",
        "difficulty": "",
        "strategy": "",
        "answer": "",
        "practice_questions": []
    }

    result = graph.invoke(state)
    return result
