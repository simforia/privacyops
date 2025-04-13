import streamlit as st
import pandas as pd
import datetime
from ghost_gpt_module import run_ghost_gpt  # GPT module import
from injector_module import run_instructor_injector
from amazon_obfuscation_module import render_amazon_obfuscation_section
from simforia_data_broker_warroom import run_broker_warroom

st.set_page_config(page_title="Simforia PrivacyOps | Ghost Protocol", layout="wide")

st.title("🛡️ Simforia PrivacyOps Suite")
st.subheader("Ghost Protocol - Digital Disappearance Assistant")

st.markdown("Erase the digital you. Control exposure, lock down your footprint, and track your privacy operations.")

with st.sidebar:
    st.header("🧠 User Profile")
    user_type = st.selectbox("Select your role:", ["Civilian", "Journalist", "IC/LEO", "Whistleblower", "Field Op"])
    st.date_input("Session Date", datetime.date.today())
    st.markdown("Customize your erasure mission below:")

st.header("🗂️ Phase Selection")

phase = st.radio("Which phase are you working on?", [
    "Phase 1 - Exposure Audit",
    "Phase 2 - Broker Opt-Out",
    "Phase 3 - Lockdown Protocols",
    "Phase 4 - Cover Identity",
    "Phase 5 - Maintenance"])

if phase == "Phase 1 - Exposure Audit":
    st.markdown("### 🔍 Exposure Audit Checklist")
    st.checkbox("Run HaveIBeenPwned breach check")
    st.checkbox("Perform Google search with `site:` queries")
    st.checkbox("Generate IntelX report")
    st.checkbox("Run Optery/Kanary exposure scan")

elif phase == "Phase 2 - Broker Opt-Out":
    st.markdown("### 📤 Broker Opt-Out Tracker")

    is_instructor = user_type == "Instructor"
    run_broker_warroom(is_instructor)

    df = pd.DataFrame({
        'Broker': ['Spokeo', 'Whitepages', 'MyLife', 'BeenVerified'],
        'Opt-Out Submitted': [False]*4,
        'Confirmation Received': [False]*4,
        'Recheck Date': [""]*4
    })

            })
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    st.download_button("💾 Download Tracker as CSV", edited_df.to_csv(index=False), "privacy_tracker.csv", "text/csv")

elif phase == "Phase 3 - Lockdown Protocols":
    st.markdown("### 🔐 Lockdown Steps")
    st.checkbox("Setup SimpleLogin or AnonAddy aliases")
    st.checkbox("Create MySudo burner phone")
    st.checkbox("Freeze credit with all bureaus")
    st.checkbox("Install Mullvad VPN")
    st.checkbox("Harden Firefox with uBlock + PrivacyBadger")
    with st.expander("🛒 Amazon Obfuscation Playbook (Click to Expand)", expanded=True):
        render_amazon_obfuscation_section()


elif phase == "Phase 4 - Cover Identity":
    st.markdown("### 🪪 Cover Identity Generator")
    st.text_input("Alias Name")
    st.text_input("Fake DOB")
    st.text_input("Region/City")
    st.text_input("Decoy Job Title")
    st.text_input("Burner Email")
    st.text_input("Burner Phone")

elif phase == "Phase 5 - Maintenance":
    st.markdown("### 🔁 Ongoing Maintenance")
    st.checkbox("Check opt-out expiration dates")
    st.checkbox("Run monthly breach scan")
    st.checkbox("Recheck Google/Bing/Yandex caches")
    st.checkbox("Update Obsidian vault or local logs")

# ✅ GPT Advisor module with Obsidian export
run_ghost_gpt(phase)
# Instructor-only panel
if user_type in ["Instructor", "Field Op"]:  # Optional access gating
    run_instructor_injector()

