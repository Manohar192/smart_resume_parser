import streamlit as st
import pandas as pd
from parser import extract_text, parse_resume

st.title("📄 Smart Resume Parser")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    text = extract_text(uploaded_file)
    data = parse_resume(text)
    st.subheader("Extracted Data:")
    st.json(data)

    df = pd.DataFrame([data])
    st.download_button("Download CSV", df.to_csv(index=False), "resume.csv")
