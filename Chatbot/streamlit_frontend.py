import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend import chatbot

CONFIG={'configurable':{'thread_id':'thread-1'}}

if "message_history" not in st.session_state:
    st.session_state['message_history'] = []


# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])


user_input=st.chat_input("Type your message here...")

if user_input:

    # add message to history
    st.session_state['message_history'].append({"role": "User", "content": user_input})
    with st.chat_message('User'):
        st.text(user_input)

    initial_state={'messages':[HumanMessage(content=user_input)]}
    
    response=chatbot.invoke(initial_state,config=CONFIG)
    ai_message=response['messages'][-1].content

    st.session_state['message_history'].append({"role": "Assistant", "content": ai_message})
    with st.chat_message('Assistant'):
        st.text(ai_message)