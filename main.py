import streamlit as st

# ⚙️ Cấu hình trang – phải đặt đầu tiên
st.set_page_config(page_title="Các Tỉnh Mới", page_icon="🌄")

# 🏞️ Tiêu đề chính
st.title("Khám Phá Các Tỉnh Mới Ở Việt Nam")

# 🔍 Dữ liệu tỉnh
provinces = {
    "Quảng Ninh": {
        "description": "Quảng Ninh nổi tiếng với Vịnh Hạ Long – Di sản thiên nhiên thế giới.",
        "image_url": "https://media.vneconomy.vn/w800/images/upload/2023/06/30/vinh-ha-long.jpg"
    },
    "Hà Giang": {
        "description": "Hà Giang có cao nguyên đá Đồng Văn và đèo Mã Pì Lèng hùng vĩ.",
        "image_url": "https://ik.imagekit.io/tvlk/blog/2022/10/du-lich-ha-giang-1.jpg"
    }
}

# 🧭 Giao diện chọn tỉnh
province_name = st.selectbox("🗺️ Chọn một tỉnh để khám phá:", list(provinces.keys()))
province = provinces[province_name]

# 📍 Hiển thị thông tin tỉnh
st.subheader(province_name)
st.image(province["image_url"], use_column_width=True)
st.write(province["description"])
