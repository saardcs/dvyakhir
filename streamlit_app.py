import streamlit as st
import base64

st.set_page_config(page_title="My Streamlit Projects", layout="wide")

def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>🎨 My Streamlit Portfolio</h1>
    <p>Beautifully crafted interactive apps built with Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Projects
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

# Gallery
cols = st.columns(3)
for i, project in enumerate(projects):
    with cols[i % 3]:
        img_base64 = get_base64_image(project["img"])
        st.markdown(f"""
        <div class="card">
            <img src="data:image/png;base64,{img_base64}" class="card-img">
            <div class="card-overlay">
                <h3>{project['title']}</h3>
                <p>{project['desc']}</p>
                <a href="{project['url']}" target="_blank" class="button">View Project 🚀</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
