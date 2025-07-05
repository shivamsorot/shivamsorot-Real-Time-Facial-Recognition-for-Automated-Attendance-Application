# 🎓 Real-Time Facial Recognition Attendance System
An AI-based facial recognition system that automates student attendance using live webcam feed. It scans faces, matches them with stored data, and logs attendance in an Excel file — no manual marking required.

# 📌 Project Overview
This project provides a smart classroom solution for taking automated attendance using computer vision. Teachers can log in securely, select their subject, and the system begins live scanning using a webcam. It detects and recognizes student faces, and marks their presence in a structured Excel sheet — fully automated and offline-ready.

# 🔑 Features
* 🔐 Secure Teacher Login — Start attendance with authorized access.

* 📚 Subject & Faculty Info Page — Select and manage class details.

* 🎥 Live Face Recognition — Scans every 3 seconds for 30 minutes.

* 🕒 Auto Rescan Every 10 Minutes — Captures latecomers without disruption.

* 🛑 Auto Shutdown — Closes camera at 30 minutes, UI at 55 minutes.

* 📁 Excel Integration — Automatically saves attendance records.

* 🖥️ Streamlit UI — Simple, clean interface for easy use.

* 💻 Works Offline — No internet required during attendance.

# ⚙️ Installation Guide
Clone the repo and install the required libraries:
``` 
pip install -r requirements.txt  
```
**Or Install Manually:**
```
pip install opencv-python        # Webcam & image processing
pip install face-recognition     # Face detection and matching
pip install numpy                # Numerical processing
pip install pandas               # Excel/CSV handling
pip install streamlit            # Frontend UI  
```
🧠 `datetime` is part of Python’s standard library and does not require installation.

# 🚦 How It Works
1. Teacher logs in and selects subject, date, and time.

2. Webcam starts scanning faces in real-time (every 3 seconds).

3. Face recognition model identifies known students.

4. Attendance is recorded as “Present” in an Excel file.

5. Rescans every 10 minutes to detect late arrivals.

6. Camera auto-stops after 30 minutes.

7. Streamlit UI auto-shuts after 55 minutes for session security.

# 📄 Sample Output (Excel Format)
|Name|	Subject|	Date|	Time|	Status|  
|----|---------|------|-----|-------|
|Shivam Sorot|	AI|	2025-06-26|	10:00 AM|	Present|
|Priyanshi |	AI	|2025-06-26|	10:00 AM|	Present|

# 🆚 Why This App Stands Out
|Feature	|Our App ✅	|Others ❌|  
|---------|-----------|-----------|
|Real-time face scan (every 3 seconds)|	✅	|❌ One-time only|
|Auto rescan for latecomers	|✅|	❌ Not available|
|Auto shutdown after session	|✅|	❌ Manual closure|
|Simple & modern Streamlit UI|	✅	|❌ Often missing or complex|
|Offline functionality	|✅	|❌ Requires internet|

# 🚀 Future Scope
* 🔗 Integrate with college ERP/database systems

* 📩 Email/SMS notifications for absentees

* 📊 Real-time dashboard with charts and trends

* 📱 Build a mobile version for app-based scanning

* 🗣️ Voice confirmation when attendance is recorded

# 🤝 Contributions
Pull requests are welcome!
For significant changes, please open an issue first to discuss the proposed changes or features.

# 📬 Contact
Project Owner: Shivam Sorot  
📧 Email: shivam29022000@gmail.com
