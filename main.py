import streamlit as st

st.set_page_config(page_title="🧠 Đố Vui Trắc Nghiệm", page_icon="❓")

st.title("🧠 Đố Vui Trắc Nghiệm")

# Danh sách câu hỏi
questions = [
    {
        "question": "Quốc gia nào có diện tích lớn nhất thế giới?",
        "options": ["Trung Quốc", "Hoa Kỳ", "Canada", "Nga"],
        "answer": "Nga"
    },
    {
        "question": "Python là gì?",
        "options": ["Ngôn ngữ lập trình", "Con rắn", "Trình duyệt", "Bộ phim"],
        "answer": "Ngôn ngữ lập trình"
    },
    {
        "question": "Streamlit dùng để làm gì?",
        "options": ["Viết báo cáo", "Tạo web app bằng Python", "Chơi game", "Học Toán"],
        "answer": "Tạo web app bằng Python"
    },
]

# Khởi tạo trạng thái
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answers = []

# Câu hỏi hiện tại
q = questions[st.session_state.current_q]
st.markdown(f"### ❓ Câu {st.session_state.current_q + 1}: {q['question']}")
choice = st.radio("Chọn một đáp án:", q["options"], key=st.session_state.current_q)

if st.button("Trả lời"):
    if choice == q["answer"]:
        st.success("✅ Chính xác!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Sai! Đáp án đúng là: {q['answer']}")
    st.session_state.answers.append(choice)

    # Chuyển sang câu tiếp theo
    if st.session_state.current_q + 1 < len(questions):
        st.session_state.current_q += 1
        st.experimental_rerun()
    else:
        st.balloons()
        st.success(f"🎉 Bạn đã hoàn thành {len(questions)} câu hỏi!")
        st.info(f"📊 Điểm số của bạn: **{st.session_state.score} / {len(questions)}**")
        if st.button("🔁 Làm lại"):
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.answers = []
            st.experimental_rerun()
