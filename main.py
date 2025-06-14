import streamlit as st
import random

st.set_page_config(page_title="🏁 Đua Xe Máy", page_icon="🏍️")

st.markdown("## 🏍️ Mô phỏng game đua xe mini")

st.image("https://cdn.pixabay.com/photo/2017/08/07/22/01/motorcycle-2608487_1280.jpg", caption="Chọn hướng rẽ để tránh vật cản!")

choice = st.radio("👉 Chọn hướng đi:", ["⬅️ Trái", "⬆️ Giữa", "➡️ Phải"])

if st.button("🚦 Tiếp tục"):
    result = random.choice(["🏆 An toàn! Bạn vượt chướng ngại vật", "💥 Bị va chạm! Game over", "🚧 Gặp đường xấu, giảm tốc"])
    st.success(f"Kết quả: {result}")
