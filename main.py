import streamlit as st

# ⚙️ Cấu hình trang
st.set_page_config(page_title="Đua Xe Máy", page_icon="🏍️")

# 🚩 Tiêu đề bằng Markdown
st.markdown("""
# 🏍️ **MOTO RACE - CUỘC ĐUA XE MÁY THẦN TỐC**
> Chào mừng bạn đến với cuộc đua tốc độ!  
> Hãy chọn chiếc xe máy yêu thích và địa hình để khởi động động cơ!  
---
""")

# 🛵 Chọn xe máy
bike = st.selectbox("🛵 Chọn xe máy đua:", [
    "Exciter 155 VVA",
    "Winner X",
    "Wave Alpha Tăng Áp",
    "Honda Sonic 150R",
    "Suzuki Raider R150"
])

# 🏞️ Chọn địa hình đua
terrain = st.radio("🌍 Chọn địa hình:", [
    "Đường nhựa thành phố",
    "Đường núi hiểm trở",
    "Đường đua sân vận động",
    "Đường bùn địa hình"
])

# ⚡ Chọn tốc độ
speed = st.slider("⚙️ Chọn tốc độ khởi điểm (Km/h):", min_value=40, max_value=200, step=10, value=100)

# 🚀 Nút bắt đầu đua
if st.button("🔥 BẮT ĐẦU CUỘC ĐUA"):
    st.success(f"🏁 Bạn đang cưỡi **{bike}** trên địa hình **{terrain}** với tốc độ **{speed} Km/h**!")
    st.balloons()
    st.markdown("### 🏆 Vượt qua tất cả và trở thành tay đua huyền thoại!")

# 📸 Hình ảnh minh họa xe đua
st.image("https://cdn.pixabay.com/photo/2015/05/15/14/42/motorcycle-768923_1280.jpg", use_column_width=True, caption="Tăng tốc nào!")

# 📎 Chữ kết
st.markdown("---")
st.caption("🎮 Trang web mô phỏng đua xe máy bằng Streamlit & Markdown – Thiết kế bởi AI")
