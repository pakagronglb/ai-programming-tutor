import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def init_chat(agent_id: str = None):
    """Initialize chat session state"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add initial system message
        st.session_state.messages.append({
            "role": "system",
            "content": """You are an expert AI programming tutor. Your goal is to help students learn programming concepts effectively.
            Follow these guidelines:
            1. Be patient and encouraging
            2. Break down complex concepts into simpler parts
            3. Provide examples when explaining concepts
            4. Ask questions to check understanding
            5. Suggest exercises for practice
            6. Use proper code formatting when sharing code examples"""
        })

def show_chat(prompt_placeholder: str = "What would you like to learn about?"):
    """Display chat interface"""
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] != "system":  # Don't show system messages
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input(prompt_placeholder):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # Get response from OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages,
                stream=True,
                temperature=0.7,
                max_tokens=2000
            )

            # Stream the response
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
