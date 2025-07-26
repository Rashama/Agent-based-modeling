import streamlit as st
st.set_page_config(layout="wide")
 


import logging
from utils.session_manager import initialize_session_state

from screens.ai_manager_info import display_ai_manager_info
from screens.ai_response import display_ai_response
from screens.consent_form import display_consent_form
from screens.freelancing_scenario import display_freelancing_scenario
from screens.instruction_page import display_instruction_page
from screens.practice_task import display_practice_task
from screens.training_intro import display_training_intro
from screens.predefined_question import display_predefined_question
from screens.survey_page import display_survey_page


logging.getLogger("watchdog.observers.inotify_buffer").setLevel(logging.WARNING)
# st.write("DEBUG: current_screen =", st.session_state.get("current_screen"))




# Main function that controls the flow of the app
def main():
 
    # Paths to image and video (these can be passed dynamically if needed)
    image_path = "/home/dev/rasha_project/AI_Community_projectV2/rasha_ma/inf_agent_v2/assets/img1.png"  # Update with your local image path
    practice_image_path = "/home/dev/rasha_project/AI_Community_projectV2/rasha_ma/inf_agent_v2/assets/img1.png"

    initialize_session_state()

    if st.session_state.session_completed:
        display_survey_page()
        # st.header("Thank you for your participation. Please complete the following survey. 😃")
        # st.write("✅ Session Completed!")
        return

    if st.session_state.current_screen == "consent_form":
        display_consent_form()

    elif st.session_state.current_screen == "instruction_page":
        display_instruction_page()

    elif st.session_state.current_screen == "freelancing_scenario":
        display_freelancing_scenario()

    elif st.session_state.current_screen == "ai_manager_info":
        display_ai_manager_info()

    elif st.session_state.current_screen == "training_intro":
        display_training_intro()

    elif st.session_state.current_screen == "practice_task":
        display_practice_task(practice_image_path)



    elif st.session_state.current_screen == "input_1":
        display_predefined_question()


    elif st.session_state.current_screen == "ai_response":
        print(" in if condition for ai_response screen to call display ai response : ")
        display_ai_response(image_path)

    elif st.session_state.current_screen == "resubmit":
        st.subheader("Informational AI Manager")
        resubmit_text = st.text_area("💡 Resubmit your idea:")
        if st.button("Resubmit Done", key="resubmit_done"):
            st.session_state.session_completed = True
            st.session_state.current_screen = "completed"
            st.query_params["screen"] = "completed"
            st.rerun()

    elif st.session_state.current_screen == "completed":
        print("on complet screen")
        st.header("Thank you for your time 😃")
        st.write("✅ Session Completed!")

main()
