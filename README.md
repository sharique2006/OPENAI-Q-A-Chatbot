# OPENAI-Q-A-Chatbot
An interactive AI-powered Question &amp; Answer chatbot built with Streamlit, OpenAI, and LangChain. The application allows users to ask questions and receive AI-generated responses through a clean, modern interface with customizable model settings.

Features

AI-Powered Responses: Generate answers using OpenAI language models.

Multiple Models: Choose between GPT-4o, GPT-4 Turbo, and GPT-4.

Customizable Settings: Adjust temperature and maximum token settings through the sidebar.

Secure API Key Input: Enter your OpenAI API key through a password-protected input field.

LangChain Integration: Use prompt templates and output parsers to manage the LLM pipeline.

LangSmith Tracking: Enable tracing to monitor application runs.

Modern UI: Dark-themed interface with gradient headings, styled input fields, and response cards.

🛠️ Tech Stack

Technology

Purpose

Python

Core programming language

Streamlit

Web application interface

OpenAI

Large language model API

LangChain

LLM integration and prompt management

LangSmith

LLM tracing and monitoring

python-dotenv

Environment variable management

📁 Project Structure

AI-QA-Chatbot/
│
├── app.py              # Main Streamlit application
├── .env                # Environment variables (not committed)
├── .env.example        # Example environment configuration
├── .gitignore          # Files excluded from Git
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

Replace the repository URL with your actual GitHub repository URL.

2. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

On macOS or Linux:

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root:

LANGCHAIN_API_KEY=your_langsmith_api_key

Obtain your LangSmith API key from LangSmith.

The OpenAI API key is entered directly into the application's sidebar when you run the chatbot. You can obtain an API key from the OpenAI Platform.

Security: Never commit your actual API keys or .env file to GitHub.

5. Run the application

streamlit run app.py

Open the local URL displayed in your terminal, usually:

http://localhost:8501

🚀 How to Use

Launch the application.

Enter your OpenAI API key in the sidebar.

Select an OpenAI model.

Adjust the temperature and maximum token settings as needed.

Enter your question in the input field.

View the AI-generated response.

🔍 LangSmith Monitoring

The application enables LangSmith tracing to help monitor LLM interactions.

The project is configured with the following tracking settings:

LANGCHAIN_TRACING_V2: Enables tracing.

LANGCHAIN_API_KEY: Authenticates with LangSmith.

LANGCHAIN_PROJECT: Names the tracing project.

You can view traced runs in your LangSmith dashboard.

📦 Requirements

Create a requirements.txt file containing:

streamlit
openai
langchain-openai
langchain-core
python-dotenv

Install the packages using:

pip install -r requirements.txt

🔮 Future Improvements

Chat history and multi-turn conversations.

Support for additional LLM providers.

Streaming responses.

Export conversations to text or PDF.

Improved error handling and API usage feedback.

Deployment on Streamlit Community Cloud.

⚠️ Notes

An active OpenAI API account with API access and available quota is required.

API usage may incur charges depending on the selected model and account.

The temperature and maximum token controls are currently displayed in the UI; they need to be connected to the model configuration to affect generated responses.

Keep all API keys private.
