import streamlit as st
import requests

st.set_page_config(page_title="Drug-Disease Interaction", page_icon="💊", layout="centered")

st.title("💊 Drug-Disease Interaction App")
st.markdown("Use the controls below to select specific features to predict whether a drug interacts with a disease.")

# Input sections with better layout
with st.expander("📊 Number of Drug Targets", expanded=False):
    num_drugtargets = st.number_input(
        "Select the total number of target proteins that the drug interacts with. Range: 0 - 191.", min_value=0, max_value=191, value=1, step=1
    )

with st.expander("🧪 Target Proteins", expanded=False):
    st.caption("Select the specific target proteins involved in the disease pathway.")
    st.caption("✔️ Checked = present (1), ⬜ Unchecked = not present (0).")

    Target_A0A024R8I1 = int(st.checkbox("Target Protein A0A024R8I1", value=False))

    Target_A0A0E1R3H3 = int(st.checkbox("Target Protein A0A0E1R3H3", value=False))

    Target_A0A0H2XJ39 = int(st.checkbox("Target Protein A0A0H2XJ39", value=False))

    Target_A0A143ZZK9 = int(st.checkbox("Target Protein A0A143ZZK9", value=False))

with st.expander("🧬 Number of Biological Pathways", expanded=False):
    num_pathways = st.number_input(
        "Select the total number of biological pathways affected by the drug. Range: 0 - 3.", min_value=0, max_value=3, value=1, step=1
    )

with st.expander("🧬 Biological Pathways", expanded=False):
    st.caption("Select the specific biological pathways affected by the drug.")
    st.caption("✔️ Checked = drug interacts with biological pathway (1), ⬜ Unchecked = not present (0).")

    Pathway_Axon_guidance = int(st.checkbox("Pathway: Axon guidance", value=False))
    Pathway_Cell_adhesion_molecules__CAMs_ = int(st.checkbox("Pathway: Cell adhesion molecules (CAMs)", value=False))
    Pathway_Developmental_Biology = int(st.checkbox("Pathway: Developmental Biology", value=False))
    Pathway_Ephrin_signaling = int(st.checkbox("Pathway: Ephrin signaling", value=False))

# Prepare data
params = {
    "Num_DrugTargets": num_drugtargets,
    "Num_Pathways": num_pathways,
    "Target_A0A024R8I1": Target_A0A024R8I1,
    "Target_A0A0E1R3H3": Target_A0A0E1R3H3,
    "Target_A0A0H2XJ39": Target_A0A0H2XJ39,
    "Target_A0A143ZZK9": Target_A0A143ZZK9,
    "Pathway_Axon_guidance": Pathway_Axon_guidance,
    "Pathway_Cell_adhesion_molecules__CAMs_": Pathway_Cell_adhesion_molecules__CAMs_,
    "Pathway_Developmental_Biology": Pathway_Developmental_Biology,
    "Pathway_Ephrin_signaling": Pathway_Ephrin_signaling
}

# Interaction prediction
if st.button("🔍 Predict Interaction"):
    try:
        response = requests.get(url="https://y-28999410199.europe-west1.run.app/predict", params=params)
        result = response.json()

        def from_num_interaction(x):
            return "no interaction between the drug and the disease" if x == 0 else "an interaction between the drug and the disease"

        pretty_pred = from_num_interaction(result['interaction'])

        st.success(f"✅ Prediction: There is **{pretty_pred}**.")
    except Exception as e:
        st.error(f"❌ Failed to get prediction: {e}")
