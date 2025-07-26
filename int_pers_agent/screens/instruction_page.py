import streamlit as st

def display_instruction_page():
    instruction_image_path = "imag3.jpeg"

    st.markdown(
        """
        <style>
        /* Instruction Container Styling */
        .instruction-container {
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
        .instruction-header {
            color: #336699 !important;
            font-size: 24px !important;  /* Increased font size */
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Text */
        .instruction-text {
            color: #333 !important;
            font-size: 20px !important;  /* Increased font size */
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            word-wrap: break-word;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Image */
        .instruction-image {
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
            .instruction-container {
                background-color: #333 !important;
                color: #f9f9f9 !important;
            }
            .instruction-header {
                color: #99ccff !important;
            }
            .instruction-text {
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

    st.markdown(
        f"""
        <div class="instruction-container">
            <h2 class="instruction-header">Instructions</h2>
            <p class="instruction-text">
                We are conducting an experiment to examine how Artificial Intelligence (AI) managers influence individual performance. In this experiment, you will generate ideas for various situations and will be managed by an Interpersonal AI manager.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        col1, col2, col3 = st.columns([1.8, 1, 1])
        with col2:
            if st.button("Next", key="next_button"):
                st.session_state.current_screen = "freelancing_scenario"
                st.query_params["screen"] = "freelancing_scenario"
                st.rerun()