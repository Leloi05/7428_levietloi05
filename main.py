import streamlit as st
import random
import time

# 🚥 Cấu hình trang
st.set_page_config(page_title="🏁 Game Đua Xe Mini", page_icon="🏍️")

# 🏎️ Tiêu đề bằng Markdown
st.markdown("""
# 🏍️ **MOTO RACE SIMULATOR**
Chào mừng bạn đến với game đua xe máy mini!  
> Hãy chọn xe, địa hình và tốc độ. Sau đó bắt đầu cuộc đua và xem kết quả!
---
""")

# 🔧 Lựa chọn của người chơi
car = st.selectbox("🛵 Chọn xe máy:", ["Winner X", "Exciter", "Wave Alpha", "Sirius", "Raider"])
track = st.radio("🛣️ Chọn địa hình:", ["Đường nhựa", "Đường đất", "Đồi núi", "Thành phố"])
speed = st.slider("⚙️ Tốc độ (Km/h):", 50, 300, 150, step=10)

# 🚀 Bắt đầu đua
if st.button("🔥 BẮT ĐẦU ĐUA"):
    st.markdown(f"### 🚦 Bắt đầu đua với **{car}** trên địa hình **{track}** với tốc độ **{speed} Km/h**...")
    st.info("Đang tính toán kết quả cuộc đua...")
    time.sleep(2)

    # 🎲 Kết quả ngẫu nhiên
    result = random.choice(["🏆 Bạn đã chiến thắng!", "😓 Bạn về nhì", "💥 Xe bị hỏng giữa đường", "🥉 Bạn về thứ ba"])

    st.success(result)

    # 📸 Ảnh minh họa
    st.image("https://cdn.pixabay.com/photo/2017/02/01/16/38/motorcycle-racing-2035702_1280.jpg", caption="Cuộc đua đã kết thúc!", use_column_width=True)

# 📌 Footer
st.markdown("---")
st.caption("🎮 Game mô phỏng đua xe mini bằng Streamlit + Markdown – Thiết kế bởi ChatGPT")
