import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="🏁 Đăng Nhập Đua Xe", page_icon="🏎️")

# Giao diện tiêu đề bằng Markdown
st.markdown("""
# 🏎️ **Đăng Nhập Hệ Thống Đua Xe**
Chào mừng đến với **SpeedZone** – nơi bạn chạm đến giới hạn tốc độ!  
> Hãy khởi động động cơ bằng cách đăng nhập bên dưới:
""")

# Form đăng nhập
with st.form("race_login"):
    username = st.text_input("👤 Tên tài xế")
    password = st.text_input("🔑 Mật khẩu", type="password")
    submit = st.form_submit_button("🔥 Vào đường đua")

# Kiểm tra thông tin
if submit:
    if username == "racer" and password == "fast123":
        st.success("🏁 Đăng nhập thành công! Chuẩn bị vào vạch xuất phát...")
        st.markdown("""
        ### 🚦 Sẵn sàng!
        Bạn đã vào hệ thống. Hãy chọn đường đua và bắt đầu cuộc đua tốc độ!
        """)
    else:
        st.error("❌ Sai thông tin. Hãy kiểm tra lại tên tài xế hoặc mật khẩu.")
