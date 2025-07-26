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
    # print("#########in load image function")
    return Image.open(image_path)

def display_media(image_path,width):
    image_width = width
    image = load_image(image_path)
    st.image(image, caption="Collaboration Image", width=image_width)

def display_resubmit_complete_buttons():
    st.markdown("""
        <style>
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

        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 3px solid #ccc !important;
            border-radius: 7px !important;
            padding: 10px 20px !important;
            font-size: 30px !important;
            cursor: pointer;
            box-shadow: none;
            transition: all 0.3s ease;
            max-width: 200px;
            margin: 10px auto 0 auto;
            display: block;
        }

        .stButton > button:hover {
            background-color: #c1c1c1 !important;
            color: #336699 !important;
            border: 3px solid #336699 !important;
        }

        @media (prefers-color-scheme: dark) {
            .custom-label {
                color: #ffffff !important;
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
    """, unsafe_allow_html=True)

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

    col1, col2, col3 = st.columns([1, 2.45, 1])
    with col2:
        # st.markdown('<label class="custom-label">💡 If you would like to resubmit your idea, please type into the box below!</label>', unsafe_allow_html=True)
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
                        update_idea_by_id(st.session_state.user_id, None,resubmitted_idea,"interpersonal_agent")
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


            
# Helper function to send the request to the backend API and get AI response
def get_ai_response(user_idea,curr_screen):

    try:    
        with st.spinner("🤔 Interpersonal AI Agent is Analyzing.. Please wait..."):
            # Prepare your question and include user_idea in the payload
            print("################")
            print("in get_ai response function and user idea is :  ", user_idea)
            payload = {"idea": user_idea}

            response = requests.post(
                "http://127.0.0.1:5001/ask", json=payload
            )

        if response.status_code == 200:
            data = response.json()
            st.session_state.ai_response = data.get("response", "No response received.")
            # st.session_state.evaluation = data.get("evaluation", "No evaluation available.")
            # st.session_state.references = data.get("references", [])
            st.session_state.show_response = True
            st.session_state.idea_submitted = True  # Prevent AI re-call
            if curr_screen == 'input_1':
                st.session_state.current_screen = "ai_response"  # Move to AI response screen

            st.success("✅ Response received!")



        else:
            st.error(f"❌ Error {response.status_code}")

    except Exception as e:
        st.error(f"⚠️ Failed to connect to backend: {e}")





# def display_ai_response(image_path,curr_screen):
#     # Create a container to hold all content
#     container = st.container()

#     # Use a single column to center content
#     with container:
#         col1, col2, col3 = st.columns([1, 4.2, 1])  # Create three columns, middle one is wider

#         # Place content in the middle column
#         with col2:
#             st.header("🤖🧠 I am the Interpersonal AI manager and have compiled the following information on this matter:")
#             st.success(st.session_state.ai_response)


#             st.write("Based on the feedback provided above, if you would like to resubmit your idea please enter it below.##############")

#             # Display Resubmit and Complete buttons
#             # display_resubmit_complete_buttons()


#     if curr_screen == "ai_response":
#         display_resubmit_complete_buttons()
#         st.session_state.current_screen = "completed"
#         print("##############calling for main scenario")
#     elif curr_screen == "practice_task":
#         # st.session_state.current_screen = "input_1"
#         print("####################calling for practice task ")



def display_ai_response(image_path, curr_screen):
    st.markdown("""
        <style>
        .input-wrapper {
            max-width: 900px;
            margin: 0 auto 5px auto;
            text-align: left;
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

        .ai-feedback-box {
            background-color: #d4edda;
            border-left: 5px solid #28a745;
            padding: 15px;
            margin-top: 10px;
            margin-bottom: 20px;
            color: #155724;
            font-size: 18px;
            font-family: Arial, Helvetica, sans-serif;
            border-radius: 4px;
        }

        @media (prefers-color-scheme: dark) {
            .custom-label {
                color: #ffffff !important;
            }
            .ai-feedback-box {
                background-color: #284e36 !important;
                color: #ccebd1 !important;
                border-left: 5px solid #5dd68c !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # with st.container():
    #     col1, col2, col3 = st.columns([1, 4.2, 1])
    #     with col2:
    st.markdown("""
        <div class="input-wrapper">
            <h3>🤖🧠 Interpersonal AI manager</h3>
            <div class="ai-feedback-box">{}</div>
            <h5>Based on the feedback provided above, if you would like to resubmit your idea please enter it below.</h5>
        </div>
    """.format(st.session_state.ai_response), unsafe_allow_html=True)

    if curr_screen == "ai_response":
        # print("#####in display ai response from main scenario")
        display_resubmit_complete_buttons()
        # st.session_state.current_screen = "completed"
        # st.session_state.session_completed = True
    elif curr_screen == "practice_task":
        # print("###################in display ai response from practice task ")
        pass



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
            

