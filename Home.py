import streamlit as st
from PIL import Image
import base64

# Convert the image to base64 for inline HTML rendering
def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get base64 encoded string
image_base64 = get_image_base64("AI (4).png")

# Custom HTML to align image top-left
st.markdown(
    f"""
    <div style="position: absolute; top: 10px; left: 10px;">
        <img src="data:image/png;base64,{image_base64}" alt="AI Logo" style="height: 80px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Add some top padding so the title doesn't overlap
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

st.title("AI-Driven Drug Repurposing App")

st.markdown("""
            ---
""")

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

st.markdown("""
            ---
            :rocket: Pick a page from the sidebar to get started!
""")
