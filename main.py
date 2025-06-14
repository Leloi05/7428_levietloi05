import streamlit as st

# ⚙️ Cấu hình trang
st.set_page_config(page_title="Trang Web Scratch Giả Lập", page_icon="🐱", layout="wide")

# 🔵 Header chính (logo và menu)
st.markdown("""
<style>
    .scratch-header {
        background-color: #974ec3;
        padding: 1rem;
        color: white;
        font-size: 22px;
        font-weight: bold;
    }
    .menu-buttons > button {
        margin-right: 10px;
    }
</style>
<div class='scratch-header'>
    🐱 Scratch Giả Lập &nbsp;&nbsp;&nbsp;&nbsp;
    <span class='menu-buttons'>
        <button>Start Creating</button>
        <button>Join</button>
        <button>Sign in</button>
    </span>
</div>
""", unsafe_allow_html=True)

# 🔮 Nút giới thiệu
st.markdown("### 👨‍💻 About Scratch | 👨‍👩‍👧‍👦 For Parents | 🧑‍🏫 For Educators")

# 🎬 Video banner placeholder
st.markdown("## 🎥 Watch Video")
st.image("https://cdn.scratch.mit.edu/get_image/gallery/1118595_170x100.png", caption="Scratch Promo")

# 📂 Các dự án nổi bật (giả lập bằng card)
st.markdown("## 🏆 Featured Projects")
cols = st.columns(5)
project_images = [
    "https://cdn.scratch.mit.edu/get_image/project/650093752_144x108.png",
    "https://cdn.scratch.mit.edu/get_image/project/649999950_144x108.png",
    "https://cdn.scratch.mit.edu/get_image/project/650028177_144x108.png",
    "https://cdn.scratch.mit.edu/get_image/project/650016825_144x108.png",
    "https://cdn.scratch.mit.edu/get_image/project/650043322_144x108.png"
]

project_names = [
    "Game Vượt Chướng Ngại",
    "Typing Speed Test",
    "Bản Đồ Mini",
    "Pixel Adventure",
    "Game Lập Trình Mèo"
]

for i in range(5):
    with cols[i]:
        st.image(project_images[i], use_column_width=True)
        st.caption(f"🎮 {project_names[i]}")

# 📁 Studio nổi bật
st.markdown("## 🌟 Featured Studios")
cols = st.columns(4)
studio_names = ["Studio Game 1", "Thử Thách Mèo", "Game Nhập Vai", "Studio Scratcher"]
for i in range(4):
    with cols[i]:
        st.markdown(f"🗂️ {studio_names[i]}")
        st.image("https://cdn.scratch.mit.edu/get_image/gallery/1118595_170x100.png", use_column_width=True)
