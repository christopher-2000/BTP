from sidebar import*
from main_page import*
from CBF import *

# Display Content on the sidebar
st.write("""
    # University Recommendation System
    ### Btech Project - Group 13  
    """)
st.info(" <<<< Edit Your Scores in sidebar and Press Recommend Button ")

sidebar()
#Display Content on the right side
display_top()
search_college()

