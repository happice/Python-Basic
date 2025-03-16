# To run, copy and paste the code below.
# streamlit run alice.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/
import streamlit as st

st.title("Save the Forest")

description = """
This game is based on SDGs 15 which is, Life on Land.   
The main idea of the game is to save the forest and make the air quality better for humans and animals living on land. 
The player will have to collect trees instead of factories, however if they do get the factory, they will have 3 lives. 
If they use all 3, they will be eliminated from the game. 
"""
st.write(description)


# The player had to collect trees to plant, however if you get a factory 3 times, you get eliminated. 

st.image("1.png")