import streamlit as st
from PIL import Image
from random import randint
import pandas as pd


st.title("Image Classification with History")
uploaded_file = st.file_uploader("Upload" , type = ["jpg","png","jpeg"])
image_display = st.empty()

if "history" not in st.session_state:
    st.session_state["history"] = []


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_display.image(image,caption = "Uploaded Image")

    if st.button("Classify"):
        image_display.empty()
        label = randint(0,10)
        st.write(f"Predicted class: {label}")

        st.session_state["history"].append({
            "Image": uploaded_file.name ,
            "Prediction": label
        })


st.subheader("Classification History")

if st.session_state["history"]:
    history_df = pd.DataFrame(st.session_state["history"])
    st.dataframe(history_df)
else:
    st.write("First , upload an image and classify")
