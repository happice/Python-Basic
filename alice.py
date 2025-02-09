# To run, copy and paste the code below.
# streamlit run alice.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/
import streamlit as st

st.title("The Evil Coding Teacher")
st.write("Elena is a talented coder that goes to CIT coding acedemy with 5 of her friends. One Sunday morning, everybody else expept Elena Choi was at room 3 waiting for Elena to come.However, the coding teacher looked suspicious. The other 5 friends, Eugenia, Eiley, Yuna and Alice found out that the teacher had kidnapped her...")

# background-color: #a8d5ba;
#background-size: cover;
#background: url(...)

response = st.text_input("Do you think the coding teacher is mean? Say 'Yes' or 'No'")
st.write(response)

if response.lower()== 'yes' :
  st.success("You are CORRECT!")
elif response.lower() == 'no':
    st.error("You are WRONG!")
