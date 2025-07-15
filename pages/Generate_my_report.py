import streamlit as st
from nodes.report_manager import ReportManager

# Set page to full width
# st.set_page_config(layout="wide")

for key, value in [
    ("enable_feedback", False),
    ("user_input", ""), 
    ("content", "")]:
    if key not in st.session_state:
        st.session_state[key] = value

st.title("AI Report Generator")

with st.container(border=True):
    st.markdown("Generate comprehensive research reports on any topic using **Agentic-AI-powered-workflows.** Simply enter your research question below and our intelligent system will plan, research, and synthesize a detailed report for you.")
    st.image("static/images/home_page.jpeg")

manager = ReportManager()

output_placeholder = st.empty()

def handle_output(contents):
    for content in contents:
        if content == "__interrupt__":
            st.session_state.enable_feedback = True
            break
        st.session_state.content += content
        output_placeholder.markdown(st.session_state.content)

if prompt := st.chat_input("Enter your query here..."):
    if st.session_state.enable_feedback:
        contents = manager.resume(prompt)
    else:
        contents = manager.run(prompt)    
    handle_output(contents)