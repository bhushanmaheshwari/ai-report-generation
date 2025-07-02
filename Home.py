import streamlit as st
from workflow import orchestrator_worker
    
if "generating" not in st.session_state:
    st.session_state.generating = False

st.markdown("<div style='text-align: center; margin-bottom:20px'><h1>📚 AI Report Generator</h1></div>", unsafe_allow_html=True)

st.write("""
A powerful, AI-driven application that generates comprehensive AI reports on any topic, leveraging the latest LLMs and a multi-step workflow orchestration. Built with LangGraph, LangChain, and Streamlit.
""")

st.image("https://langchain-ai.github.io/langgraph/tutorials/workflows/img/worker.png", caption="")

st.markdown("---")

st.subheader("🚀 Features")
st.markdown("""
- **Automated AI Report Generation**: Enter any topic and receive a structured, scholarly AI report.
- **Section Planning**: The app intelligently breaks down your topic into logical sections, each with a clear description.
- **AI-Powered Writing**: Each section is written by an LLM, with citations and scholarly tone.
- **Seamless Orchestration**: Uses a multi-step workflow (orchestrator, workers, synthesizer) for modular, extensible report generation.
- **Modern UI**: Clean, interactive Streamlit interface for easy use.
""")

st.markdown("---")

st.subheader("🛠️ How It Works")
st.markdown("""
1. **Input**: Enter your topic.
2. **Planning**: The orchestrator LLM creates a report outline with section names and descriptions.
3. **Writing**: Each section is written by a dedicated LLM worker, with citations and markdown formatting.
4. **Synthesis**: All sections are combined into a final, ready-to-use AI report.
""")

st.markdown("---")

st.subheader("⚡ Quickstart")
st.markdown("""
1. **Clone the repo**
   ```bash
   git clone https://github.com/bhushanmaheshwari/ai-report-generation.git
   cd ai-report-generation
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables**
   Create a `.env` file with your API keys (e.g., for Google Generative AI).
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```
4. **Run the app**
   ```bash
   streamlit run Home.py
   ```
""")

st.markdown("---")

st.subheader("✨ Why Use This?")
st.markdown("""
- **Save hours** on report writing.
- **Get structured, scholarly content** with citations.
- **Flexible and extensible** for research, academia, or business.
""")

