
import streamlit as st
from similarity_checker import get_similarity_score
from fact_check_api import get_fact_checked_sources

st.title("📰 News Authenticity Checker")

user_input = st.text_area("Paste a news article or headline")

if st.button("Check Credibility"):
    with st.spinner("Analyzing..."):
        score, verdict = get_similarity_score(user_input)
        sources = get_fact_checked_sources(user_input)

    st.markdown(f"### 🧠 Credibility Score: **{score:.2f}/1.0**")
    st.markdown(f"### ✅ Verdict: **{verdict}**")

    if sources:
        st.markdown("#### 🗞️ Verified Sources Found:")
        for source in sources:
            st.write(f"- [{source['title']}]({source['url']})")
    else:
        st.warning("No verified sources found.")
