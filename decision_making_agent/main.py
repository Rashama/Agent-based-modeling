import streamlit as st
st.set_page_config(layout="wide")
 


import logging
from utils.session_manager import initialize_session_state
from utils.utils import display_selected_ideas, display_resubmit_complete_buttons

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
    image_path = "img1.png"  # Update with your local image path
    #video_path = "7665d69d-73ca-4072-b5f6-5a35200a29e4.MP4"  # Update with your local video path
    practice_image_path = "img1.png"
    #practice_video_path = "7665d69d-73ca-4072-b5f6-5a35200a29e4.MP4"

    initialize_session_state()

    # Conditional display based on session state
    if st.session_state.session_completed:
        display_survey_page()
        return

    if st.session_state.current_screen == "consent_form":
        print("######################### in consent form")
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
   


    elif st.session_state.current_screen == "display_ideas":
        container = st.container()
        with container:
            col1, col2, col3 = st.columns([1, 4.2, 1])  # Center-align the content
            with col2:
                print("##################################in screen display ideas : ")
                #st.markdown("<h1 style='text-align: center;margin-bottom: 5px;'>AI Decision Making Agent</h1>", unsafe_allow_html=True)
                display_selected_ideas()
                display_resubmit_complete_buttons()



    elif st.session_state.current_screen == "completed":
        print("########in elif of completed")
        st.header("Thank you for your time 😃")
        st.write("✅ Session Completed!")

main()
