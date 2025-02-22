import streamlit as st # type: ignore
import requests # type: ignore
from PIL import Image # type: ignore
import io

# Set Page Layout
st.set_page_config(page_title="AI Image Colorizer", layout="centered")

# Sidebar for Theme Selection
st.sidebar.title("Settings")
theme = st.sidebar.radio("Select Theme", ("Light", "Dark"))

# Define Colors
if theme == "Light":
    primary_color = "#4CAF50"
    bg_color = "#ffffff"
    text_color = "#000000"
    shadow_color = "rgba(0, 0, 0, 0.1)"
else:
    primary_color = "#90EE90"
    bg_color = "#121212"
    text_color = "#ffffff"
    shadow_color = "rgba(255, 255, 255, 0.1)"

# Custom CSS for Beautiful UI
st.markdown(f"""
    <style>
        body {{ background-color: {bg_color}; color: {text_color}; }}
        .big-font {{ font-size:20px !important; }}
        .stButton>button {{ background-color: {primary_color}; color: white; font-size: 16px; padding: 10px 20px; border-radius: 10px; box-shadow: 2px 2px 10px {shadow_color}; }}
        .stFileUploader {{ border: 2px dashed {primary_color}; padding: 10px; border-radius: 10px; }}
        .stImage {{ border-radius: 10px; box-shadow: 2px 2px 10px {shadow_color}; }}
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown(f"<h1 style='text-align: center; color: {primary_color};'>AI Image Colorizer</h1>", unsafe_allow_html=True)
st.markdown("<p class='big-font' style='text-align: center;'>Upload a black & white image and get it colorized using AI!</p>", unsafe_allow_html=True)

# Upload Image
uploaded_file = st.file_uploader("Upload a Black & White Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display Uploaded Image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Colorize Image"):
        st.write("Processing your image... ⏳")
        
        # Convert file to bytes
        img_bytes = uploaded_file.read()

        # Send to API for Colorization (Replace with your API key)
        response = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={"image": img_bytes},
            headers={"api-key": "YOUR_DEEPAI_API_KEY"}
        )

        # Get Response
        if response.status_code == 200:
            output_url = response.json()["output_url"]
            st.image(output_url, caption="Colorized Image", use_column_width=True)
            
            # Download Button
            st.download_button("Download Colorized Image", requests.get(output_url).content, "colorized.jpg", "image/jpeg")
        else:
            st.error("Failed to process the image. Try again later!")

# Footer
st.markdown(f"<p style='text-align: center; color: grey;'>Powered by AI & Streamlit | Created by Shan-E-Zehra</p>", unsafe_allow_html=True)
