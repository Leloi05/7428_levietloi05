import streamlit as st
st.title('đi ngủ')
import streamlit as st

# ✅ Phải nằm ở đầu tiên sau import
st.set_page_config(page_title="Các Tỉnh Mới", page_icon="🏞️")

# Tiêu đề trang
st.title("🏞️ Khám Phá Các Tỉnh Mới Ở Việt Nam")

# Dữ liệu mẫu
provinces = {
    "Khánh Hòa": {
        "description": "Khánh Hòa là tỉnh ven biển với Nha Trang nổi tiếng.",
        "image_url": "https://cdn.britannica.com/41/94441-050-0AB083E4/Nha-Trang-coast-Khanh-Hoa-Vietnam.jpg"
    },
    "Lào Cai": {
        "description": "Lào Cai có Sa Pa và đỉnh Fansipan – nóc nhà Đông Dương.",
        "image_url": "https://static.vinwonders.com/production/sapa-thang-canh-lao-cai-1.jpg"
    }
}

# Giao diện
province_name = st.selectbox("🗺️ Chọn một tỉnh:", list(provinces.keys()))
province = provinces[province_name]

st.subheader(province_name)
st.image(province["image_url"], use_column_width=True)
st.write(province["description"])
