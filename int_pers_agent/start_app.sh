#!/bin/bash

# Run the Python backend
python3 /home/dev/rasha_project/AI_Community_projectV2/rasha_ma/int_pers_agent_v2/backend/int_backend.py &

# Wait a bit to make sure the backend starts (optional)
sleep 2

# Run the Streamlit frontend
streamlit run /home/dev/rasha_project/AI_Community_projectV2/rasha_ma/int_pers_agent_v2/main.py
