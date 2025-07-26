import streamlit as st
from utils.utils import display_resubmit_complete_buttons,display_media

def display_ai_response(image_path):

    print("##########################in display ai response")
    # Recover from query params if not already in session_state
    if "ai_response" not in st.session_state or not st.session_state.ai_response:
        encoded_resp = st.query_params.get("ai_response", "")
        if encoded_resp:
            st.session_state.ai_response = encoded_resp.split("|||")

    # Debugging
    # st.write("DEBUG: ai_response", st.session_state.get("ai_response"))

    # Safeguard again
    if not st.session_state.get("ai_response"):
        st.error("AI response not available. Please resubmit your query.")
        return

    col1, col2 = st.columns(2)  # Create two columns

    with col1:
        # Use Markdown to emphasize the header
        header_text = "🤖🧠 I am the Interpersonal AI manager and have compiled the following information on this matter:"
        st.markdown(
            """
            <style>
            .ai-response-container {
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

            .ai-response-header {
                color: #336699 !important;
                font-size: 24px !important;
                margin-bottom: 15px;
                text-align: center;
                font-family: Arial, Helvetica, sans-serif;
            }

            .ai-response-text {
                color: #333 !important;
                font-size: 20px !important;
                line-height: 1.6;
                margin-bottom: 20px;
                text-align: justify;
                word-wrap: break-word;
                font-family: Arial, Helvetica, sans-serif;
            }

            .ai-response-bullet-points {
                font-size: 20px;
                line-height: 1.6;
                margin-bottom: 20px;
                text-align: justify;
                font-family: Arial, Helvetica, sans-serif;
            }

            .ai-response-box {
                background-color: #d4edda;
                border: 1px solid #c3e6cb;
                color: #155724;
                padding: 10px;
                border-radius: 4px;
                margin-bottom: 15px;
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

            @media (prefers-color-scheme: dark) {
                .ai-response-container {
                    background-color: #333 !important;
                    color: #f9f9f9 !important;
                }

                .ai-response-header {
                    color: #99ccff !important;
                }

                .ai-response-text,
                .ai-response-bullet-points {
                    color: #f1f1f1 !important;
                }

                .ai-response-box {
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
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Header
        st.markdown(
            f"""
            <h2 class="ai-response-header">{header_text}</h2>
            """,
            unsafe_allow_html=True,
        )

        # AI Response label
        st.markdown(
            """
            <p class="ai-response-text" style="font-size: 20px; font-weight: bold;">AI Response:</p>
            """,
            unsafe_allow_html=True,
        )
        bullet_points = "".join(
            f"<li>{line.strip()}</li>" for line in st.session_state.ai_response if line.strip()
        )





        # Wrap in styled green box with <ul>
        st.markdown(
            f"""
            <div class="ai-response-box ai-response-bullet-points">
                <ul style="padding-left: 20px;">{bullet_points}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Resubmit instructions
        # resubmit_text = "Based on the information provided above, if you would like to resubmit your idea please enter it below."
        # st.markdown(
        #     f"""
        #     <p class="ai-response-text" style="font-size: 18px;">{resubmit_text}</p>
        #     """,
        #     unsafe_allow_html=True,
        # )

        # Display Resubmit and Complete buttons
        display_resubmit_complete_buttons()

    with col2:
        # Display image with larger size
        display_media(image_path,600)
