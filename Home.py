import streamlit as st
import sys
import os

# Import components
from components.chat import init_chat, show_chat
from components.quiz import show_quiz
from components.resources import show_resources

def show_roadmap():
    """Display the learning roadmap section"""
    st.subheader("🗺️ Learning Roadmap")
    
    # Beginner Path
    st.markdown("### 🌱 Beginner Path")
    with st.expander("1. Python Fundamentals", expanded=True):
        st.markdown("""
        - Variables and Data Types
        - Basic Operators
        - Control Flow (if/else)
        - Loops (for/while)
        - Functions
        - Basic Data Structures (lists, tuples, dictionaries)
        - File Handling
        """)
    
    # Intermediate Path
    st.markdown("### 🚀 Intermediate Path")
    with st.expander("2. Advanced Python Concepts"):
        st.markdown("""
        - Object-Oriented Programming
        - Exception Handling
        - Modules and Packages
        - List Comprehensions
        - Lambda Functions
        - Decorators
        - Generators
        """)
    
    # Advanced Topics
    st.markdown("### 💫 Advanced Path")
    with st.expander("3. Specialized Topics"):
        st.markdown("""
        - Web Development
            - HTML/CSS Basics
            - Flask/Django
            - RESTful APIs
        - Data Science
            - NumPy
            - Pandas
            - Data Visualization
        - Database
            - SQL Basics
            - Database Design
            - ORM Concepts
        """)
    
    # Projects Section
    st.markdown("### 🛠️ Project Ideas")
    with st.expander("Practice Projects"):
        st.markdown("""
        - Beginner Projects:
            - To-Do List Application
            - Calculator
            - Password Generator
        - Intermediate Projects:
            - Weather App
            - File Organizer
            - Simple Blog
        - Advanced Projects:
            - Social Media Dashboard
            - E-commerce Platform
            - Machine Learning Model
        """)

def init_session_state():
    """Initialize session state variables"""
    try:
        init_chat()
    except Exception as e:
        st.error(f"Error initializing session state: {str(e)}")

def main():
    try:
        # Page config
        st.set_page_config(
            page_title="AI Programming Tutor",
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="collapsed"  # This will collapse the sidebar
        )

        # Hide all Streamlit navigation and menus
        hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .css-1rs6os {visibility: hidden;}
        .css-17ziqus {visibility: hidden;}
        .css-1q1n0ol {visibility: hidden;}
        div[data-testid="stSidebarNav"] {display: none;}
        </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

        # Tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat", "🧪 Quiz", "🗺️ Roadmap", "📚 Resources"])
        
        with tab1:
            st.title("🤖 AI Programming Tutor")
            st.write("Welcome! I'm your personal programming tutor. Ask me anything about coding!")
            init_session_state()
            show_chat("What programming topic would you like to learn about?")
        
        with tab2:
            show_quiz()
        
        with tab3:
            show_roadmap()
        
        with tab4:
            show_resources()

    except Exception as e:
        st.error(f"Error in main: {str(e)}")
        st.write(f"Error type: {type(e)}")

if __name__ == "__main__":
    main()
