import streamlit as st
st.title('hello world')
import streamlit as st
import random

st.set_page_config(page_title="Game Oẳn Tù Tì", page_icon="🎮", layout="centered")

st.title("✌️✊✋ Oẳn Tù Tì")

choices = ["Kéo", "Búa", "Bao"]
user_choice = st.selectbox("Bạn chọn gì?", choices)

if st.button("Chơi!"):
    computer_choice = random.choice(choices)
    st.write(f"🤖 Máy chọn: **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("⚖️ Hòa rồi!")
    elif (
        (user_choice == "Kéo" and computer_choice == "Bao") or
        (user_choice == "Búa" and computer_choice == "Kéo") or
        (user_choice == "Bao" and computer_choice == "Búa")
    ):
        st.success("🎉 Bạn thắng!")
    else:
        st.error("💥 Bạn thua rồi!")

st.markdown("---")
st.caption("Tạo bởi bạn và AI 🧠")
