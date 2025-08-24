import re
import random
from urllib.parse import urlparse
import streamlit as st

# Page setup
st.set_page_config(page_title="My Roblox Links Dashboard", page_icon="🎮", layout="wide")

# 🎨 Custom background color
page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f0f4ff; /* light blue background */
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0); /* remove top bar background */
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Centered title
st.markdown("<h1 style='text-align: center;'>🎮 My Roblox Links Dashboard</h1>", unsafe_allow_html=True)

# Roblox links
LINKS = [
    "https://www.roblox.com/games/920587237/Adopt-Me",
    "https://www.roblox.com/games/286090429/Arsenal",
    "https://www.roblox.com/games/126884695634066/Grow-a-Garden",
    "https://www.roblox.com/games/17625359962/RIVALS",
    "https://www.roblox.com/games/2753915549/UPDATE-Blox-Fruits",
    "https://www.roblox.com/games/116495829188952/Dead-Rails-Alpha",
    "https://www.roblox.com/games/15101393044/LADY-GAGA-Dress-To-Impress",
    "https://www.roblox.com/games/10449761463/The-Strongest-Battlegrounds",
    "https://www.roblox.com/games/16116270224/Dandys-World-ALPHA",
    "https://www.roblox.com/games/5985232436/Infectious-Smile-SUMMER",
]

# Extract game name from Roblox link
def extract_name(url: str) -> str:
    try:
        path = urlparse(url).path.strip("/")
        parts = path.split("/")
        if len(parts) >= 3 and parts[0].lower() == "games":
            return parts[2].replace("-", " ")
        return parts[-1].replace("-", " ") if parts else url
    except Exception:
        return url

# 🎲 Random Game Button -> opens in new tab
if st.button("🎲 Pick a Random Game"):
    random_link = random.choice(LINKS)
    random_name = extract_name(random_link)
    st.success(f"Your random game is: **{random_name}**")

    # Open the link in a new tab automatically
    js = f"window.open('{random_link}');"
    st.components.v1.html(f"<script>{js}</script>", height=0, width=0)

# 🔍 Search Bar
query = st.text_input("Search for a game:")
filtered_links = [link for link in LINKS if query.lower() in extract_name(link).lower()] if query else LINKS

# Display game cards
if not LINKS:
    st.info("Add Roblox game links to the LINKS list at the top of the code.")
else:
    cols_per_row = 3
    for i in range(0, len(filtered_links), cols_per_row):
        cols = st.columns(cols_per_row)
        for col, link in zip(cols, filtered_links[i:i+cols_per_row]):
            name = extract_name(link)
            with col:
                st.markdown(
                    f"""
                    <div style="display:flex;flex-direction:column;
                                justify-content:center;align-items:center;
                                width:100%;height:200px;border:2px solid #ccc;
                                border-radius:12px;box-shadow:2px 2px 6px rgba(0,0,0,0.1);
                                background:white; transition:0.2s;">
                        <div style="font-size:16px;font-weight:bold;color:#333;margin-bottom:8px;">
                            {name}
                        </div>
                        <a href="{link}" target="_blank"
                           style="padding:8px 16px;border-radius:8px;
                                  background-color:#e8ffe8;color:white;
                                  text-decoration:none;font-weight:bold;">
                            Open Game
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
