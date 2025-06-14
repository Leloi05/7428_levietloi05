import streamlit as st

st.set_page_config(page_title="🏁 Game Đua Xe", page_icon="🚗")

# --- Dữ liệu cấp độ
levels = {
    1: {"correct": "Thẳng", "message": "Bạn thấy con đường rộng mở phía trước."},
    2: {"correct": "Trái", "message": "Một khúc cua bất ngờ hiện ra bên trái!"},
    3: {"correct": "Phải", "message": "Một xe tải chắn đường, bạn cần tránh sang phải."},
    4: {"correct": "Thẳng", "message": "Tăng tốc về đích!"},
}

# --- Trạng thái phiên chơi
if "level" not in st.session_state:
    st.session_state.level = 1
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🚗 Game Đua Xe – Chọn Hướng")

st.markdown(f"### 🛣️ Cấp độ: {st.session_state.level}")
st.markdown(f"🔧 {levels[st.session_state.level]['message']}")

# --- Chọn hướng
choice = st.radio("👉 Chọn hướng di chuyển:", ["Trái", "Phải", "Thẳng"])

if st.button("🏎️ Tiếp tục"):
    correct = levels[st.session_state.level]["correct"]
    if choice == correct:
        st.success("✅ Tuyệt vời! Bạn đã chọn đúng hướng.")
        st.session_state.score += 1
        if st.session_state.level < len(levels):
            st.session_state.level += 1
        else:
            st.balloons()
            st.success(f"🎉 Bạn đã hoàn thành game với {st.session_state.score} điểm!")
            if st.button("🔁 Chơi lại"):
                st.session_state.level = 1
                st.session_state.score = 0
    else:
        st.error("❌ Bạn đã chọn sai và bị va chạm!")
        st.markdown(f"💥 Hướng đúng là: **{correct}**")
        if st.button("🔁 Thử lại"):
            st.session_state.level = 1
            st.session_state.score = 0
