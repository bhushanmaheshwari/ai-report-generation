import streamlit as st

st.markdown("<div style='text-align: center; margin-bottom:20px'><h1>📚 AI Report Generator</h1></div>", unsafe_allow_html=True)

st.subheader("Let's get started!", divider="grey")

with st.form("input_form", border=0):
    user_input = st.text_area("📌 Enter your topic here", placeholder="e.g., Impact of WBG DPI in Lower and Middle Income countries...")
    submitted = st.form_submit_button("Generate Report")
    if submitted:
        st.session_state.generating = True
        st.rerun()

if st.session_state.generating:
    progress_placeholder = st.empty()
    progress_messages = []
    expander_header = "Thinking..."
    expander_open = True

    config = {"configurable": {"thread_id": "1"}}
    events = orchestrator_worker.stream(
        {"topic": user_input},
        config,
    )
    
    for event in events:
        if "orchestrator" in event:
            sections_text = "*Preparing: Layout of the report*"
            progress_messages.append(sections_text)
        
        elif "worker" in event:
            progress_messages.append(
                f"*Working on: {event['worker']['section_summaries']}*"
            )

        elif "synthesizer" in event:
            # progress_messages.append("✅ **Report complete!**")
            st.markdown(event["synthesizer"]["final_report"])
            expander_header = "Report generation complete!"
            expander_open = False

        with progress_placeholder.expander(expander_header, expanded=expander_open):
            for msg in progress_messages:
                st.markdown(msg, unsafe_allow_html=True)
