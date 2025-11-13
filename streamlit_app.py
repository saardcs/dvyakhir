import streamlit as st
from streamlit_extras.let_it_rain import rain

# Page config
st.set_page_config(page_title="My Streamlit Gallery", layout="wide")

# Custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🎨 My Streamlit Projects Gallery")

# Optional: A little visual effect
rain(emoji="💻", font_size=20, falling_speed=5, animation_length="infinite")

# Project data
projects = [
    {
        "title": "AI Art Generator",
        "desc": "Create art from text prompts using diffusion models.",
        "img": "assets/project1.png",
        "url": "https://your-ai-art.streamlit.app"
    },
    {
        "title": "Stock Dashboard",
        "desc": "Interactive stock visualization with live data.",
        "img": "assets/project2.png",
        "url": "https://your-stock.streamlit.app"
    },
    {
        "title": "Chatbot Interface",
        "desc": "Conversational AI built with LangChain and Streamlit.",
        "img": "assets/project3.png",
        "url": "https://your-chatbot.streamlit.app"
    },
]

# Animated cards
cols = st.columns(3)
for i, project in enumerate(projects):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card">
                <img src="{project['img']}" class="card-img">
                <div class="card-content">
                    <h3>{project['title']}</h3>
                    <p>{project['desc']}</p>
                    <a href="{project['url']}" target="_blank" class="button">View Project 🚀</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
