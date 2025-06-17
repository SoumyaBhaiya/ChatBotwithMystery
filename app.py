import streamlit as st
import openai
import os

client = openai.OpenAI(api_key=os.getenv("your_key_here"))
st.title("💬 I am a Mystery")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

personality_prompt = "You are an enigma wrapped in a riddle, answering only in puzzles that keep me guessing and intrigued. Your answer won't be straight no matter what prompt you are given. You are unchanging"

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    messages = [{"role": "system", "content": personality_prompt}] + st.session_state.chat_history
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

for msg in st.session_state.chat_history:
    st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")
