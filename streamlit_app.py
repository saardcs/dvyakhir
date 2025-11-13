import streamlit as st

st.set_page_config(page_title="My Streamlit Projects", layout="wide")

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>✨ My Streamlit Portfolio</h1>
    <p>Interactive apps • Data • AI • Design</p>
</div>
""", unsafe_allow_html=True)

# Project data
projects = [
    {
        "title": "AI Art Generator",
        "desc": "Turn text prompts into unique images using diffusion models.",
        "img": "assets/project1.png",
        "url": "https://your-ai-art.streamlit.app"
    },
    {
        "title": "Finance Dashboard",
        "desc": "Visualize and analyze market trends in real-time.",
        "img": "assets/project2.png",
        "url": "https://your-stock.streamlit.app"
    },
    {
        "title": "Chatbot Assistant",
        "desc": "Conversational AI built with Streamlit + LangChain.",
        "img": "assets/project3.png",
        "url": "https://your-chatbot.streamlit.app"
    },
]

# Gallery layout
cols = st.columns(3)
for i, project in enumerate(projects):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card" onclick="window.open('{project['url']}', '_blank')">
                <div class="card-image" style="background-image: url('{project['img']}');"></div>
                <div class="card-content">
                    <h3>{project['title']}</h3>
                    <p>{project['desc']}</p>
                    <div class="button">View Project 🚀</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
