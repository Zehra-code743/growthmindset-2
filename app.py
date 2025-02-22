import streamlit as st  # type: ignore
import requests  # type: ignore
from PIL import Image  # type: ignore

# Set Page Layout
st.set_page_config(page_title="AI Image Colorizer", layout="wide")

# Sidebar for Theme Selection
st.sidebar.title("Settings")
theme = st.sidebar.radio("Select Theme", ("Light", "Dark"))

# Define Colors
if theme == "Light":
    primary_color = "#4CAF50"
    bg_color = "#f8f9fa"
    text_color = "#333333"
    shadow_color = "rgba(0, 0, 0, 0.1)"
else:
    primary_color = "#90EE90"
    bg_color = "#1e1e1e"
    text_color = "#ffffff"
    shadow_color = "rgba(255, 255, 255, 0.1)"

# Custom CSS for Beautiful UI
st.markdown(f"""
    <style>
        body {{ background-color: {bg_color}; color: {text_color}; }}
        .big-font {{ font-size:22px !important; font-weight: bold; }}
        .stButton>button {{ background-color: {primary_color}; color: white; font-size: 18px; padding: 12px 24px; border-radius: 10px; box-shadow: 4px 4px 15px {shadow_color}; transition: 0.3s; }}
        .stButton>button:hover {{ transform: scale(1.05); }}
        .stFileUploader {{ border: 3px dashed {primary_color}; padding: 15px; border-radius: 10px; text-align: center; }}
        .stImage {{ border-radius: 10px; box-shadow: 4px 4px 15px {shadow_color}; }}
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown(f"<h1 style='text-align: center; color: {primary_color};'>🖌️ AI Image Colorizer</h1>", unsafe_allow_html=True)
st.markdown("<p class='big-font' style='text-align: center;'>Give life to black & white images using AI! ✨</p>", unsafe_allow_html=True)

# Example Images
st.subheader("Example Before & After:")
col1, col2 = st.columns(2)
with col1:
    st.image("https://i.imgur.com/F0ZIW0P.jpg", caption="Black & White", use_column_width=True)
with col2:
    st.image("https://i.imgur.com/k8OIfgM.jpg", caption="Colorized", use_column_width=True)

st.markdown("---")

# Upload Image
st.markdown("### Upload Your Image:")
uploaded_file = st.file_uploader("Upload a Black & White Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("🎨 Colorize Image"):
        st.write("Processing your image... ⏳")
        
        # Send to API for Colorization (Replace with your API key)
        response = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={"image": uploaded_file.getvalue()},
            headers={"api-key": "YOUR_DEEPAI_API_KEY"}
        )

        # Get Response
        if response.status_code == 200:
            output_url = response.json()["output_url"]
            st.image(output_url, caption="Colorized Image", use_column_width=True)
            
            # Download Button
            st.download_button("⬇️ Download Colorized Image", requests.get(output_url).content, "colorized.jpg", "image/jpeg")
        else:
            st.error("⚠️ Failed to process the image. Try again later!")

# AI Colorization Tips
st.markdown("## Tips for Best Results:")
st.info("🔹 Use high-quality black & white images for better results.")
st.info("🔹 Faces and landscapes work best with AI colorization.")
st.info("🔹 Avoid images with excessive noise or low contrast.")

# Footer
st.markdown(f"<p style='text-align: center; color: grey;'>Powered by AI & Streamlit | Created by Shan-E-Zehra</p>", unsafe_allow_html=True)
