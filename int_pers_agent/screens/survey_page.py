import streamlit as st
from utils.utils import generate_unique_number
from utils.db_manager import update_generative_num_by_id


def display_survey_page():
    st.markdown(
        """
        <style>
        .survey-container {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 0 auto 20px auto;
            max-width: 900px;
            background-color: #f9f9f9;
            box-sizing: border-box;
        }

        .survey-header {
            color: #336699 !important;
            font-size: 24px !important;
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        .survey-text {
            color: #333 !important;
            font-size: 18px !important;
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            word-wrap: break-word;
            font-family: Arial, Helvetica, sans-serif;
        }

        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 3px solid #ccc !important;
            border-radius: 7px !important;
            padding: 10px 20px !important;
            font-size: 20px !important;
            cursor: pointer;
            box-shadow: none;
            transition: all 0.3s ease;
            display: block;
            margin: 0 auto;
        }

        .stButton > button:hover {
            background-color: #c1c1c1 !important;
            color: #336699 !important;
            border: 3px solid #336699 !important;
        }

        .loader {
            border: 8px solid #f3f3f3;
            border-top: 8px solid #3498db;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="survey-container">
            <h2 class="survey-header">Survey Instructions</h2>
            <div class="survey-text">
                <ul>
                    <li>Click the button below to generate a random number.</li>
                    <li>Write down the number that appears.</li>
                    <li>Proceed to complete the survey.</li>
                    <li>When prompted in the survey, enter the number you wrote down.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    placeholder = st.empty()
    if st.session_state.get("unique_number") is None:
        if placeholder.button("Generate Number", key="generate_num_button"):
            spinner_placeholder = st.empty()
            with spinner_placeholder.container():
                st.markdown(
                    """
                    <div style="display: flex; justify-content: center; align-items: center; height: 300px; margin-left: 50px;">
                        <div style="text-align: center;">
                            <div class="loader"></div>
                            <p style="margin-top: 10px;">🔄 Generating your unique number...</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            try:
                unique_number = generate_unique_number()
                st.session_state.unique_number = unique_number
                user_id = st.session_state.get("user_id")
                if user_id is not None:
                    update_generative_num_by_id(user_id, unique_number)
                else:
                    st.warning("User ID not found in session state.")
            except ValueError as e:
                st.error(str(e))
            finally:
                spinner_placeholder.empty()

    if st.session_state.get("unique_number") is not None:
        st.markdown(
            f"""
            <div class="survey-container">
                <p class="survey-text" style="text-align:center;">
                    <strong>Your Unique Number:</strong> {st.session_state.unique_number:03d}
                </p>
                <p class="survey-text" style="text-align:center;">
                <a href="https://umich.qualtrics.com/jfe/form/SV_3kmUwkd6xRUc0rY" style="font-size:20px; color:#336699; text-decoration:underline;">
                    Click here to proceed to the Survey
                </a>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
