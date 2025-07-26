import streamlit as st


def display_freelancing_scenario():
    # Scenario title and content
    scenario_title = "Freelancing Scenario"
    scenario_content = """
    Imagine you’re a freelancer, hired through a platform called FreelanceHub, to collaborate with two other freelancers on a short-term project to create a website for a client. The project must be completed within two weeks, and since you all live in different cities, the entire project is managed virtually through Zoom for meetings and emails for daily communication and collaboration.

    The client has set strict deadlines and expects daily updates on progress. To ensure the project's success, each team member has been asked to come up with one idea that specifically focuses on improving the efficiency of your 30-minute daily Zoom meetings and enhancing collaboration on Microsoft Teams. Your idea should aim to optimize communication, ensure that everyone is clear on their tasks, and help the team meet the tight deadline.

    The top three ideas will each receive a $5 reward.
    """

    # CSS styling (matching consent form)
    st.markdown(
        """
        <style>
        .scenario-container {
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

        .scenario-header {
            color: #336699 !important;
            font-size: 24px !important;  /* Increased font size */
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        .scenario-text {
            color: #333 !important;
            font-size: 20px !important;  /* Increased font size */
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            word-wrap: break-word;
            font-family: Arial, Helvetica, sans-serif;
        }

        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 3px solid #ccc !important;  /* Increased border size */
            border-radius: 7px !important;  /* Increased border-radius */
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
            .scenario-container {
                background-color: #333 !important;
                color: #f9f9f9 !important;
            }
            .scenario-header {
                color: #99ccff !important;
            }
            .scenario-text {
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

    # Manually replace newlines with <br> to avoid multiple <p> tags
    scenario_content_html = scenario_content.replace("\n", "<br>")

    # Inject HTML for full control over the text structure
    st.markdown(
        f"""
        <div class="scenario-container">
            <h2 class="scenario-header">{scenario_title}</h2>
            <p class="scenario-text">{scenario_content_html}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Centered "Next" button
    with st.container():
        col1, col2, col3 = st.columns([1.8, 1, 1])
        with col2:
            if st.button("Next", key="next_button"):
                st.session_state.current_screen = "ai_manager_info"
                st.query_params["screen"] = "ai_manager_info"
                st.rerun()
