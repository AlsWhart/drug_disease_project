import streamlit as st
from PIL import Image
import base64

# Convert image to base64
def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load all images
ai_image_base64 = get_image_base64("images/AI (4).png")
drugs_image_base64 = get_image_base64("images/drugs.png")
proteins_image_base64 = get_image_base64("images/Target proteins.png")
ml_image_base64 = get_image_base64("images/machine learning (4).png")

# Display images in a row using HTML/CSS
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: flex-start; padding: 20px;">
        <img src="data:image/png;base64,{ai_image_base64}" alt="AI Logo" style="height: 100px; margin-right: 30px;">
        <img src="data:image/png;base64,{drugs_image_base64}" alt="Drugs" style="height: 100px; margin-right: 30px;">
        <img src="data:image/png;base64,{proteins_image_base64}" alt="Proteins" style="height: 100px; margin-right: 30px;">
        <img src="data:image/png;base64,{ml_image_base64}" alt="Machine Learning" style="height: 100px; margin-right: 30px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Padding below images
st.markdown("<br>", unsafe_allow_html=True)
st.title("AI-Driven Drug Repurposing App")
st.markdown("""🧠 Developers: Dr. Francy Johanna Pérez-Llanos, Alice Wharton, Dr. Marijana Jevtić, Luka Jelic and Sjoerd de Wit.""")
st.markdown("""---""")

#Sections for better layout
with st.expander("Welcome to the AI-Driven Drug Repurposing App!", expanded=False):
    st.caption("This project serves as a proof of concept (PoC) to demonstrate the feasibility of using AI and genomic data for drug repurposing. By integrating multi-source biomedical datasets, we aim to explore whether machine learning models can successfully predict new drug-disease relationships based on genomic biomarkers and drug interactions.")

with st.expander("🔬 How it works", expanded=False):
    st.caption("The app uses a machine learning model hosted on a cloud API to make the prediction. Simply choose a drug and a disease and the app will query the model and display the result.")

st.markdown("""
            ---
            #### :test_tube: App Sections
""")

with st.expander("Advanced Prediction for Researchers"):
    st.caption("A more detailed version where you can input specific biological features of a drug-disease interaction like whether a target protein is involved in the disease pathway and whether the drug affects a specific biological pathway — designed for advanced users and researchers.")

with st.expander("General Prediction for Everyone"):
    st.caption("A simplified version where you just select a **drug** and a **disease** from dropdown menus — no technical background is needed. Ideal for quick searches.")
st.markdown("""🚀 Pick a page from the sidebar to get started!""")
st.markdown("""---""")

with st.expander("References"):
    st.caption("Images created in BioRender. Perez, J. (2025) https://BioRender.com/vg8e5t0")
