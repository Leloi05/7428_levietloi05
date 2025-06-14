import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="🏁 Game Đua Xe", page_icon="🏎️", layout="centered")

# Tiêu đề trang
st.markdown("""
# 🏎️ **SPEEDZONE - GAME ĐUA XE SIÊU TỐC**
Chào mừng bạn đến với thế giới tốc độ!  
Hãy chọn xe đua, chọn đường đua và bấm nút **"BẮT ĐẦU ĐUA"** để cháy hết mình!  
---
""")

# Hình ảnh minh họa
st.image("https://cdn.pixabay.com/photo/2020/01/28/01/23/sportscar-4798262_1280.jpg", caption="Sẵn sàng để đua?", use_column_width=True)

# Chọn xe đua
car = st.selectbox("🚘 Chọn xe đua:", ["Xe Tia Chớp", "Xe Địa Hình", "Xe Công Thức 1", "Xe Bay Cyber"])

# Chọn đường đua
track = st.radio("🛣️ Chọn đường đua:", ["Đường Thành Phố", "Sa Mạc Nóng Bỏng", "Rừng Tốc Độ", "Đường Đua Mặt Trăng"])

# Chọn tốc độ
speed = st.slider("⚙️ Chọn tốc độ (Km/h):", 50, 400, 150, step=10)

# Nút bắt đầu
if st.button("🔥 BẮT ĐẦU ĐUA"):
    st.success(f"🚀 Bạn đang đua với **{car}** trên đường **{track}** với tốc độ **{speed} Km/h**!")
    st.balloons()
    st.markdown("### 🏆 Hãy cố gắng để về đích trước mọi đối thủ!")

# Footer
st.markdown("---")
st.caption("🎮 Trang web demo game đua xe - thiết kế bởi ChatGPT")
