import streamlit as st
st.title('đi ngủ')
# Danh sách tỉnh mẫu
provinces = {
    "Khánh Hòa": {
        "description": "Khánh Hòa là một tỉnh ven biển thuộc Nam Trung Bộ Việt Nam, nổi tiếng với thành phố biển Nha Trang.",
        "image_url": "https://cdn.britannica.com/41/94441-050-0AB083E4/Nha-Trang-coast-Khanh-Hoa-Vietnam.jpg"
    },
    "Lào Cai": {
        "description": "Lào Cai là tỉnh vùng núi phía Bắc, nơi có thị trấn Sapa nổi tiếng với phong cảnh tuyệt đẹp và đỉnh Fansipan.",
        "image_url": "https://static.vinwonders.com/production/sapa-thang-canh-lao-cai-1.jpg"
    },
    "Bình Định": {
        "description": "Bình Định nổi tiếng với võ thuật cổ truyền và những bãi biển hoang sơ, thơ mộng như Kỳ Co, Eo Gió.",
        "image_url": "https://media-cdn-v2.laodong.vn/Storage/NewsPortal/2022/7/14/1060995/Binh-Dinh-4.jpg"
    }
}

# Giao diện trang
st.set_page_config(page_title="Các Tỉnh Mới", page_icon="🏞️")
st.title("🏞️ Khám Phá Các Tỉnh Mới Ở Việt Nam")

# Chọn tỉnh
province_name = st.selectbox("🗺️ Chọn một tỉnh để xem thông tin:", list(provinces.keys()))

# Hiển thị thông tin
province = provinces[province_name]
st.subheader(province_name)
st.image(province["image_url"], use_column_width=True)
st.write(province["description"])

st.markdown("---")
st.caption("Tạo bởi bạn và AI 🤖")
