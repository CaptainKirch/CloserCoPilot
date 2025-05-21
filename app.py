import streamlit as st
from analyzer import analyze_transcript

st.set_page_config(page_title="Closer Copilot", layout="wide")
st.title("🤖 Closer Copilot")
st.markdown("Upload your sales call transcript and get an AI-powered breakdown.")

uploaded_file = st.file_uploader("📄 Upload a transcript (.txt)", type="txt")

if uploaded_file:
    transcript_text = uploaded_file.read().decode("utf-8")
    
    st.subheader("📜 Transcript Preview")
    st.text_area("Raw Transcript", transcript_text, height=300)

    if st.button("🔍 Analyze Transcript"):
        with st.spinner("Analyzing..."):
            report = analyze_transcript(transcript_text)
            st.subheader("🧠 Call Analysis Report")
            st.markdown(report)
