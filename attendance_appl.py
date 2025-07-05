import streamlit as st
import cv2
import os
import time
import numpy as np
import pandas as pd
from datetime import datetime
from deepface import DeepFace
from mtcnn import MTCNN
import tensorflow as tf

# Define directories
DATASET_PATH = r"D:\final_year\dataset"  # Student face dataset
ATTENDANCE_DIR = "Attendance"

# Ensure attendance directory exists
if not os.path.exists(ATTENDANCE_DIR):
    os.makedirs(ATTENDANCE_DIR)

# Load MTCNN detector
detector = MTCNN()

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "attendance_data" not in st.session_state:
    st.session_state.attendance_data = {}
if "scan_count" not in st.session_state:
    st.session_state.scan_count = 0

# Function to recognize faces and mark attendance
def recognize_and_mark_attendance(frame, detected_students):
    results = DeepFace.find(img_path=frame, db_path=DATASET_PATH, model_name="Facenet512", distance_metric="cosine", enforce_detection=False)
    if results and isinstance(results, list) and len(results[0]) > 0:
        recognized_face = results[0].iloc[0]
        name = os.path.basename(os.path.dirname(recognized_face['identity']))
        
        if name not in detected_students:  # Only detect once per scan
            detected_students.add(name)
            if name in st.session_state.attendance_data:
                st.session_state.attendance_data[name] += 1
            else:
                st.session_state.attendance_data[name] = 1
            
            st.success(f"Detected {name} ({st.session_state.attendance_data[name]} times)")

# Function to finalize attendance after multiple scans
def finalize_attendance():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    file_path = f"{ATTENDANCE_DIR}/Attendance_{date_str}.csv"
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("Name,Time\n")
    
    for name, count in st.session_state.attendance_data.items():
        if count >= 2:  # Mark attendance if detected twice
            with open(file_path, "a") as f:
                f.write(f"{name},{now.strftime('%H:%M:%S')}\n")
    
    st.success("✅ Attendance saved successfully!")
    st.session_state.page = "Login"  # Reset to login after completion

# Streamlit UI
if st.session_state.page == "Login":
    st.title("🔐 Teacher Login")
    teacher_id = st.text_input("Enter Teacher ID")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if teacher_id == "admin" and password == "1234":
            st.session_state.page = "Faculty Details"
        else:
            st.error("Invalid ID or Password!")

elif st.session_state.page == "Faculty Details":
    st.title("📚 Faculty & Subject Details")
    faculty_name = st.text_input("Faculty Name")
    subject_name = st.text_input("Subject Name")
    subject_code = st.text_input("Subject Code")
    class_time = st.time_input("Lecture Start Time")
    class_date = st.date_input("Lecture Date")
    if st.button("Start Attendance"):
        st.session_state.faculty_name = faculty_name
        st.session_state.subject_name = subject_name
        st.session_state.subject_code = subject_code
        st.session_state.class_time = class_time
        st.session_state.class_date = class_date
        st.session_state.page = "Attendance System"
        st.session_state.scan_count = 0  # Reset scan count

elif st.session_state.page == "Attendance System":
    st.title("📸 Face Recognition Attendance System")
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    
    if cap.isOpened():
        while st.session_state.scan_count < 4:  # 4 scans
            detected_students = set()
            scan_start_time = time.time()
            while time.time() - scan_start_time < 15:  # 15 seconds per scan
                ret, frame = cap.read()
                if not ret:
                    st.error("Error accessing camera!")
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                stframe.image(frame, channels="RGB")
                temp_img_path = "temp_frame.jpg"
                cv2.imwrite(temp_img_path, frame)
                recognize_and_mark_attendance(temp_img_path, detected_students)
                time.sleep(1)
            
            st.session_state.scan_count += 1
            if st.session_state.scan_count < 4:
                st.write(f"✅ Scan {st.session_state.scan_count} completed! Next scan in 20 seconds...")
                time.sleep(20)
        
        cap.release()
        cv2.destroyAllWindows()
        finalize_attendance()
    
    if st.button("Back to Login"):
        st.session_state.page = "Login"