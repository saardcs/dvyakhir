import streamlit as st

# Page setup
st.set_page_config(page_title="My Streamlit Projects", layout="wide")
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');</style>", unsafe_allow_html=True)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>🚀 My Streamlit Projects</h1>
    <p>Clean design • Smooth animations • Built with ❤️ in Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Project data
projects = [
    {
        "title": "AI Art Generator",
        "desc": "Generate stunning AI art using diffusion models and text prompts.",
        "img": "assets/project1.png",
        "url": "https://your-ai-art.streamlit.app"
    },
    {
        "title": "Financial Dashboard",
        "desc": "Track and visualize live market data with custom analytics.",
        "img": "assets/project2.png",
        "url": "https://your-stock.streamlit.app"
    },
    {
        "title": "AI Chat Assistant",
        "desc": "Conversational chatbot built with LangChain and Streamlit.",
        "img": "assets/project3.png",
        "url": "https://your-chatbot.streamlit.app"
    },
]

# Gallery
cols = st.columns(3)
for i, project in enumerate(projects):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card" onclick="window.open('{project['url']}', '_blank')">
                <div class="card-image" style="background-image: url('{project['img']}');"></div>
                <div class="card-overlay">
                    <h3>{project['title']}</h3>
                    <p>{project['desc']}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
