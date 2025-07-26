import streamlit as st
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
        /* Main question container */
        .question-container {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 0 auto 20px auto;
            width: 55%;
            background-color: #f9f9f9;
            box-sizing: border-box;
        }

        /* Headers */
        .question-header {
            color: #336699 !important;
            font-size: 24px !important;
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Question paragraph */
        .question-text {
            color: #333 !important;
            font-size: 20px !important;
            line-height: 1.6;
            margin-bottom: 15px;
            text-align: justify;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Input wrapper */
        .input-wrapper {
            max-width: 55%;
            margin: 0 auto 10px auto;
            text-align: left;
        }

        .custom-label {
            font-size: 20px !important;
            font-weight: 400;
            margin-bottom: 5px;
            display: block;
            color: #333;
            font-family: Arial, Helvetica, sans-serif;
        }

        textarea {
            font-size: 20px !important;
        }

        .stTextArea {
            max-width: 55% !important;
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
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c1c1c1 !important;
            color: #336699 !important;
            border: 3px solid #336699 !important;
        }

        /* Dark mode styles */
        @media (prefers-color-scheme: dark) {
            .question-container {
                background-color: #333 !important;
                color: #f1f1f1 !important;
                border-color: #555 !important;
            }
            .question-header {
                color: #99ccff !important;
            }
            .question-text,
            .custom-label {
                color: #f1f1f1 !important;
            }
            .stTextArea textarea {
                background-color: #222 !important;
                color: #f1f1f1 !important;
                border-color: #666 !important;
            }
            .stButton > button {
                color: #f1f1f1 !important;
                background-color: #444 !important;
                border: 3px solid #aaa !important;
            }
            .stButton > button:hover {
                background-color: #555 !important;
                color: #99ccff !important;
                border-color: #99ccff !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Center-aligned question section
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

    # Input field for idea
    st.markdown("""
        <div class="input-wrapper">
            <label class="custom-label">💡 Enter your idea:</label>
        </div>
    """, unsafe_allow_html=True)
    
    st.session_state.user_idea = st.text_area("", key="practice_idea_input", height=150)

    # Centered submit button
    with st.container():
        col1, col2, col3 = st.columns([9, 10, 0.1])
        with col2:
            if st.button("SUBMIT", key="next_button"):
                idea = st.session_state.user_idea.strip()
                if idea and idea != st.session_state.last_idea_submitted:
                    st.session_state.submit_in_progress = True
                    st.session_state.last_idea_submitted = idea
                    with st.spinner("Saving idea and generating response..."):
                        update_idea_by_id(st.session_state.user_id, idea, None, "decision_making_agent")
                    st.session_state.current_screen = "display_ideas"
                    st.query_params["screen"] = "display_ideas"
                    st.rerun()
                elif not idea:
                    st.warning("⚠️ Please enter an idea before proceeding.")
                else:
                    st.info("✅ This idea has already been submitted. Please enter a new idea.")
                    st.session_state.current_screen = "display_ideas"
                    st.query_params["screen"] = "display_ideas"
                    st.session_state.submit_in_progress = False
                    st.rerun()
