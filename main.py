import streamlit as st
st.title('hello world')
import random

# Cấu hình trang
st.set_page_config(page_title="Game Oẳn Tù Tì", page_icon="🎮")

# Tiêu đề
st.title("✊ ✌️ ✋ Oẳn Tù Tì")

# Lựa chọn
choices = ["Búa", "Kéo", "Bao"]
user_choice = st.radio("👉 Bạn chọn gì?", choices)

# Khi nhấn nút
if st.button("🎮 Chơi"):
    computer_choice = random.choice(choices)
    st.write(f"🤖 Máy chọn: **{computer_choice}**")

    # Xử lý thắng thua
    if user_choice == computer_choice:
        st.info("⚖️ Hòa rồi!")
    elif (
        (user_choice == "Búa" and computer_choice == "Kéo") or
        (user_choice == "Kéo" and computer_choice == "Bao") or
        (user_choice == "Bao" and computer_choice == "Búa")
    ):
        st.success("🎉 Bạn Thắng!")
    else:
        st.error("💥 Bạn Thua rồi!")

# Ghi chú cuối
st.markdown("---")
st.caption("👨‍💻 Tạo bởi AI hỗ trợ bạn!")
