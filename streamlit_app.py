import os
import streamlit as st
import pandas as pd

from src.dataset_inspector import DatasetInspector
from src.preprocessing_advisor import PreprocessingAdvisor


st.set_page_config(
    page_title="OpenClaw ML Research Assistant",
    layout="wide"
)

st.title("OpenClaw ML Research Assistant")

st.markdown("""
Interactive ML dataset inspection and preprocessing recommendation system.
""")

st.header("Dataset Upload")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    os.makedirs("data", exist_ok=True)

    dataset_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(dataset_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success(f"Dataset uploaded: {uploaded_file.name}")

    inspector = DatasetInspector(dataset_path)

    inspector.validate_dataset()

    dataset = inspector.load_dataset()

    st.header("Dataset Preview")

    st.dataframe(dataset.head())
    
    st.header("Missing Value Analysis")

    missing_report = inspector.detect_missing_values()

    st.dataframe(missing_report)
    
    st.header("Schema Information")

    schema_report = inspector.infer_schema()

    st.dataframe(schema_report)
    
    st.header("Preprocessing Recommendations")

    advisor = PreprocessingAdvisor(dataset)

    recommendations = advisor.generate_recommendations()

    for recommendation in recommendations:
        st.info(recommendation)