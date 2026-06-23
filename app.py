import streamlit as st

st.set_page_config(page_title="Colon Cancer Decision Tool")

st.title("Colon Cancer Decision Support Tool")

stage = st.selectbox(
    "Select Colon Cancer Stage",
    ["Stage I", "Stage II", "Stage III", "Stage IV"]
)

if st.button("Show Recommendation"):

    if stage == "Stage I":
        recommendation = """
        Observation after curative surgery.
        No adjuvant chemotherapy recommended.
        """

    elif stage == "Stage II":
        recommendation = """
        Evaluate high-risk features.
        Consider adjuvant chemotherapy in selected patients.
        """

    elif stage == "Stage III":
        recommendation = """
        Adjuvant chemotherapy recommended.

        Options:
        - FOLFOX
        - CAPOX
        """

    elif stage == "Stage IV":
        recommendation = """
        Metastatic disease.

        Consider:
        - Systemic therapy
        - Targeted therapy when appropriate
        - Surgical evaluation if resectable
        """

    st.subheader("Recommendation")
    st.success(recommendation)

st.markdown("---")
st.caption("Educational prototype only. Not for clinical decision-making.")
