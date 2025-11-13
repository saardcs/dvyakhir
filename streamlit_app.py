import streamlit as st
import base64
from streamlit_extras.carousel import carousel

st.set_page_config(page_title="My Streamlit Projects", layout="wide")

# --- Convert image to base64 ---
def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Load CSS ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="header">
    <h1>🎨 My Streamlit Portfolio</h1>
    <p>Beautifully crafted interactive apps built with Streamlit</p>
</div>
""", unsafe_allow_html=True)

# --- Projects ---
projects = [
    {
        "title": "AI Art Generator",
        "desc": "Generate unique visuals from text prompts using diffusion models.",
        "img": "assets/project1.png",
        "url": "https://your-ai-art.streamlit.app"
    },
    {
        "title": "Financial Dashboard",
        "desc": "Explore live market analytics and trends with interactive charts.",
        "img": "assets/project2.png",
        "url": "https://your-stock.streamlit.app"
    },
    {
        "title": "Chatbot Assistant",
        "desc": "Conversational AI interface powered by LangChain and Streamlit.",
        "img": "assets/project3.png",
        "url": "https://your-chatbot.streamlit.app"
    },
]

# --- Prepare carousel items with overlay HTML ---
carousel_items = []
for project in projects:
    img_base64 = get_base64_image(project["img"])
    html = f"""
    <div class="carousel-card">
        <img src="data:image/png;base64,{img_base64}" class="card-img">
        <div class="card-overlay">
            <h3>{project['title']}</h3>
            <p>{project['desc']}</p>
            <a href="{project['url']}" target="_blank" class="button">View Project 🚀</a>
        </div>
    </div>
    """
    carousel_items.append({"image": html, "caption": ""})  # caption empty; overlay handles it

# --- Display carousel ---
carousel(
    carousel_items,
    height=450,
    auto_play=False,
    hide_indicators=False
)
