import streamlit as st

st.title("Ứng dụng Streamlit đầu tiên")
st.write("Chào bạn! Giao diện web đã sẵn sàng.")

name = st.text_input("Nhập tên của bạn:")
if name:
    st.success(f"Xin chào {name}!")