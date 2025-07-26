import streamlit as st
from utils.utils import display_media, get_ai_response, display_ai_response

# New function to display the practice task

def display_practice_task(image_path):
    # Initialize session state variables if they don't exist
    if 'practice_submitted' not in st.session_state:
        st.session_state.practice_submitted = False
    if 'practice_idea' not in st.session_state:
        st.session_state.practice_idea = ""
    if 'resubmit_idea' not in st.session_state:
        st.session_state.resubmit_idea = ""

    # Task content
    practice_title = "Practice Task"
    practice_content = """
    Imagine you are organizing a community event in a local park.
    Please suggest one innovative way to promote the event and attract attendees from the neighborhood.
    """
    ai_manager_info = """
    <ul style="font-size: 20px;">
        <li>Research indicates that 70% of event-goers are influenced by visually appealing and creative promotional materials.</li>
        <li>A study shows that 58% of people learn about community events through social media.</li>
        <li>Studies have demonstrated that engaging local organizations or volunteers in the planning and promotion can lead to a 20% higher turnout.</li>
    </ul>
    """


    # Styling
    st.markdown(
        """
        <style>
        .practice-container {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 0 auto;
            margin-bottom: 20px;
            max-width: 900px;
            background-color: #f9f9f9;
            box-sizing: border-box;
            width: 100%;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        .practice-header {
            color: #336699 !important;
            font-size: 24px !important;
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        .practice-text {
            color: #333 !important;
            font-size: 20px !important;
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            word-wrap: break-word;
            font-family: Arial, Helvetica, sans-serif;
        }

        .ai-manager-info {
            font-size: 16px;  /* Increased font size */
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            font-family: Arial, Helvetica, sans-serif;
        }

        .success-box {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 15px;
        }

        .stTextArea > textarea {
            font-size: 16px !important;
            padding: 10px;
            width: 100% !important;
            max-width: 900px !important;  /* match .practice-container */
            margin: 0 auto;
            display: block;
            box-sizing: border-box;
        }


        textarea {
            font-size: 20px !important;
            padding: 10px !important;
            font-family: Arial, Helvetica, sans-serif !important;
        }

        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 1px solid #ccc !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
            font-size: 30px !important;
            cursor: pointer;
            box-shadow: none;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c1c1c1 !important;
            color: #336699 !important;
            border: 1px solid #336699 !important;
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



        @media (prefers-color-scheme: dark) {
            .practice-container {
                background-color: #333 !important;
                color: #f9f9f9 !important;
            }

            .practice-header {
                color: #99ccff !important;
            }

            .practice-text,
            .ai-manager-info {
                color: #f1f1f1 !important;
            }

            .success-box {
                background-color: #2e5732 !important;
                border-color: #417e4a !important;
                color: #c1f2c7 !important;
            }

            .stButton > button {
                background-color: #444 !important;
                color: #f1f1f1 !important;
                border: 1px solid #ccc !important;
            }

            .stButton > button:hover {
                background-color: #555 !important;
                color: #99ccff !important;
                border: 1px solid #99ccff !important;
            }
            .custom-label {
                color: #ffffff !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Task display
    if not st.session_state.practice_submitted:
        # Container to hold everything
        container = st.container()
        with container:
            col1, col2, col3 = st.columns([1, 4.2, 1])
            with col2:
                # Displaying the task title and content
                st.markdown(
                    f"""
                    <div class="practice-container">
                        <h2 class="practice-header">{practice_title}</h2>
                        <p class="practice-text">{practice_content}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                # Text area for user input (increased size)
                with st.container():
                    st.markdown("""
                        <div class="input-wrapper">
                            <label class="custom-label">💡 Enter your idea:</label>
                        </div>
                    """, unsafe_allow_html=True)
                    st.session_state.practice_idea = st.text_area(label="", key="practice_idea_input", height=150)



        with st.container():
            # Buttons to submit the idea
            col1, col2, col3 = st.columns([9, 10, 0.1])
            with col2:
                if st.button("SUBMIT", key="submit_button"):
                    if st.session_state.practice_idea.strip():
                        st.session_state.practice_submitted = True
                        get_ai_response(st.session_state.practice_idea, "practice_task")
                        st.rerun()
                    else:
                        st.warning("⚠️ Please enter an idea before submitting.")
    else:
        col1, col2, col3 = st.columns([1, 4.2, 1])
        with col2:
            display_ai_response(image_path, 'practice_task')

          

            st.session_state.resubmit_idea = st.text_area(label="", key="resubmit_text", height=100)

        # Create new row of columns for centering the Submit button
        button_col1, button_col2, button_col3 = st.columns([9, 10, 0.1])
        with button_col2:
            if st.button("Submit", key="resubmit_done"):
                st.session_state.current_screen = "input_1"
                st.query_params["screen"] = "input_1"
                st.rerun()