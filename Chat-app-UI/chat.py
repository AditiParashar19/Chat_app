import streamlit as st
from chat_logic import main

st.set_page_config("Chatbot")
st.title("Intellichat")
st.write("Chatbot for news, weather , cricket, location , open any website ")

user_input = st.text_input("Enter your message : ")

if("chat_history" not in st.session_state):  #chat and response both save in history
    st.session_state.chat_history = []

if(st.button("send")):      # handle button click
    if(user_input.strip() != ""):    #check if text box is not empty
        st.session_state.chat_history.append(("Aditi",user_input)) #storing in session what user input is
        response = main(user_input)
        st.session_state.chat_history.append(("Intellichat",response))
for sender,message in st.session_state.chat_history:
    if(sender=="Aditi"):
        st.markdown(f"**Aditi:** {message}")
    else:
        st.markdown(f"**IntelliChat:** {message}")


