import streamlit as st

RESOURCES_DATABASE = {
    "Python Basics": {
        "Official Documentation": {
            "Python Official Docs": "https://docs.python.org/3/",
            "Python Tutorial": "https://docs.python.org/3/tutorial/",
        },
        "Free Courses": {
            "Codecademy Python": "https://www.codecademy.com/learn/learn-python-3",
            "W3Schools Python": "https://www.w3schools.com/python/",
            "Real Python": "https://realpython.com/",
        },
        "Practice Platforms": {
            "LeetCode": "https://leetcode.com/",
            "HackerRank": "https://www.hackerrank.com/domains/python",
            "CodeWars": "https://www.codewars.com/",
        }
    },
    "Web Development": {
        "Frontend": {
            "MDN Web Docs": "https://developer.mozilla.org/",
            "W3Schools HTML/CSS": "https://www.w3schools.com/html/",
            "JavaScript.info": "https://javascript.info/",
        },
        "Backend": {
            "Django Documentation": "https://docs.djangoproject.com/",
            "Flask Documentation": "https://flask.palletsprojects.com/",
            "FastAPI Documentation": "https://fastapi.tiangolo.com/",
        }
    },
    "Data Science": {
        "Libraries": {
            "NumPy Documentation": "https://numpy.org/doc/",
            "Pandas Documentation": "https://pandas.pydata.org/docs/",
            "Matplotlib Documentation": "https://matplotlib.org/stable/index.html",
        },
        "Courses": {
            "Kaggle Learn": "https://www.kaggle.com/learn",
            "DataCamp": "https://www.datacamp.com/",
        }
    }
}

def show_resources():
    """Display learning resources section"""
    st.title("📚 Learning Resources")
    
    # Resource category selector
    category = st.selectbox(
        "Select Category",
        options=list(RESOURCES_DATABASE.keys()),
        key="resource_category"
    )
    
    # Display resources for selected category
    if category:
        for section, resources in RESOURCES_DATABASE[category].items():
            with st.expander(f"📖 {section}", expanded=True):
                for name, url in resources.items():
                    st.markdown(f"- [{name}]({url})")
        
        # Additional tips based on category
        st.markdown("---")
        st.subheader("💡 Learning Tips")
        
        if category == "Python Basics":
            st.info("""
            - Start with simple programs
            - Practice coding daily
            - Use Python's interactive shell
            - Join Python communities
            - Work on small projects
            """)
        elif category == "Web Development":
            st.info("""
            - Build responsive layouts
            - Learn browser developer tools
            - Practice with real projects
            - Stay updated with new technologies
            - Test across different browsers
            """)
        elif category == "Data Science":
            st.info("""
            - Master pandas and numpy
            - Practice data visualization
            - Work with real datasets
            - Participate in Kaggle competitions
            - Learn statistical concepts
            """) 