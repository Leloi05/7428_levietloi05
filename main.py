import streamlit as st

# ⚙️ Đặt cấu hình trang đầu tiên
st.set_page_config(page_title="Đăng Nhập", page_icon="🔐")

# 📝 Hiển thị tiêu đề bằng Markdown
st.markdown("""
# 🔐 Đăng Nhập
Chào mừng bạn đến với hệ thống!  
Vui lòng nhập thông tin để tiếp tục.
""")

# 📥 Tạo form đăng nhập
with st.form("login_form"):
    username = st.text_input("👤 Tên đăng nhập")
    password = st.text_input("🔑 Mật khẩu", type="password")
    submitted = st.form_submit_button("Đăng Nhập")

# ✅ Kiểm tra thông tin đăng nhập
if submitted:
    if username == "admin" and password == "123456":
        st.success("✅ Đăng nhập thành công!")
        st.markdown("### 🎉 Chào mừng, **admin**!")
    else:
        st.error("❌ Tên đăng nhập hoặc mật khẩu không đúng.")
