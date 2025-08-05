# 📊 Bi-monthly Student Dashboard

A secure, interactive dashboard built with Streamlit to track and visualize student performance every two weeks. Designed for educators and administrators, this app provides a streamlined interface for monitoring academic progress, attendance, and engagement.

---

## 🚀 Features

- 🔐 **Secure Authentication** using `streamlit-authenticator`
- 🧮 **Modular Architecture** for scalability and maintainability
- 📈 **Performance Visualization** with dynamic charts and metrics
- 🗂️ **Student Data Management** with structured inputs and summaries
- 🧠 **Built for Educators** with intuitive workflows and clean UI

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/biomnthly-student-dashboard.git
cd biomnthly-student-dashboard

2. Install Dependencies
bash
pip install -r requirements.txt
3. Configure Authentication
Edit config.yaml to define user credentials:

yaml
credentials:
  usernames:
    jagdev:
      email: jagdev@example.com
      name: Jagdev Singh
      password: "$2b$12$YourHashedPasswordHere"

cookie:
  expiry_days: 1
  key: "some_signature_key"
  name: "student_dashboard_cookie"
💡 Use bcrypt to hash passwords securely.

▶️ Run the App
bash
streamlit run app.py
🧱 Project Structure
biomnthly-student-dashboard/
│
├── app.py                  # Main Streamlit app
├── config.yaml             # Authentication config
├── modules/                # Modular components (charts, data handlers)
│   ├── auth.py
│   ├── dashboard.py
│   └── utils.py
├── assets/                 # Static files (images, logos)
├── requirements.txt
└── README.md
📌 Notes
Make sure preauthorized is removed from config.yaml and Authenticate() to avoid deprecation errors.

For multi-user support or registration, consider extending with register_user_view.

👨‍🏫 About the Developer
Created by Jagdev Singh Dosanjh, a dedicated computer faculty at GHS Chananke, Amritsar. Passionate about building scalable educational tools and interactive learning platforms.

📬 Contact
For feedback or collaboration:

📧 jagdev@example.com

🌐 LinkedIn Profile

📄 License
This project is licensed under the MIT License.