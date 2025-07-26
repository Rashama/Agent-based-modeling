import streamlit as st 

def display_consent_form():
    st.markdown(
        """
        <style>
        .consent-container {
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

        /* Increased font size for header */
        .consent-header {
            color: #336699 !important;
            font-size: 24px !important;  /* Dramatically increased font size */
            margin-bottom: 15px;
            text-align: center;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Increased font size for text */
        .consent-text {
            color: #333 !important;
            font-size: 20px !important;  /* Dramatically increased font size */
            line-height: 1.6;
            margin-bottom: 20px;
            text-align: justify;
            word-wrap: break-word;
            font-family: Arial, Helvetica, sans-serif;
        }

        /* Button Container */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 5px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        /* Button Styles */
        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 1px solid #ccc !important;
            border-radius: 7px !important;
            padding: 10px 20px !important;
            font-size: 30px !important;
            cursor: pointer;
            box-shadow: none;
            transition: all 0.3s ease;
        }

        /* Button Hover Styles */
        .stButton > button:hover {
            background-color: #c1c1c1 !important;
            color: #336699 !important;
            border: 1px solid #336699 !important;
        }

        /* Dark Mode Adaptation */
        @media (prefers-color-scheme: dark) {
            .consent-container {
                background-color: #333 !important;
                color: #f9f9f9 !important;
            }
            .consent-header {
                color: #99ccff !important;
            }
            .consent-text {
                color: #f1f1f1 !important;
            }
            .stButton > button {
                color: #f1f1f1 !important;
                background-color: #444 !important;
                border: 1px solid #ccc !important;
            }
            .stButton > button:hover {
                background-color: #555 !important;
                color: #336699 !important;
                border: 1px solid #336699 !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="consent-container">
            <h2 class="consent-header">Informed Consent Form</h2>
            <p class="consent-text">
                Please read this consent form carefully before deciding to participate in this study.
            </p>
            <p class="consent-text">
                <b>Purpose of the research study:</b> We are conducting research to understand how Informational AI managers affect workers. Your participation in this survey is highly appreciated.
            </p>
            <p class="consent-text">
                <b>Risks/Discomforts:</b> The risks involved in this study are minimal. No sensitive data will be collected.
            </p>
            <p class="consent-text">
                <b>Benefits:</b> While there are no direct benefits to you, the findings from this study will hopefully benefit others in the future.
            </p>
            <p class="consent-text">
                <b>Voluntary participation:</b> Your participation is completely voluntary. You can withdraw from the task at any time without penalty.
            </p>
            <p class="consent-text">
                <b>Confidentiality:</b> Your identity will remain strictly confidential. Your personal information will be protected, and your responses will be used solely for scientific purposes. All data will be securely stored and only accessed by the research team. This study has been reviewed and deemed exempt by the Institutional Review Board.
            </p>
            <p class="consent-text">
                <b>Questions:</b> If you have any questions about this research, please contact Rasha Alahmad at <a href="mailto:Rasha.ahmad@kfupm.edu.sa">Rasha.ahmad@kfupm.edu.sa</a>.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        col1, col2, col3 = st.columns([1.5, 1.4, 2])
        with col2:
            if st.button("Yes, I agree", key="consent_yes"):
                st.session_state.consent_given = True
                st.session_state.current_screen = "instruction_page"
                st.query_params["screen"] = "instruction_page"
                st.rerun()
        with col3:
            if st.button("No, I don't agree", key="consent_no"):
                st.session_state.session_completed = True
                st.rerun()
