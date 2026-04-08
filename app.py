import streamlit as st
import requests

st.title("🎓 AI Study Copilot (Gemini Powered)")

user_input = st.text_input("Ask your question:")

if st.button("Submit"):

    with st.spinner("Thinking... 🤖"):
        response = requests.post(
            "http://localhost:8000/ask",
            json={"input": user_input}
        )

    data = response.json()

    st.subheader("📘 Explanation")
    st.write(data["answer"])

    st.subheader("📝 Practice Questions")
    for q in data["practice_questions"]:
        st.write(q)