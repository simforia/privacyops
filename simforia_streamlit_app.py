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
    export_log
)

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
    if st.checkbox("Run HaveIBeenPwned breach check"):
        log_checkbox("Phase 1", "HaveIBeenPwned check completed")
    if st.checkbox("Perform Google search with `site:` queries"):
        log_checkbox("Phase 1", "Google site search completed")
    if st.checkbox("Generate IntelX report"):
        log_checkbox("Phase 1", "IntelX report generated")
    if st.checkbox("Run Optery/Kanary exposure scan"):
        log_checkbox("Phase 1", "Optery/Kanary scan run")

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
    if st.checkbox("Setup SimpleLogin or AnonAddy aliases"):
        log_checkbox("Phase 3", "Setup SimpleLogin or AnonAddy")
    if st.checkbox("Create MySudo burner phone"):
        log_checkbox("Phase 3", "Created MySudo burner phone")
    if st.checkbox("Freeze credit with all bureaus"):
        log_checkbox("Phase 3", "Credit frozen")
    if st.checkbox("Install Mullvad VPN"):
        log_checkbox("Phase 3", "Mullvad VPN installed")
    if st.checkbox("Harden Firefox with uBlock + PrivacyBadger"):
        log_checkbox("Phase 3", "Firefox hardened")

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
    if st.checkbox("Check opt-out expiration dates"):
        log_checkbox("Phase 5", "Opt-out expiration checked")
    if st.checkbox("Run monthly breach scan"):
        log_checkbox("Phase 5", "Monthly breach scan run")
    if st.checkbox("Recheck Google/Bing/Yandex caches"):
        log_checkbox("Phase 5", "Cache recheck done")
    if st.checkbox("Update Obsidian vault or local logs"):
        log_checkbox("Phase 5", "Obsidian vault updated")

run_ghost_gpt(phase)

if user_type in ["Instructor", "Field Op"]:
    run_instructor_injector()

export_log()
