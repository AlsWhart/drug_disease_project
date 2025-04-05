import streamlit as st

st.title("Drug-Disease Interaction Prediction App")

st.markdown("""
Welcome to the **Drug-Disease Interaction App**!
This project serves as a proof of concept (PoC) to demonstrate the feasibility of using AI and genomic data for drug repurposing. By integrating multi-source biomedical datasets, we aim to explore whether machine learning models can successfully predict new drug-disease relationships based on genomic biomarkers and drug interactions.

:microscope: **How it works:**
The app uses a machine learning model hosted on a cloud API to make the prediction. Simply choose a drug and a disease and the app will query the model and display the result.


---

### :test_tube: App Sections:

#### 1. General Prediction (for Everyone)
A simplified version where you just select a **drug** and a **disease** from dropdown menus — no technical background needed. Ideal for quick searches.

#### 2. Advanced Prediction (for Researchers)
A more detailed version where you can input specific biological features of a drug-disease interaction like whether a target protein is involved in the disease pathway and whether the drug affects a specific biological pathway — designed for advanced users and researchers.

---

:rocket: Pick a page from the sidebar to get started!
""")
