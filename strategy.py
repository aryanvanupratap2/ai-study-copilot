def choose_strategy(state):

    if "assignment" in state["intent"]:
        state["strategy"] = "step_by_step_solution"

    elif "exam" in state["intent"]:
        state["strategy"] = "exam_revision_with_questions"

    elif state["difficulty"] == "hard":
        state["strategy"] = "deep_explanation"

    else:
        state["strategy"] = "simple_explanation"

    return state