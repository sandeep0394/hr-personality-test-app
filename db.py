from supabase import create_client, Client
import streamlit as st

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_candidate_result(name, email, label, score, timestamp):
    data = {
        "name": name,
        "email": email,
        "result": label,
        "score": score,
        "created_at": timestamp
    }
    supabase.table("results").insert(data).execute()

def has_attempted(email):
    response = supabase.table("results").select("*").eq("email", email).execute()
    return len(response.data) > 0
