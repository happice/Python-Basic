# To run, copy and paste the code below.
# streamlit run alice.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/


import streamlit as st
import base64

st.title("Save the Forest")

description = """
This game is based on SDGs 15 which is, Life on Land.   
The main idea of the game is to save the forest and make the air quality better for humans and animals living on land. 
The player will have to collect trees instead of factories, however if they do get the factory, they will have 3 lives. 
If they use all 3, they will be eliminated from the game. 
"""
st.write(description)


# The player had to collect trees to plant, however if you get a factory 3 times, you get eliminated. 

# Function to convert an image file to a base64 encoded string.
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# Paths to the image files.
image_path_1 = "1.png"  # Path to the first image.
image_path_2 = "2.png"  # Path to the second image.
image_path_3 = "3.png"

# Encode both images to base64 strings.
encoded_image_1 = get_base64_image(image_path_1)
encoded_image_2 = get_base64_image(image_path_2)
encoded_image_3 = get_base64_image(image_path_3)

# HTML code that displays the image with an overlay clickable area.
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      display: inline-block;
    }}
    .clickable-area {{
      position: absolute;
      top: 203px;
      left: 262px;
      width: 72px;
      height: 23px;
      cursor: pointer;
      border: 2px solid red;
    }}
    #game-image {{
      width: 600px;
      cursor: pointer;
    }}
  </style>
</head>
<body>
  <div class="container" onclick="handleImageClick()">
    <img id="game-image" src="data:image/png;base64,{encoded_image_1}" alt="Game Image">
    <div id="clickableArea" class="clickable-area" onclick="handleBoxClick(event)"></div>
  </div>

  <script>
    let currentStage = 1;

    function handleBoxClick(event) {{
      event.stopPropagation(); // Prevents the parent container click
      document.getElementById("game-image").src = "data:image/png;base64,{encoded_image_2}";
      document.getElementById("clickableArea").style.display = "none";
      currentStage = 2;
    }}

    function handleImageClick() {{
      if (currentStage === 2) {{
        document.getElementById("game-image").src = "data:image/png;base64,{encoded_image_3}";
        currentStage = 3;
      }}
    }}
  </script>
</body>
</html>
"""

# Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)
