import base64
import streamlit as st
from PIL import Image
import requests
from filelock import FileLock
import os,random
from utils.db_manager import update_idea_by_id
import json
import pandas as pd


def load_ideas(file_path="/home/dev/rasha_project/AI_Community_projectV2/rasha_ma/decision_making_agent_v2/assets/ideas.json"):
    with open(file_path, "r") as file:
        return json.load(file)["ideas"]
    
    

import streamlit as st
import pandas as pd
import random
# from utils.data_loader import load_profiles  # adjust if needed



def load_profiles(file_path="/home/dev/rasha_project/AI_Community_projectV2/rasha_ma/decision_making_agent_v2/assets/sudo_profiles.json"):
    with open(file_path, "r") as file:
        return json.load(file)


def display_profiles():
    profiles = load_profiles()
    selected_profiles = []

    # Attempt to retrieve saved IDs if present
    profile1 = next((p for p in profiles if p["ID"] == st.session_state.get("saved_id1")), None)
    profile2 = next((p for p in profiles if p["ID"] == st.session_state.get("saved_id2")), None)

    if profile1 and profile2:
        selected_profiles = [profile1, profile2]
    else:
        selected_profiles = random.sample(profiles, 2)
        st.session_state.saved_id1 = selected_profiles[0]["ID"]
        st.session_state.saved_id2 = selected_profiles[1]["ID"]

    for profile in selected_profiles:
        profile.pop("Gender", None)

    # Inject styles
    st.markdown(
        """
        <style>
        .center-content {
            background-color: #f9f9f9;
            width: 52.5%;
            padding: 20px;
            border-radius: 10px;
            font-family: Arial, Helvetica, sans-serif;
            color: #333;
            margin-bottom: 20px;
        }

        .profile-header {
            text-align: center;
            font-size: 24px;
            color: #336699 !important;
            margin-bottom: 10px;
        }

        .profile-subtext {
            text-align: justify;
            font-size: 20px !important;
            color: #444;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-family: Arial, Helvetica, sans-serif;
            margin-top: 10px;
        }

        th, td {
            text-align: center;
            border: 1px solid #ddd;
            padding: 8px;
        }

        /* Dark Mode Support */
        @media (prefers-color-scheme: dark) {
            .center-content {
                background-color: #333 !important;
                color: #f1f1f1 !important;
            }

            .profile-header {
                color: #99ccff !important;
            }

            .profile-subtext {
                color: #ddd !important;
            }

            th, td {
                color: #f1f1f1 !important;
                border: 1px solid #666 !important;
            }

            table {
                background-color: #222 !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display main container with header and text
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <div class="center-content">
                <h1 class="profile-header">Team Members</h1>
                <p class="profile-subtext">
                    I am the decision making AI manager, for this experiment, I have formed six teams of two people. After reviewing your ideas using LLM and various machine learning techniques, I’ve assigned you to Team 4. Here is the information of your team members:
                </p>
                <h2 class="profile-header">Selected Team Members</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Display the table
    df = pd.DataFrame(selected_profiles)
    html_table = df.to_html(index=False)
    html_table = html_table.replace("<th>", "<th style='text-align: center;'>")
    html_table = html_table.replace("<td>", "<td style='text-align: center;'>")

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <div style="width: 55%; max-width: 100%; padding: 0 20px;">
                {html_table}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Optional: debug
    print("Saved ID 1:", st.session_state.saved_id1)
    print("Saved ID 2:", st.session_state.saved_id2)



def display_selected_ideas():
    ideas = load_ideas()

    # Save selected ideas only once in session_state
    if "selected_idea1" not in st.session_state or "selected_idea2" not in st.session_state:
        selected = random.sample(ideas, 2)
        st.session_state.selected_idea1 = selected[0]
        st.session_state.selected_idea2 = selected[1]

    # Use previously saved ideas
    idea1 = st.session_state.selected_idea1
    idea2 = st.session_state.selected_idea2

    # Styling and rendering
    st.markdown(
        """
        <style>
        .ideas-container {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 0 auto;
            max-width: 900px;
            background-color: #f9f9f9;
            text-align: center;
        }
        .main-header {
            text-align: center;
            margin-bottom: 2px;
            color: #336699 !important;
            font-size: 26px;
            font-family: Arial, Helvetica, sans-serif;
        }
        .ideas-header {
            color: #336699;
            font-size: 24px !important;
            margin-bottom: 15px;
            font-family: Arial, Helvetica, sans-serif;
        }
        .ideas-text {
            font-size: 20px !important;
            line-height: 1.8;
            text-align: justify;
            color: #333;
            font-family: Arial, Helvetica, sans-serif;
        }

        @media (prefers-color-scheme: dark) {
            .ideas-container {
                background-color: #333 !important;
                border-color: #666 !important;
            }
            .main-header {
                color: #99ccff !important;
            }
            .ideas-header {
                color: #99ccff !important;
            }
            .ideas-text {
                color: #f1f1f1 !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="ideas-container">
            <h1 class="main-header">Decision Making AI Manager</h1>
            <h2 class="ideas-header">💡 Your team members have provided the following ideas.</h2>
            <p class="ideas-text"><strong>ID: {st.session_state.saved_id1}</strong> - {idea1}</p>
            <p class="ideas-text"><strong>ID: {st.session_state.saved_id2}</strong> - {idea2}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )




# Helper function to display media (image and video)
def display_media(image_path, video_path):
    # st.subheader("📸 Image Related to the Response:")

    # st.subheader("🎥 Video Related to the Response:")
    try:
        with open(video_path, "rb") as video_file:
            video_bytes = video_file.read()
            video_base64 = base64.b64encode(video_bytes).decode()
            video_html = f"""
                <video width="450" autoplay loop muted controls>
                    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            """
            st.markdown(video_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Video file not found: {video_path}")
    except Exception as e:
        st.error(f"Error displaying video: {e}")

    image_width = 450
    st.image(image_path, caption="Collaboration Image", width=image_width)



def display_resubmit_complete_buttons():
    st.markdown(
        """
        <style>
        .custom-label {
            font-size: 20px !important;
            font-weight: 400;
            margin-bottom: 5px;
            color: #333;
            font-family: Arial, Helvetica, sans-serif;
        }
        textarea {
            font-size: 18px !important;
        }
        .stButton > button {
            background-color: #e0e0e0 !important;
            color: #333 !important;
            border: 2px solid #ccc !important;
            border-radius: 6px !important;
            padding: 8px 20px !important;
            font-size: 18px !important;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #ccc !important;
            color: #336699 !important;
        }
        @media (prefers-color-scheme: dark) {
            .custom-label {
                color: #ffffff !important;
            }
            .stButton > button {
                background-color: #444 !important;
                color: #f1f1f1 !important;
                border: 2px solid #ccc !important;
            }
            .stButton > button:hover {
                background-color: #555 !important;
                color: #99ccff !important;
                border: 2px solid #99ccff !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Initialize state if needed
    st.session_state.setdefault("resubmitted_idea", "")
    st.session_state.setdefault("last_resubmitted_idea", "")
    st.session_state.setdefault("submit_in_progress", False)

    # Input field (centered and narrowed)
    col1, col2, col3 = st.columns([1,8.5, 1])
    with col2:
        st.markdown('<label class="custom-label">💡 If you would like to resubmit your idea, please type it into the box below.</label>', unsafe_allow_html=True)
        st.session_state.resubmitted_idea = st.text_area(label="", key="resubmit_idea_input", height=100)

    # Submit button (centered)
    col1, col2, col3 = st.columns([2.5, 1, 2.5])
    with col2:
        if st.button("SUBMIT", key="complete_button"):
            if st.session_state.submit_in_progress:
                st.warning("⏳ Submission in progress. Please wait...")
                return

            idea = st.session_state.resubmitted_idea.strip()
            if idea == st.session_state.last_resubmitted_idea:
                st.info("✅ This idea has already been submitted. Please enter a new idea.")
                st.session_state.current_screen = "completed"
                st.query_params["screen"] = "completed"
                st.session_state.session_completed = True
                st.rerun()
            elif idea:
                st.session_state.submit_in_progress = True
                st.session_state.last_resubmitted_idea = idea
                try:
                    with st.spinner("Saving idea and generating response..."):
                        update_idea_by_id(st.session_state.user_id, None, idea, "decision_making_agent")
                except Exception as e:
                    st.error(f"Error saving idea: {e}")
                    st.session_state.submit_in_progress = False
                    return

                st.session_state.submit_in_progress = False
                st.session_state.current_screen = "completed"
                st.query_params["screen"] = "completed"
                st.session_state.session_completed = True
                st.rerun()
            else:
                st.warning("⚠️ Please enter an idea before submitting.")


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