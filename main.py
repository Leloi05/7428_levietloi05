import streamlit as st
import random
import time

st.set_page_config(page_title="🎴 Memory Card Game", page_icon="🧠", layout="centered")
st.title("🧠 Memory Card Game")

# Danh sách cặp thẻ (dùng emoji cho đơn giản)
emojis = ["🐶", "🐱", "🐶", "🐱", "🐵", "🐵"]
random.shuffle(emojis)

# Session state
if "cards" not in st.session_state:
    st.session_state.cards = ["❓"] * 6
    st.session_state.emojis = emojis
    st.session_state.flipped = []
    st.session_state.matched = []
    st.session_state.moves = 0

# Reset game
if st.button("🔄 Chơi lại"):
    emojis = ["🐶", "🐱", "🐶", "🐱", "🐵", "🐵"]
    random.shuffle(emojis)
    st.session_state.cards = ["❓"] * 6
    st.session_state.emojis = emojis
    st.session_state.flipped = []
    st.session_state.matched = []
    st.session_state.moves = 0

# Hiển thị 2 hàng x 3 cột
cols = st.columns(3)

for i in range(6):
    if st.session_state.cards[i] != "❓" or i in st.session_state.matched:
        cols[i % 3].button(st.session_state.emojis[i], key=i, disabled=True)
    else:
        if cols[i % 3].button("❓", key=i):
            st.session_state.cards[i] = st.session_state.emojis[i]
            st.session_state.flipped.append(i)

# Kiểm tra lật 2 thẻ
if len(st.session_state.flipped) == 2:
    idx1, idx2 = st.session_state.flipped
    if st.session_state.emojis[idx1] == st.session_state.emojis[idx2]:
        st.session_state.matched.extend([idx1, idx2])
    else:
        time.sleep(1)
        st.session_state.cards[idx1] = "❓"
        st.session_state.cards[idx2] = "❓"
    st.session_state.flipped = []
    st.session_state.moves += 1
    st.experimental_rerun()

# Kết thúc game
if len(st.session_state.matched) == 6:
    st.success(f"🎉 Hoàn thành trong {st.session_state.moves} lượt!")

