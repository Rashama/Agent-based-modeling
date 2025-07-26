import streamlit as st
from utils.utils import load_base64_image

def display_ai_manager_info():
    # Content for the AI manager information
    ai_manager_title = "Interpersonal AI Manager"
    ai_manager_content = """
    I am the Interpersonal AI Manager, developed by Tech Innovate Inc. I am designed to serve as an Interpersonal manager, assisting participants in generating better ideas by providing them with relevant Interpersonal. I leverage advanced large language models (LLMs) such as OpenAI's GPT-4 and proprietary machine learning algorithms to assist you. My system integrates neural network architectures and natural language processing techniques to provide accurate and contextually relevant support. I will interact with you following the steps outlined in the graph below.

    I will be here throughout the experiment to ensure that your contributions are effective.
    """

    # # Path to the AI manager image
    # ai_manager_image_path = "/home/dev/rasha_project/AI_Community_projectV2/rasha_ma/img2.png"

    # # # Load and encode image
    # with open(ai_manager_image_path, "rb") as image_file:
    #     encoded_image = base64.b64encode(image_file.read()).decode()

    ai_manager_image_path = "/home/dev/rasha_project/AI_Community_projectV2/rasha_ma/int_pers_agent_v2/assets/img2.png"
    encoded_image = load_base64_image(ai_manager_image_path)

    # Style for container
    st.markdown(
        """
        <style>
        .ai-manager-container {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 0 auto 20px auto;
            max-width: 900px;
            background-color: #f9f9f9;
            box-sizing: border-box;
            width: 100%;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        .ai-manager-header {
            color: #336699 !important;
            font-size: 24px !important;  /* Increased font size */
            margin-bottom: 15px;
        }

        .ai-manager-text, .ai-manager-container p {
            color: #333;
            font-size: 20px !important;  /* Increased font size */
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            word-wrap: break-word;
        }

        .ai-manager-image {
            display: block;
            margin: 0 auto;
            max-width: 90%;
            max-height: 250px;
            height: auto;
            object-fit: contain;
            border-radius: 8px;
        }

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

        @media (prefers-color-scheme: dark) {
            .ai-manager-container {
                background-color: #333 !important;
                color: #f9f9f9 !important;
            }
            .ai-manager-header {
                color: #99ccff !important;
            }
            .ai-manager-text {
                color: #f1f1f1 !important;
            }
            .stButton > button {
                color: #f1f1f1 !important;
                background-color: #444 !important;
                border: 3px solid #ccc !important;
            }
            .stButton > button:hover {
                background-color: #555 !important;
                color: #99ccff !important;
                border: 3px solid #99ccff !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display content
    st.markdown(
        f"""
        <div class="ai-manager-container">
            <h2 class="ai-manager-header">{ai_manager_title}</h2>
            <p class="ai-manager-text">{ai_manager_content}</p>
            <img src="data:image/jpeg;base64,{encoded_image}" class="ai-manager-image" />
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Centered Next button
    with st.container():
        col1, col2, col3 = st.columns([1.8, 1, 1])
        with col2:
            if st.button("Next", key="next_button"):
                st.session_state.current_screen = "training_intro"
                st.query_params["screen"] = "training_intro"
                st.rerun()
