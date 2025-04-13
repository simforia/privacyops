import streamlit as st
import pandas as pd
import datetime
from ghost_gpt_module import run_ghost_gpt
from injector_module import run_instructor_injector
from amazon_obfuscation_module import render_amazon_obfuscation_section
from simforia_data_broker_warroom import run_broker_warroom
from simforia_ops_module import (
    render_broker_overlay,
    log_checkbox,
    trigger_inject_alert,
    export_log,
    generate_gpt_overlay
)

if "simforia_log" not in st.session_state:
    st.session_state.simforia_log = []

st.set_page_config(page_title="Simforia PrivacyOps | Ghost Protocol", layout="wide")

st.subheader("Ghost Protocol - Digital Disappearance Assistant")
st.markdown("Erase the digital you. Control exposure, lock down your footprint, and track your privacy operations.")

with st.sidebar:
    st.header("🧠 User Profile")
    user_type = st.selectbox("Select your role:", ["Civilian", "Journalist", "IC/LEO", "Whistleblower", "Field Op", "Instructor"])
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
    tasks = [
        "Run HaveIBeenPwned breach check",
        "Perform Google search with `site:` queries",
        "Generate IntelX report",
        "Run Optery/Kanary exposure scan"
    ]
    for task in tasks:
        if st.checkbox(task):
            log_checkbox("Phase 1", task)
            generate_gpt_overlay("Exposure Audit", task, instructor=(user_type == "Instructor"))

elif phase == "Phase 2 - Broker Opt-Out":
    st.markdown("### 📤 Broker Opt-Out Tracker")
    is_instructor = user_type == "Instructor"

    render_broker_overlay(
        broker="Spokeo",
        description="Aggregates social media and public records data.",
        opt_out_url="https://www.spokeo.com/optout",
        instructor=is_instructor
    )

    run_broker_warroom(is_instructor)

    df = pd.DataFrame({
        'Broker': ['Spokeo', 'Whitepages', 'MyLife', 'BeenVerified'],
        'Opt-Out Submitted': [False]*4,
        'Confirmation Received': [False]*4,
        'Recheck Date': [""]*4
    })
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    st.download_button("💾 Download Tracker as CSV", edited_df.to_csv(index=False), "privacy_tracker.csv", "text/csv")

elif phase == "Phase 3 - Lockdown Protocols":
    st.markdown("### 🔐 Lockdown Steps")
    tasks = [
        "Setup SimpleLogin or AnonAddy aliases",
        "Create MySudo burner phone",
        "Freeze credit with all bureaus",
        "Install Mullvad VPN",
        "Harden Firefox with uBlock + PrivacyBadger"
    ]
    for task in tasks:
        if st.checkbox(task):
            log_checkbox("Phase 3", task)
            generate_gpt_overlay("Lockdown Protocols", task, instructor=(user_type == "Instructor"))

    with st.expander("🛒 Amazon Obfuscation Playbook (Click to Expand)", expanded=True):
        render_amazon_obfuscation_section()

elif phase == "Phase 4 - Cover Identity":
    st.markdown("### 🪪 Cover Identity Generator")
    identity_fields = [
        "Alias Name", "Fake DOB", "Region/City", "Decoy Job Title", "Burner Email", "Burner Phone"
    ]
    for field in identity_fields:
        st.text_input(field)
        generate_gpt_overlay("Cover Identity", field, instructor=(user_type == "Instructor"))

elif phase == "Phase 5 - Maintenance":
    st.markdown("### 🔁 Ongoing Maintenance")
    tasks = [
        "Check opt-out expiration dates",
        "Run monthly breach scan",
        "Recheck Google/Bing/Yandex caches",
        "Update Obsidian vault or local logs"
    ]
    for task in tasks:
        if st.checkbox(task):
            log_checkbox("Phase 5", task)
            generate_gpt_overlay("Maintenance", task, instructor=(user_type == "Instructor"))

run_ghost_gpt(phase)

if user_type in ["Instructor", "Field Op"]:
    run_instructor_injector()

export_log()
