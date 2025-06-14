import streamlit as st
st.title('hello world')
import streamlit as st
import random

# Thiết lập session state cho số bí mật
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

st.title("🎮 Trò chơi đoán số 🎯")
st.subheader("Hãy đoán một số từ 1 đến 100!")

# Nhập số
guess = st.number_input("Nhập số bạn đoán:", min_value=1, max_value=100, step=1)

# Nút "Đoán"
if st.button("Đoán"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.warning("🔼 Số bí mật lớn hơn!")
    elif guess > st.session_state.secret_number:
        st.warning("🔽 Số bí mật nhỏ hơn!")
    else:
        st.success(f"🎉 Chính xác! Bạn đã đoán đúng sau {st.session_state.attempts} lần.")
        # Reset game
        if st.button("Chơi lại"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0

# Hiện số lần đoán
st.info(f"Số lần bạn đã đoán: {st.session_state.attempts}")
