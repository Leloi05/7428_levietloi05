import streamlit as st

# --- Cấu hình trang
st.set_page_config(page_title="Scratch Login Demo", page_icon="🐱", layout="wide")

# --- Session state để lưu trạng thái đăng nhập
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Hàm kiểm tra đăng nhập
def check_login(username, password):
    return username == "scratchuser" and password == "1234"

# --- Nếu chưa đăng nhập
if not st.session_state.logged_in:
    st.markdown("## 🔐 Scratch Login")
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")
    if st.button("➡️ Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.success("✅ Đăng nhập thành công!")
        else:
            st.error("❌ Sai tài khoản hoặc mật khẩu.")
    st.stop()

# --- Header sau khi đăng nhập
st.markdown("""
<style>
.scratch-header {
    background-color: #974ec3;
    padding: 1rem;
    color: white;
    font-size: 22px;
    font-weight: bold;
}
</style>
<div class='scratch-header'>
🐱 Scratch Giả Lập &nbsp;&nbsp;&nbsp;&nbsp;
<span>Xin chào, <strong>scratchuser</strong>!</span>
</div>
""", unsafe_allow_html=True)

# --- Giao diện chính
st.markdown("## 🏆 Featured Scratch Games")

game_data = [
    {
        "name": "Flappy Bird Remix",
        "img": "https://cdn2.scratch.mit.edu/get_image/project/770178950_144x108.png",
        "url": "https://scratch.mit.edu/projects/770178950/"
    },
    {
        "name": "Car Racing Game",
        "img": "https://cdn2.scratch.mit.edu/get_image/project/596235086_144x108.png",
        "url": "https://scratch.mit.edu/projects/596235086/"
    },
    {
        "name": "Cat Jump",
        "img": "https://cdn2.scratch.mit.edu/get_image/project/532063343_144x108.png",
        "url": "https://scratch.mit.edu/projects/532063343/"
    },
    {
        "name": "Maze Runner",
        "img": "https://cdn2.scratch.mit.edu/get_image/project/671704498_144x108.png",
        "url": "https://scratch.mit.edu/projects/671704498/"
    }
]

cols = st.columns(4)
for i, game in enumerate(game_data):
    with cols[i]:
        st.image(game["img"], caption=game["name"], use_column_width=True)
        st.markdown(f"[🎮 Chơi ngay]({game['url']})")

# --- Nút đăng xuất
if st.button("🔓 Đăng xuất"):
    st.session_state.logged_in = False
    st.rerun()
