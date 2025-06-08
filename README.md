# 🧠 HR Personality Test App

A Streamlit-based AI-powered application that predicts a candidate's personality based on answers to behavioral questions. This tool is designed to help HR professionals screen candidates more efficiently by analyzing responses and emailing results automatically.


## 🚀 Features

- 🎯 Predicts personality traits using a trained Machine Learning model
- 📩 Automatically emails test results to the candidate
- 📊 Uses data-driven insights from a Kaggle behavioral dataset
- 🔒 Tracks if a user has already attempted the test using Supabase
- 🎨 Clean and simple UI built with Streamlit
- ☁️ Deployed using Streamlit Cloud for easy access


## 📁 Dataset

This app uses a Kaggle dataset titled **“Personality Prediction Dataset”** which is saved as:


personality_dataset.csv


Source: [Kaggle - Personality Prediction Dataset]

## 📥 Installation

Follow these steps to run the project locally:

1. **Clone this repository**:

   bash
   git clone https://github.com/sandeep0394/hr-personality-test-app.git
   cd hr-personality-test-app


2. **Install required libraries**:

   > Make sure Python 3.8 or higher is installed.

   bash
   pip install -r requirements.txt


3. **Configure your credentials**:

   Create a file `.streamlit/secrets.toml` and add the following:
   toml
   SUPABASE_URL = "https://your-project.supabase.co"
   SUPABASE_KEY = "your-service-role-key"

After creating projects in supabase name your project and create a table according to the given schema and also create a RLC which should be enabled

https://accounts.google.com/v3/signin/challenge/pk/presend?TL=ALgCv6z_EiDtLDSwQcXL-NanyaMF-tmAJyMZkl4dpLXLBATALA_6JhTNbd-G0oLQ&authuser=0&cid=1&continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords%3Frapt%3DAEjHL4PL5GWdjCsyqHm1u06PrzO1mzLvvnVx4JX62rZrwfiQXo9IG0f_hYQR3HjPCsIkJ3-Ipv6e5n9JO1e3-3aB1l00Jsv0DM2e9SjrI7lfgmjT6AcnkCk&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords%3Frapt%3DAEjHL4PL5GWdjCsyqHm1u06PrzO1mzLvvnVx4JX62rZrwfiQXo9IG0f_hYQR3HjPCsIkJ3-Ipv6e5n9JO1e3-3aB1l00Jsv0DM2e9SjrI7lfgmjT6AcnkCk&ifkv=AdBytiPvZOV6LPGvcr9tbi-Jm48gV_mGPVDMKwdlR4fQ2rXXQgeXA5idjf1JI7VmnfPhPWrxj2nHLg&osid=1&rart=ANgoxceBJTVAOt92cQH2Jt_AM2-0fFpTIDGGUKDXl2ju2KqyuYm1Or4Wvkisl_Mn_Ypl9WCwL5yGvjEarNfgDuqodD77yg8r8EbccXNfJ_bFnynC4Da130k&rpbg=1&service=accountsettings

Using the above link create an app for your application and will geenarate password so add your email and generated password here below 
   SENDER_EMAIL = "your-email@example.com"
   APP_PASSWORD = "your-app-password"

Add this all in secrets.toml as given in project structure and fromthere use use secrets for safety purpose rather than accesing directly.

5. **Run the app**:

   bash
   streamlit run app1.py

6.**TO STOP PRESS CTRL+C in the terminal.**
  


## 🧪 Prerequisites

* Python 3.8+
* Google App Password (for sending email via Gmail)
* Supabase account/project
* `personality_model.pkl` (trained model file) in root directory
* `personality_dataset.csv` (dataset used for training)



## 📦 Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python, Supabase
* **ML**: scikit-learn
* **Email Service**: SMTP (Gmail with App Password)
* **Database**: Supabase (PostgreSQL)


## 🗂️ Project Structure

hr-personality-test-app/
│
├── app1.py                   # Streamlit UI application
├── db.py                     # Database logic (Supabase)
├── personality_model.pkl     # Trained ML model
├── personality_dataset.csv   # Kaggle dataset
├── requirements.txt          # Python libraries
├── .streamlit/
│   └── secrets.toml          # API keys and sensitive configs
└── README.md                 # This documentation


## 🧠 About the ML Model

* Trained using the Kaggle dataset with algorithms like `Logistic Regression`
* Evaluates behavioral input to predict one of several personality types
* Outputs are shown and emailed with clarity


## 🤝 Contributing

Want to improve this project? Please fork the repository, create a new branch, and submit a pull request. Contributions, issues, and feature requests are welcome.


## 📄 License

This project is Open to all.

## 👨‍💻 Author

Built by **Abotula Sai Sandeep**
GitHub: [@sandeep0394](https://github.com/sandeep0394)

## 🌐 Live Demo
https://hr-personality-test-app.streamlit.app/


✅ **Pro Tip**: After creating the `README.md`, don’t forget to add `.streamlit/secrets.toml` to your `.gitignore` file to avoid exposing secrets.

Let me know if you want a badge, logo, or deployment link included later.
```
