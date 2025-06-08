import streamlit as st
import pickle
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from db import insert_candidate_result, has_attempted

# Load model
model = pickle.load(open('personality_model.pkl', 'rb'))

# Page Configuration and CSS
st.set_page_config(page_title="Behavioral Interview Assistant", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    .question-card {
        padding: 1rem;
        border-radius: 1rem;
        background-color: #ffffff;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
        border: 1px solid #e0e0e0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        padding: 12px;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #105a8c;
        transform: scale(1.02);
    }
    .timer-box {
        background-color: #ffeeba;
        color: #856404;
        padding: 10px 16px;
        border-radius: 10px;
        font-weight: bold;
        display: inline-block;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 193, 7, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(255, 193, 7, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 193, 7, 0); }
    }
    @media screen and (max-width: 600px) {
        .question-card { padding: 1rem 0.5rem; }
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 HR Behavioral Round Assistant")

# Initialize Session State
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.submitted = False
    st.session_state.name = ""
    st.session_state.email = ""

# Email Sending Function
def send_result_email(to_email, name, label, score):
    sender_email = st.secrets["EMAIL"]
    sender_password = st.secrets["EMAIL_PASSWORD"]
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your HR Personality Assessment Result"
    msg["From"] = sender_email
    msg["To"] = to_email

    html = f"""
    <html>
        <body>
            <h3>Hello {name},</h3>
            <p>Your behavioral interview result is:</p>
            <ul>
                <li><b>Predicted Personality:</b> {label}</li>
                <li><b>Behavioral Score:</b> {score}/10</li>
            </ul>
            <p>Thank you for participating.</p>
        </body>
    </html>
    """

    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        st.success("📩 Result email sent!")
    except Exception as e:
        st.error(f"Failed to send result email: {e}")

# Step 0: Candidate Info
if st.session_state.step == 0:
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.name = st.text_input("Full Name")
    with col2:
        st.session_state.email = st.text_input("Email Address")

    if st.button("Start Test"):
        if st.session_state.name and st.session_state.email:
            if has_attempted(st.session_state.email):
                st.error("❌ You have already attempted this test.")
            else:
                st.session_state.step = 1
                st.session_state.start_time = time.time()
                st.session_state.submitted = False
        else:
            st.warning("Please fill in your name and email to continue.")
    st.stop()

# Timer Logic
elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = max(0, 60 - elapsed_time)
minutes, seconds = divmod(remaining_time, 60)

if not st.session_state.submitted and remaining_time <= 0:
    st.session_state.step = 8
    st.session_state.submitted = True
    st.rerun()

if not st.session_state.submitted:
    st.markdown(f"<div class='timer-box'>⏱️ Time left: {minutes:02d}:{seconds:02d}</div>", unsafe_allow_html=True)

def next_step():
    st.session_state.step += 1

step = st.session_state.step
a = st.session_state.answers

with st.container():
    st.markdown("<div class='question-card'>", unsafe_allow_html=True)

    if step == 1:
        st.subheader("1️⃣ How many hours do you spend alone daily?")
        time_alone = st.slider("Choose a value:", 0, 11, key="alone")
        if st.button("Next"):
            a['time_alone'] = time_alone
            next_step()

    elif step == 2:
        st.subheader("2️⃣ Do you have stage fear?")
        stage_fear = st.radio("Select one:", ["Yes", "No"], key="sfear")
        if st.button("Next"):
            a['stage_fear'] = 1 if stage_fear == "Yes" else 0
            next_step()

    elif step == 3:
        st.subheader("3️⃣ How many social events do you attend per week?")
        social_event = st.slider("Choose a value:", 0, 10, key="sevent")
        if st.button("Next"):
            a['social_event'] = social_event
            next_step()

    elif step == 4:
        st.subheader("4️⃣ How often do you go outside per week?")
        going_outside = st.slider("Choose a value:", 0, 7, key="goutside")
        if st.button("Next"):
            a['going_outside'] = going_outside
            next_step()

    elif step == 5:
        st.subheader("5️⃣ Do you feel drained after socializing?")
        drained = st.radio("Select one:", ["Yes", "No"], key="drain")
        if st.button("Next"):
            a['drained'] = 1 if drained == "Yes" else 0
            next_step()

    elif step == 6:
        st.subheader("6️⃣ How many close friends do you have?")
        friends = st.slider("Choose a value:", 0, 15, key="friends")
        if st.button("Next"):
            a['friends'] = friends
            next_step()

    elif step == 7:
        st.subheader("7️⃣ How often do you post on social media per week?")
        post_freq = st.slider("Choose a value:", 0, 10, key="post")
        if st.button("Submit"):
            a['post_freq'] = post_freq
            st.session_state.submitted = True
            next_step()

if step == 8:
    st.balloons()
    st.success("✅ Thank you! Here's your result.")

    time_alone = a.get('time_alone', 0)
    stage_fear = a.get('stage_fear', 0)
    social_event = a.get('social_event', 0)
    going_outside = a.get('going_outside', 0)
    drained = a.get('drained', 1)
    friends = a.get('friends', 0)
    post_freq = a.get('post_freq', 0)

    features = [[time_alone, stage_fear, social_event, going_outside, drained, friends, post_freq]]
    prediction = model.predict(features)[0]
    label = "Extrovert" if prediction == 1 else "Introvert"

    score = 0
    if stage_fear == 0: score += 1
    if drained == 0: score += 1
    if social_event >= 5: score += 2
    if friends >= 5: score += 2
    if going_outside >= 4: score += 1
    if post_freq >= 5: score += 1
    if time_alone <= 3: score += 2

    st.markdown(f"🧬 <b>Predicted Personality:</b> <code>{label}</code>", unsafe_allow_html=True)
    st.markdown(f"📊 <b>Behavioral Score:</b> <code>{score}/10</code>", unsafe_allow_html=True)

    if score >= 6:
        st.success("✅ Candidate is Behaviorally Suitable for the role.", icon="✅")
    else:
        st.warning("⚠️ Candidate may not be suitable behaviorally for this role.", icon="⚠️")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insert_candidate_result(st.session_state.name, st.session_state.email, label, score, timestamp)
    send_result_email(st.session_state.email, st.session_state.name, label, score)
    st.markdown(f"🕒 <b>Submitted on:</b> <code>{timestamp}</code>", unsafe_allow_html=True)

if remaining_time > 0 and not st.session_state.submitted:
    time.sleep(1)
    st.rerun()
