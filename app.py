import streamlit as st
from agent import run_research_agent

st.set_page_config(page_title="AI Agent Intelligence Lab", layout="centered")
st.title("🤖 AI Agent Intelligence Lab")
st.write("Orchestrate a team of free autonomous agents to crawl the web and build analytical reports.")

# User entry target field
topic = st.text_input("Enter your research topic:", placeholder="e.g., Next-generation solar cell developments")

if st.button("Launch Research Team"):
    if topic:
        with st.spinner("Agents are scanning web indexes and generating reports..."):
            try:
                # Direct invocation to our structural worker framework
                report = run_research_agent(topic)
                st.success("Analysis Complete!")
                st.markdown("### 📊 Compiled Intelligence Report")
                st.markdown(report)
            except Exception as e:
                st.error(f"Operational constraint encountered: {e}")
    else:
        st.warning("Please specify a target focus topic.")
