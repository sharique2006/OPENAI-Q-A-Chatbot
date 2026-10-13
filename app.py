
import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With OPENAI"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant . Please  repsonse to the user queries"),
        ("user", "Question:{question}")
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens):
    openai.api_key = api_key

    llm = ChatOpenAI(model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer


# ---------------- UI DESIGN ----------------

st.set_page_config(
    page_title="Enhances Q %  Chatbot With OPENAI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

/* Main application background */
.stApp {
    background: linear-gradient(135deg, #0b1120 0%, #111827 55%, #172554 100%);
    color: #f1f5f9;
}

/* Main content spacing */
.block-container {
    max-width: 1050px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Hide default Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main heading */
.hero-title {
    font-size: 43px;
    font-weight: 800;
    text-align: center;
    letter-spacing: -1.5px;
    color: #ffffff;
    margin-bottom: 8px;
}

.hero-title span {
    background: linear-gradient(90deg, #818cf8, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    text-align: center;
    font-size: 16px;
    color: #94a3b8;
    margin-bottom: 35px;
}

/* Hero icon */
.hero-icon {
    text-align: center;
    font-size: 48px;
    margin-bottom: 8px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #0f172a);
    border-right: 1px solid #263449;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #f8fafc;
}

/* Input fields */
.stTextInput input {
    background-color: #111c30 !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 14px !important;
}

.stTextInput input:focus {
    border-color: #818cf8 !important;
    box-shadow: 0 0 0 1px #818cf8 !important;
}

/* Input labels */
.stTextInput label {
    color: #cbd5e1 !important;
    font-weight: 600;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #111c30;
    border-color: #334155;
    border-radius: 10px;
    color: #f8fafc;
}

/* Slider labels */
.stSlider label {
    color: #cbd5e1 !important;
}

/* Information cards */
.info-card {
    background: rgba(30, 41, 59, 0.65);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 22px;
}

.card-heading {
    font-size: 18px;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 8px;
}

.card-description {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.7;
}

/* Response card */
.response-card {
    background: linear-gradient(
        145deg,
        rgba(30, 41, 59, 0.95),
        rgba(23, 37, 84, 0.75)
    );
    border: 1px solid #475569;
    border-left: 4px solid #818cf8;
    border-radius: 16px;
    padding: 25px;
    margin-top: 25px;
    color: #e2e8f0;
    line-height: 1.8;
    font-size: 16px;
    overflow-wrap: anywhere;
}

/* Status messages */
.stAlert {
    border-radius: 12px;
}

/* Divider */
hr {
    border-color: #334155;
    margin-top: 25px;
    margin-bottom: 25px;
}

/* Footer */
.custom-footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 45px;
}

/* Responsive heading */
@media (max-width: 640px) {
    .hero-title {
        font-size: 32px;
    }

    .block-container {
        padding-top: 1.5rem;
    }
}

</style>
""", unsafe_allow_html=True)


# ---------------- APP TITLE ----------------

st.markdown("""
<div class="hero-icon">🤖</div>
<div class="hero-title">AI <span>Q&A Chatbot</span></div>
<div class="hero-subtitle">
    Your intelligent assistant, powered by OpenAI and LangChain.
    Ask questions and explore ideas.
</div>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR SETTINGS ----------------

st.sidebar.markdown("## ⚙️ Settings")
st.sidebar.markdown(
    "<p style='color:#94a3b8;font-size:13px;'>"
    "Configure your AI assistant below."
    "</p>",
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

api_key = st.sidebar.text_input(
    "🔑 OpenAI API Key",
    type="password",
    placeholder="Enter your API key"
)

st.sidebar.markdown("### 🧠 Model Configuration")

engine = st.sidebar.selectbox(
    "Select OpenAI model",
    ["gpt-4o", "gpt-4-turbo", "gpt-4"]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=50,
    max_value=300,
    value=150
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="
    background:rgba(30,41,59,0.7);
    border:1px solid #334155;
    border-radius:12px;
    padding:15px;
">
    <div style="color:#a5b4fc;font-weight:700;">
        ✨ AI Assistant
    </div>
    <div style="color:#94a3b8;font-size:12px;margin-top:6px;">
        Powered by OpenAI · LangChain · LangSmith
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------- MAIN INTERFACE ----------------

st.markdown("""
<div class="info-card">
    <div class="card-heading">💬 Start a Conversation</div>
    <div class="card-description">
        Ask a question, learn something new, or get help with a topic.
        Enter your message below to get started.
    </div>
</div>
""", unsafe_allow_html=True)

user_input = st.text_input(
    "Your question",
    placeholder="e.g. Explain LangChain in simple terms...",
    label_visibility="visible"
)

if user_input and api_key:
    with st.spinner("🤖 Generating your answer..."):
        response = generate_response(
            user_input, api_key, engine, temperature, max_tokens
        )

    st.markdown("""
    <div style="
        font-size:22px;
        font-weight:700;
        color:#f8fafc;
        margin-top:30px;
        margin-bottom:12px;
    ">
        ✨ AI Response
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="response-card">{response}</div>',
        unsafe_allow_html=True
    )

elif user_input:
    st.warning("🔑 Please enter your OpenAI API key in the sidebar.")

else:
    st.markdown("""
    <div class="info-card">
        <div class="card-heading">🚀 Ready when you are</div>
        <div class="card-description">
            Your conversation starts here. Enter your API key in the sidebar,
            type a question, and let your AI assistant help you.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="custom-footer">
    Built with Streamlit, OpenAI & LangChain
    <br>
    Intelligent conversations, simplified.
</div>
""", unsafe_allow_html=True)
