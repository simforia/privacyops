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

# Ensure session state is initialized
if "simforia_log" not in st.session_state:
    st.session_state.simforia_log = []

st.set_page_config(page_title="Simforia PrivacyOps | Ghost Protocol", layout="wide")

st.subheader("Ghost Protocol - Digital Disappearance Assistant")
st.markdown("Erase the digital you. Control exposure, lock down your footprint, and track your privacy operations.")

with st.sidebar:
    st.header("🧠 Configure Your Identity Profile")

    user_name = st.text_input("Full Name", placeholder="e.g., Jordan Reeves")
    user_address = st.text_input("Street Address", placeholder="123 Main St, Apt 4B")
    user_city = st.text_input("City", placeholder="e.g., Asheville")
    user_state = st.text_input("State/Province", placeholder="e.g., NC")
    user_zip = st.text_input("ZIP/Postal Code", placeholder="e.g., 28801")
    user_phone = st.text_input("Phone Number", placeholder="e.g., 555-123-4567")
    user_email = st.text_input("Email Address", placeholder="e.g., jordan@example.com")

    st.session_state["user_identity"] = {
        "name": user_name,
        "address": user_address,
        "city": user_city,
        "state": user_state,
        "zip": user_zip,
        "phone": user_phone,
        "email": user_email
    }

    st.header("🧠 User Profile")
    user_type = st.selectbox("Select your role:", ["Civilian", "Journalist", "IC/LEO", "Whistleblower", "Field Op", "Instructor"])
    st.date_input("Session Date", datetime.date.today())
    st.markdown("Customize your erasure mission below:")

    # ✅ Add this new option:
    advanced_mode = st.checkbox("🔬 Enable Advanced Phases", value=False)
    instructor_mode = st.checkbox("🎓 Instructor Mode", value=False)
st.session_state["is_instructor"] = instructor_mode


if advanced_mode:
    phase = st.radio("Which phase are you working on?", [
        "Phase 0 – Threat Modeling & Persona Calibration",
        "Phase 1 – Exposure Audit",
        "Phase 1.5 – Infrastructure & Access Hygiene",
        "Phase 2 – Broker Opt-Out",
        "Phase 2.5 – Legal & Financial Cloaking",
        "Phase 3 – Lockdown Protocols",
        "Phase 4 – Cover Identity",
        "Phase 4.5 – Synthetic Ecosystem & Decoys",
        "Phase 5 – Maintenance",
        "Phase 5.5 – Burn Network Protocol",
        "Phase 6 – Deception & Noise Seeding",
        "Phase 7 – Cross-Platform Identity Decoupling",
        "Phase 8 – Metadata & Behavioral Cloaking",
        "Phase 9 – Digital Footprint Intelligence (DFI) Feedback Loops",
        "Phase 9.5 – Behavioral Feedback AI Loop",
        "Optional Phase – DNA & Biometric Spoof Prevention"
    ])
else:
    phase = st.radio("Which phase are you working on?", [
        "Phase 1 – Exposure Audit",
        "Phase 2 – Broker Opt-Out",
        "Phase 3 – Lockdown Protocols",
        "Phase 4 – Cover Identity",
        "Phase 5 – Maintenance",
        "Phase 6 – Deception & Noise Seeding",
        "Phase 7 – Cross-Platform Identity Decoupling",
        "Phase 8 – Metadata & Behavioral Cloaking",
        "Phase 9 – Digital Footprint Intelligence (DFI) Feedback Loops"
    ])


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

elif phase == "Phase 6 - Deception & Noise Seeding":
    st.markdown("### 🕵️ Deception & Noise Seeding")
    deception_tactics = [
        "Create noise in people search engines",
        "Seed false job profiles on resume sites",
        "Generate misleading purchase patterns",
        "Use honeypot accounts and controlled leaks"
    ]
    for task in deception_tactics:
        if st.checkbox(task):
            log_checkbox("Phase 6", task)
            generate_gpt_overlay("Surveillance Economy", task, instructor=(user_type == "Instructor"))

elif phase == "Phase 7 - Cross-Platform Identity Decoupling":
    st.markdown("### 🧬 Cross-Platform Identity Decoupling")
    tactic = st.radio(
        "Select your decoupling strategy:",
        ["Metadata Decoupling", "Account Segmentation", "Full Identity Partitioning"],
        key="phase7_strategy"
    )
    if tactic:
        log_checkbox("Phase 7", tactic)
        generate_gpt_overlay("Cross-Platform Ecosystem", tactic, instructor=(user_type == "Instructor"))

elif phase == "Phase 8 - Metadata & Behavioral Cloaking":
    st.markdown("### 🕵️ Phase 8 – Metadata & Behavioral Cloaking")
    tasks = [
        "Use Firefox containers for identity segmentation",
        "Rotate user agents with extensions like Chameleon",
        "Deploy MAC address randomization before connecting",
        "Use hardened OS environments (e.g., Tails, Qubes)",
        "Disable app telemetry, voice input, and activity tracking",
        "Spoof geolocation using browser extensions",
        "Use separate VMs or browser profiles per compartment"
    ]
    for task in tasks:
        if st.checkbox(task, key=f"p8_{task}"):
            log_checkbox("Phase 8", task)
            generate_gpt_overlay("Metadata Cloaking", task, instructor=(user_type == "Instructor"))

elif phase == "Phase 9 - Digital Footprint Intelligence (DFI) Feedback Loops":
    st.markdown("### 📊 Phase 9 – DFI Feedback Loops")
    tasks = [
        "Re-scan people search engines monthly",
        "Monitor for re-listed data using Kanary/Optery",
        "Set Google Alerts for full name, phone, and address",
        "Check if leaked emails are reused or scraped",
        "Review browser/device fingerprint results weekly",
        "Audit metadata leakage from installed extensions"
    ]
    for task in tasks:
        if st.checkbox(task, key=f"p9_{task}"):
            log_checkbox("Phase 9", task)
            generate_gpt_overlay("Digital Footprint Monitoring", task, instructor=(user_type == "Instructor"))

run_ghost_gpt(phase)

if user_type in ["Instructor", "Field Op"]:
    run_instructor_injector()

export_log()
