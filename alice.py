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

# Encode both images to base64 strings.
encoded_image_1 = get_base64_image(image_path_1)
encoded_image_2 = get_base64_image(image_path_2)

# HTML code that displays the image with an overlay clickable area.
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Container to hold the image and position the clickable area relative to it */
    .container {{
      position: relative;
      display: inline-block;
    }}
    /* Clickable area overlay positioned over the image */
    .clickable-area {{
      position: absolute;
      top: 203px;         /* Distance from the top of the container */
      left: 262px;       /* Distance from the left of the container */
      width: 72px;      /* Width of the clickable area */
      height: 23px;     /* Height of the clickable area */
      cursor: pointer;   /* Change the mouse pointer to indicate clickable area */
      border: 2px solid red; /* Red border to visually identify the clickable area */
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- Display the image using the base64 encoded string -->
    <img id="game-image" src="data:image/png;base64,{encoded_image_1}" width="600" alt="Clickable Image">
    <!-- Div element that acts as the clickable overlay area -->
    <div class="clickable-area" onclick="changeImage()"></div>
  </div>
  <script>
    // Function to change the image when the clickable area is clicked.
    function changeImage() {{
      // Change the source of the image to the second image.
      document.getElementById('game-image').src = "data:image/png;base64,{encoded_image_2}";
    }}
  </script>
</body>
</html>
"""

# Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)
