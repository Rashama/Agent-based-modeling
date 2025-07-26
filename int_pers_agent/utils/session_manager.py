import streamlit as st
from utils.db_manager import create_user_slot
from streamlit_cookies_manager import EncryptedCookieManager
import os

def initialize_session_state():
    query_params = st.query_params
    screen_from_url = query_params.get("screen", None)
    cookies = EncryptedCookieManager(
        prefix="myapp_",
        password=os.environ.get("COOKIES_PASSWORD", "My secret password")
    )

    if not cookies.ready():
        st.stop()

    if "user_id" not in cookies:
        new_user_id = create_user_slot()
        cookies["user_id"] = str(new_user_id)
        cookies.save()
        st.session_state.user_id = new_user_id
        st.write(f"🆕 Created and saved new user_id in cookie: {new_user_id}")
    else:
        st.session_state.user_id = int(cookies["user_id"])
        # st.write(f"🔁 Reusing user_id from cookie: {st.session_state.user_id}")

    valid_screens = {
        "consent_form", "instruction_page", "freelancing_scenario", "ai_manager_info",
        "training_intro", "practice_task", "input_1", "ai_response", "resubmit", "completed"
    }



    # STEP 2: Handle screen logic
    if "current_screen" not in st.session_state:
        if screen_from_url in valid_screens:
            st.session_state.current_screen = screen_from_url
        else:
            st.session_state.current_screen = "consent_form"

    if st.session_state.current_screen in ["ai_response", "resubmit", "completed"]:
        st.query_params["screen"] = st.session_state.current_screen
    else:
        if screen_from_url in valid_screens:
            st.session_state.current_screen = screen_from_url

    if st.session_state.current_screen not in valid_screens:
        st.session_state.current_screen = "consent_form"

    if "unique_number" not in st.session_state:
        st.session_state.unique_number = None

    # STEP 3: Initialize other keys if needed
    defaults = {
        "submit_triggered": False,
        "user_idea_text": "",
        "last_idea_submitted": "",
        "submit_in_progress": False,
        "ai_response": None,
        "show_response": False,
        "user_idea": "",
        "resubmit_user_idea": "",
        "idea_submitted": False,
        "session_completed": False,
        "consent_given": False,
        "practice_idea": "",
        "practice_submitted": False,
        "resubmitted_idea": "",
    }

    for key, val in defaults.items():
        # Always reset submit_in_progress to False on fresh page load
        if key == "submit_in_progress":
            st.session_state[key] = False
        elif key not in st.session_state:
            st.session_state[key] = val