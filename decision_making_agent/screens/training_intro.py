import streamlit as st

# New function to display the training introduction
def display_training_intro():
    # Content for the training introduction
    training_title = "Training Task"
    training_content = """
    On the following pages, you’ll complete a practice task, where you’ll be presented with a problem scenario, and the goal is to come up with an innovative idea to address it.
    After doing this, you will be presented with the main problem and you need to provide an innovative idea.
    """

    # Custom CSS (reusing consent container styles)
    st.markdown(
        """
        <style>
        /* Instruction Container Styling */
        .training-container {
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

        /* Header */
        .training-header {
            color: #336699 !important;
            font-size: 24px !important;  /* Increased font size */
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Text */
        .training-text {
            color: #333 !important;
            font-size: 20px !important;  /* Increased font size */
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            word-wrap: break-word;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Image */
        .training-image {
            display: block;
            margin: 0 auto 20px auto;
            max-width: 100%;
            max-height: 200px;
            height: auto;
        }

        /* Button Styles */
        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 3px solid #ccc !important;  /* Increased border size */
            border-radius: 7px !important;  /* Increased border-radius for a rounder button */
            padding: 10px 20px !important;  /* Increased padding */
            font-size: 30px !important;  /* Increased font size */
            cursor: pointer;
            box-shadow: none;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c1c1c1 !important;
            color: #336699 !important;
            border: 3px solid #336699 !important;  /* Same increased border size on hover */
        }

        /* Dark Mode Support */
        @media (prefers-color-scheme: dark) {
            .training-container {
                background-color: #333 !important;
                color: #f9f9f9 !important;
            }
            .training-header {
                color: #99ccff !important;
            }
            .training-text {
                color: #f1f1f1 !important;
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


    # Training introduction content
    st.markdown(
        f"""
        <div class="training-container">
            <h2 class="training-header">{training_title}</h2>
            <p class="training-text">{training_content}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Create a centered "Next" button
    with st.container():
        col1, col2, col3 = st.columns([1.8, 1, 1])  # Adjust column widths for centering
        with col2:
            if st.button("Next", key="next_button"):
                st.session_state.current_screen = "practice_task"  # Proceed to the practice task
                st.query_params["screen"] = "practice_task"
                st.rerun()