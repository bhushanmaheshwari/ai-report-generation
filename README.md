# 📚 AI Report Generation

A powerful, AI-driven application that generates comprehensive AI reports on any topic, leveraging the latest LLMs and a multi-step workflow orchestration. Built with [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and [Streamlit](https://streamlit.io/).

![Demo Screenshot](https://langchain-ai.github.io/langgraph/tutorials/workflows/img/worker.png)


## 🚀 Features

- **Automated AI Report Generation**: Enter any topic and receive a structured, scholarly AI report.
- **Section Planning**: The app intelligently breaks down your topic into logical sections, each with a clear description.
- **AI-Powered Writing**: Each section is written by an LLM, with citations and scholarly tone.
- **Seamless Orchestration**: Uses a multi-step workflow (orchestrator, workers, synthesizer) for modular, extensible report generation.
- **Modern UI**: Clean, interactive Streamlit interface for easy use.


## 🛠️ How It Works

1. **Input**: Enter your topic.
2. **Planning**: The orchestrator LLM creates a report outline with section names and descriptions.
3. **Writing**: Each section is written by a dedicated LLM worker, with citations and markdown formatting.
4. **Synthesis**: All sections are combined into a final, ready-to-use AI report.


## 🏗️ Tech Stack

- **Python 3.10+**
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini Pro)](https://ai.google.dev/)
- [Pydantic](https://docs.pydantic.dev/)
- [dotenv](https://pypi.org/project/python-dotenv/)


## ⚡ Quickstart

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

## 🧠 Example Usage

1. Open the app in your browser.
2. Enter a topic, e.g., `Impact of WBG DPI in Lower and Middle Income countries`.
3. Watch as the app plans, writes, and synthesizes your AI report.
4. Copy or download your final report!


## ✨ Why Use This?

- **Save hours** on report writing.
- **Get structured, scholarly content** with citations.
- **Flexible and extensible** for research, academia, or business.


## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


## 📄 License

[MIT](LICENSE)


## 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)


> Made with ❤️ for researchers, students, and professionals.

