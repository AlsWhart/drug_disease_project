import streamlit as st
import requests

# Page title with emoji
st.title("💊 Drug-Disease Interaction App 🔬")

st.markdown("Select a drug and a disease from the dropdown menus below:")

# Example options (you can extend this list)
drug_options = [
    "aspirin", "acetaminophen", "ibuprofen", "paracetamol", "penicillin",
    "amoxicillin", "metformin", "oxygen", "insulin"
]

disease_options = [
    "diabetes", "hypertension", "cancer", "asthma", "covid-19",
    "congenital abnormality", "alzheimer", "arthritis", "depression"
]

# Dropdown menus
selected_drug = st.selectbox("🧪 Select a Drug", drug_options)
selected_disease = st.selectbox("⚕️ Select a Disease", disease_options)

# Format inputs for the API
drug_param = selected_drug.lower().replace(" ", "%20")
disease_param = selected_disease.lower().replace(" ", "%20")

# Construct URL
base_url = "https://apiproject-946982222667.europe-west1.run.app/predict"
full_url = f"{base_url}?new_drug={drug_param}&new_disease={disease_param}"

# API Call
response = requests.get(full_url).json()

# Display result with conditional logic
st.subheader("🔎 Interaction Result:")
if response == "1.00":
    st.success(f"✅ There is **an interaction** between **{selected_drug}** and **{selected_disease}**.")
elif response == "0.50":
    st.success(f"✅ There is **a 50% chance of an interaction** between **{selected_drug}** and **{selected_disease}**.")
else:
    st.warning(f"⚠️ There is **no interaction** known between **{selected_drug}** and **{selected_disease}**.")

# Footer
st.markdown("💡 *This app helps analyse potential drug-disease interactions!*")
