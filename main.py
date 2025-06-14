import streamlit as st

st.set_page_config(page_title="Fake Mario", layout="wide")

st.title("👾 Mario giả lập bằng Streamlit")

# Dùng session_state để lưu vị trí
if "x" not in st.session_state:
    st.session_state.x = 0

# Bố cục 10 cột mô phỏng vị trí
cols = st.columns(10)

# Hiển thị Mario ở cột x
for i in range(10):
    if i == st.session_state.x:
        cols[i].image("https://i.imgur.com/9Xnt7YF.png", width=60)
    else:
        cols[i].write(" ")

# Nút điều khiển
col1, col2 = st.columns(2)
if col1.button("⬅️ Trái"):
    st.session_state.x = max(0, st.session_state.x - 1)
if col2.button("➡️ Phải"):
    st.session_state.x = min(9, st.session_state.x + 1)
