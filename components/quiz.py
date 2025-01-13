import streamlit as st
import random

# Quiz questions database
QUIZ_DATABASE = {
    "python_basics": [
        {
            "question": "What is the output of: print(type(5))?",
            "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'number'>"],
            "correct": "<class 'int'>",
            "explanation": "In Python, 5 is an integer, so type(5) returns <class 'int'>"
        },
        {
            "question": "Which of these is a mutable data type in Python?",
            "options": ["list", "tuple", "string", "int"],
            "correct": "list",
            "explanation": "Lists are mutable, meaning they can be changed after creation. Tuples and strings are immutable."
        },
        {
            "question": "What does the 'len()' function return for a string?",
            "options": ["Number of characters", "Memory size", "String hash", "Unicode value"],
            "correct": "Number of characters",
            "explanation": "len() returns the number of characters in a string, including spaces and special characters."
        }
    ],
    "python_intermediate": [
        {
            "question": "What is a decorator in Python?",
            "options": [
                "A function that modifies another function",
                "A class attribute",
                "A type of loop",
                "A string format"
            ],
            "correct": "A function that modifies another function",
            "explanation": "Decorators are functions that modify the behavior of another function or class."
        },
        {
            "question": "What is the purpose of __init__ method?",
            "options": [
                "Constructor method",
                "Destructor method",
                "Iterator method",
                "Import method"
            ],
            "correct": "Constructor method",
            "explanation": "__init__ is a constructor method that initializes new object instances in a class."
        }
    ]
}

def init_quiz():
    """Initialize quiz session state"""
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False
    if "current_topic" not in st.session_state:
        st.session_state.current_topic = "python_basics"

def reset_quiz():
    """Reset quiz state"""
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False

def show_quiz():
    """Display quiz interface"""
    init_quiz()
    
    st.subheader("🧪 Programming Quiz")
    
    # Topic selector
    topic = st.selectbox(
        "Select Quiz Topic",
        options=list(QUIZ_DATABASE.keys()),
        format_func=lambda x: x.replace("_", " ").title(),
        key="quiz_topic"
    )
    
    if topic != st.session_state.current_topic:
        st.session_state.current_topic = topic
        reset_quiz()
    
    questions = QUIZ_DATABASE[topic]
    
    if not st.session_state.quiz_complete:
        current_q = questions[st.session_state.current_question]
        
        # Display progress
        st.progress((st.session_state.current_question + 1) / len(questions))
        st.write(f"Question {st.session_state.current_question + 1} of {len(questions)}")
        
        # Display question
        st.markdown(f"**{current_q['question']}**")
        
        # Display options and handle answer
        answer = st.radio("Select your answer:", current_q["options"], key=f"q_{st.session_state.current_question}")
        
        if st.button("Submit Answer"):
            if answer == current_q["correct"]:
                st.success("Correct! " + current_q["explanation"])
                st.session_state.score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {current_q['correct']}\n{current_q['explanation']}")
            
            # Move to next question or complete quiz
            if st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1
                st.experimental_rerun()
            else:
                st.session_state.quiz_complete = True
                st.experimental_rerun()
    
    else:
        # Show quiz completion message and score
        final_score = (st.session_state.score / len(questions)) * 100
        st.success(f"Quiz Complete! Your score: {final_score:.1f}%")
        
        if final_score == 100:
            st.balloons()
            st.markdown("🎉 Perfect score! Excellent work!")
        elif final_score >= 70:
            st.markdown("👏 Well done! Keep practicing!")
        else:
            st.markdown("📚 Keep learning! Try reviewing the topics and attempt the quiz again.")
        
        if st.button("Restart Quiz"):
            reset_quiz()
            st.experimental_rerun() 