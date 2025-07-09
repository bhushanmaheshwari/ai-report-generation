import streamlit as st
from gen_tech_spec.workflow import chain
    
if "generating_tech_spec" not in st.session_state:
    st.session_state.generating_tech_spec = False

st.markdown("<div style='text-align: center; margin-bottom:20px'><h1>Let's get started!</h1></div>", unsafe_allow_html=True)
with st.form("input_form", border=0):
    user_input = st.text_area("📌 Enter your topic here", placeholder="e.g., An azure based web application for travel management system...", height=500)
    submitted = st.form_submit_button("Generate Technical Specification")
    if submitted:
        st.session_state.generating_tech_spec = True

if st.session_state.generating_tech_spec:
    config = {"configurable": {"thread_id": "1"}}
    events = chain.stream(
        {"topic": user_input},
        config
    )
   
    for event in events:
        
        if "topic" in event:
            st.title(event["topic"])
        
        elif "refine_requirements" in event:
            st.subheader("Requirements", divider="blue")
            st.markdown(event["refine_requirements"]["requirements"])

        elif "generate_tech_stack" in event:
            st.subheader("Components", divider="blue")
            st.markdown(event["generate_tech_stack"]["components"])
        
        elif "generate_code" in event:
            st.subheader("Code Generated", divider="blue")
            st.code(event["generate_code"]["code"])

        elif "execute_code" in event:
            st.subheader("Architecture Diagram", divider="blue")
            st.image(event["execute_code"]["diagram"])

        
        st.session_state.generating = False 

