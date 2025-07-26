import streamlit as st
from utils.utils import get_ai_response
from utils.db_manager import update_idea_by_id

# Predefined question
question = (
    "Please provide one idea to enhance productivity and effectiveness when collaborating "
    "with the other two freelancers on the website creation project. Your idea should focus "
    "on improving communication and collaboration in a virtual setting, given that the team "
    "will be managing the project through Zoom for meetings and Microsoft Teams for daily interactions."
)


def display_predefined_question():
    st.markdown(
        """
        <style>
        /* General Container for Question Display */
        .question-container {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 0 auto;
            margin-bottom: 20px;
            max-width: 900px;
            background-color: #f9f9f9;
            box-sizing: border-box;
            width: 100%;
        }

        /* Header Styling */
        .question-header {
            color: #336699 !important;
            font-size: 24px !important;
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Question Text Styling */
        .question-text {
            color: #333 !important;
            font-size: 20px !important;
            line-height: 1.6;
            margin-bottom: 15px;
            text-align: justify;
            word-wrap: break-word;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Responsive Centering for Any Additional Content */
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 40px auto;
            width: 100%;
        }

        .center-content {
            max-width: 80%;
            padding: 0 20px;
            text-align: center;
        }
        .custom-label {
            font-size: 20px !important;
            font-weight: 400;
            margin-bottom: 5px;
            display: block;
            color: #333;
            font-family: Arial, Helvetica, sans-serif;
        }
        .input-wrapper {
            max-width: 900px;
            margin: 0 auto 5px auto;
            text-align: left;
        }

        .stTextArea {
            max-width: 900px;
            margin: 0 auto;
        }

        /* Button Styles */
        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 3px solid #ccc !important;
            border-radius: 7px !important;
            padding: 10px 20px !important;
            font-size: 30px !important;
            cursor: pointer;
            box-shadow: none;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c1c1c1 !important;
            color: #336699 !important;
            border: 3px solid #336699 !important;
        }

        /* Increase font size for text areas */
        textarea {
            font-size: 20px !important;
        }

        /* Dark Mode Adaptation */
        @media (prefers-color-scheme: dark) {
            .question-container {
                background-color: #333 !important;
                color: #f9f9f9 !important;
            }
            .question-header {
                color: #99ccff !important;
            }
            .question-text {
                color: #f1f1f1 !important;
            }
            .custom-label {
                color: #ffffff !important;
            }
            
            .stButton > button {
                color: #f1f1f1 !important;
                background-color: #444 !important;
                border: 3px solid #ccc !important;
            }

            .stButton > button:hover {
                background-color: #555 !important;
                color: #336699 !important;
                border: 3px solid #336699 !important;
            }

        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    container = st.container()
    with container:
        col1, col2, col3 = st.columns([1, 4.2, 1])  # Center-align the input box
        with col2:
            st.markdown(
                f"""
                <div class="question-container">
                    <h2 class="question-header">📢 Freelancing Scenario</h2>
                    <p class="question-text">Now that you’ve completed the practice task, let’s return to our main scenario.</p>
                    <p class="question-text">{question}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            with st.container():
                st.markdown("""
                    <div class="input-wrapper">
                        <label class="custom-label">💡 Enter your idea:</label>
                    </div>
                """, unsafe_allow_html=True)
                st.session_state.user_idea = st.text_area(label="", key="practice_idea_input", height=150)
                #st.session_state.user_idea.strip()
    with st.container():
        col1, col2, col3 = st.columns([9, 10, 0.1])  # Center-align the Next button
        with col2:
            if st.button("Submit", key="next_button"):
                idea = st.session_state.user_idea.strip()
                if idea and idea != st.session_state.last_idea_submitted:
                    st.session_state.submit_in_progress = True
                    st.session_state.last_idea_submitted = idea  # Mark as submitted
                    with st.spinner("Saving idea and generating response..."):
                        update_idea_by_id(st.session_state.user_id, idea,None,"interpersonal_agent")
                        get_ai_response(idea,"input_1")
                    print(f"################Idea saved with ID: ")
                    print("##########in predifined function current screen is : ",st.session_state.current_screen )

                    get_ai_response(idea,"input_1")

                    # st.session_state.current_screen = "ai_response"
                    # st.session_state.submit_in_progress = False
                    print("##########in predifined function current screen is : ",st.session_state.current_screen )
                    st.rerun()
                elif not idea:
                    st.warning("⚠️ Please enter an idea before proceeding.")
                else:
                    st.info("✅ This idea has already been submitted. Please enter a new idea.")
                    with st.spinner("Saving idea and generating response..."):
                        get_ai_response(idea,"input_1")
                    st.session_state.current_screen = "ai_response"
                    st.session_state.submit_in_progress = False
                    st.rerun()