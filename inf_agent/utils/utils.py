import base64
import streamlit as st
from PIL import Image
import requests
from filelock import FileLock
import os,random
from utils.db_manager import update_idea_by_id


# Predefined question
question = (
    "Please provide one idea to enhance productivity and effectiveness when collaborating "
    "with the other two freelancers on the website creation project. Your idea should focus "
    "on improving communication and collaboration in a virtual setting, given that the team "
    "will be managing the project through Zoom for meetings and Microsoft Teams for daily interactions."
)


@st.cache_resource
def load_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
    

def load_image(image_path):
    print("#########in load image function")
    return Image.open(image_path)

def display_media(image_path,width):
    image_width = width
    image = load_image(image_path)
    st.image(image, caption="Collaboration Image", width=image_width)

def get_ai_response():
    try:
        with st.spinner("🤔 Informational AI Agent is Analyzing.. Please wait..."):
            response = requests.post(
                "http://127.0.0.1:5000/ask", json={"question": question}
            )

        if response.status_code == 200:
            data = response.json()
            # In get_ai_response()
            resp_lines = data.get("response", "No response received.").splitlines()
            st.session_state.ai_response = resp_lines
            st.query_params["ai_response"] = "|||".join(resp_lines)


            st.session_state.evaluation = data.get("evaluation", "No evaluation available.")
            st.session_state.references = data.get("references", [])
            st.session_state.show_response = True
            st.session_state.idea_submitted = True  # Prevent AI re-call
            st.session_state.current_screen = "ai_response"  # Move to AI response screen
            st.query_params["screen"] = "ai_response"
            st.success("✅ Response received!")
            st.session_state.submit_in_progress = False
            st.rerun()


        else:
            st.error(f"❌ Error {response.status_code}")

    except Exception as e:
        st.error(f"⚠️ Failed to connect to backend: {e}")


def generate_unique_number():
    filename = "/home/dev/rasha_project/AI_Community_projectV2/rasha_ma/unique_numbers.txt"
    lock = FileLock(f"{filename}.lock")

    with lock:
        existing_numbers = set()

        if os.path.exists(filename):
            with open(filename, "r") as f:
                existing_numbers = {int(line.strip()) for line in f if line.strip().isdigit()}

        # Retry until a unique number is found
        while True:
            new_number = random.randint(0, 999)
            if new_number not in existing_numbers:
                with open(filename, "a") as f:
                    f.write(f"{new_number}\n")
                return new_number
            



            

def display_resubmit_complete_buttons():
    # Initialize session state for resubmitted idea if it doesn't exist
    st.markdown(
        """
        <style>
        .stButton > button {
            max-width: 200px; /* Adjust the width as needed */
        }
        .custom-label {
            font-size: 20px !important;
            font-weight: 400;
            margin-bottom: 5px;
            display: block;
            color: #333;
            font-family: Arial, Helvetica, sans-serif;
        }
        textarea {
            font-size: 18px !important;
        }
        @media (prefers-color-scheme: dark) {
            .custom-label {
                color: #ffffff !important;
            }   
        }


        </style>
        """,
        unsafe_allow_html=True,
    )

    for key in ["resubmitted_idea", "last_resubmitted_idea", "submit_in_progress", "idea_saved"]:
        if key not in st.session_state:
            st.session_state[key] = "" if "idea" in key else False

    if st.session_state.submit_in_progress and st.session_state.idea_saved:
        st.session_state.submit_in_progress = False
        st.session_state.idea_saved = False
        st.session_state.current_screen = "completed"
        st.query_params["screen"] = "completed"
        st.session_state.session_completed = True
        st.rerun()

    # col1, col2, col3 = st.columns([1, 2.45, 1])
    # with col2:
    st.markdown('<label class="custom-label">💡 Resubmit your idea:</label>', unsafe_allow_html=True)
    st.session_state.resubmitted_idea = st.text_area(label="", key="resubmit_idea_input", height=100)
    resubmitted_idea = st.session_state.resubmitted_idea.strip()

    if st.button("SUBMIT", key="complete_button"):
        if st.session_state.get("submit_in_progress", False):
            st.warning("⏳ Submission in progress. Please wait...")
            return

        if resubmitted_idea == st.session_state.get("last_resubmitted_idea", ""):
            st.info("✅ This idea has already been submitted. Please enter a new idea.")
            st.session_state.submit_in_progress = False
            st.session_state.current_screen = "completed"
            st.query_params["screen"] = "completed"
            st.session_state.session_completed = True
            st.rerun()

        else:
            st.session_state.submit_in_progress = True
            st.session_state.last_resubmitted_idea = resubmitted_idea

            try:
                with st.spinner("Saving idea and generating response..."):
                    update_idea_by_id(st.session_state.user_id,None, resubmitted_idea, "information_agent")
                st.session_state.idea_saved = True
            except Exception as e:
                st.error(f"Error saving idea: {e}")
                st.session_state.submit_in_progress = False
                return

            st.session_state.submit_in_progress = False
            st.session_state.current_screen = "completed"
            st.query_params["screen"] = "completed"
            st.session_state.session_completed = True
            st.rerun()
