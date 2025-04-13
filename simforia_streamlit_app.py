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
    "Phase 5 - Maintenance",
    "Phase 6 - Deception & Noise Seeding",
    "Phase 7 - Cross-Platform Identity Decoupling"
    "Phase 8 - Metadata Cloaking"
    "Phase 9 - Digital Footprint Intelligence (DFI) Feedback Loops"
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

    st.markdown("- **Seed false data into people search engines** (e.g., create fake LinkedIn profiles, alternate aliases).")
    st.markdown("- **Join marketing platforms with decoy emails/names** to pollute databases.")
    st.markdown("- **Use GPS spoofing apps** or spoofed check-ins to mislead location-based services.")
    st.markdown("- **Engage in controlled deception**: Loyalty cards with burner info, fake newsletter signups, etc.")
    st.markdown("- **Monitor noise profiles** with a privacy dashboard or use Optery/Kanary under multiple aliases.")

    tactic = st.radio("Select deception vector:", ["Obfuscate", "Noise Seeding", "Both (Layered Deception)"], key="phase6_deception")

    if tactic:
        generate_gpt_overlay("Surveillance Economy", tactic, instructor=(user_type == "Instructor"))
elif phase == "Phase 7 - Cross-Platform Identity Decoupling":
    st.markdown("### 🧬 Cross-Platform Identity Decoupling")

    st.markdown("- **Disentangle your accounts:** Use different aliases, emails, and profile images across services.")
    st.markdown("- **Break metadata chains:** Vary your devices, browsers, and locations when accessing services.")
    st.markdown("- **Segment usage patterns:** Divide your online behaviors into distinct compartments (e.g., financial, health, social).")
    st.markdown("- **Use compartmentalized identities:** Each purpose (banking, work, social) should have a unique email, phone, IP trail, and name variant.")
    st.markdown("- **Reset digital fingerprints:** Regularly purge cookies, browser caches, and rotate VPN exit nodes/IPs.")

    tactic = st.radio(
        "Which strategy do you want to apply?",
        ["Metadata Decoupling", "Account Segmentation", "Full Identity Partitioning"],
        key="phase7_decoupling"
    )
elif phase == "Phase 7 - Cross-Platform Identity Decoupling":
    st.markdown("### 🧬 Cross-Platform Identity Decoupling")

    st.markdown("- **Disentangle your accounts:** Use different aliases, emails, and profile images across services.")
    st.markdown("- **Break metadata chains:** Vary your devices, browsers, and locations when accessing services.")
    st.markdown("- **Segment usage patterns:** Divide your online behaviors into distinct compartments (e.g., financial, health, social).")
    st.markdown("- **Use compartmentalized identities:** Each purpose (banking, work, social) should have a unique email, phone, IP trail, and name variant.")
    st.markdown("- **Reset digital fingerprints:** Regularly purge cookies, browser caches, and rotate VPN exit nodes/IPs.")

    tactic = st.radio(
        "Which strategy do you want to apply?",
        ["Metadata Decoupling", "Account Segmentation", "Full Identity Partitioning"],
        key="phase7_decoupling"
    )
# --- Phase 8 ---
elif phase == "Phase 8 - Metadata & Behavioral Cloaking":
    st.markdown("### 🕵️ Phase 8 – Metadata & Behavioral Cloaking")
    st.markdown("This phase focuses on reducing metadata exposure and behavior fingerprinting.")

    phase8_tasks = [
        "Use Firefox containers for identity segmentation",
        "Rotate user agents with extensions like Chameleon",
        "Deploy MAC address randomization before connecting",
        "Use hardened OS environments (e.g., Tails, Qubes)",
        "Disable app telemetry, voice input, and activity tracking",
        "Spoof geolocation using browser extensions",
        "Use separate VMs or browser profiles per compartment"
    ]

    for task in phase8_tasks:
        if st.checkbox(task, key=task):
            log_checkbox("Phase 8", task)
            generate_gpt_overlay("Metadata Cloaking", task, instructor=(user_type == "Instructor"))

# --- Phase 9 ---
elif phase == "Phase 9 - Digital Footprint Intelligence (DFI) Feedback Loops":
    st.markdown("### 📊 Phase 9 – DFI Feedback Loops")
    st.markdown("This phase emphasizes measuring your footprint and detecting reemerging exposure.")

    phase9_tasks = [
        "Re-scan people search engines monthly",
        "Monitor for re-listed data using Kanary/Optery",
        "Set Google Alerts for full name, phone, and address",
        "Check if leaked emails are reused or scraped",
        "Review browser/device fingerprint results weekly",
        "Audit metadata leakage from installed extensions"
    ]

    for task in phase9_tasks:
        if st.checkbox(task, key=task):
            log_checkbox("Phase 9", task)
            generate_gpt_overlay("Digital Footprint Monitoring", task, instructor=(user_type == "Instructor"))
   
    if tactic:
        generate_gpt_overlay("Cross-Platform Ecosystem", tactic, instructor=(user_type == "Instructor"))

run_ghost_gpt(phase)

if user_type in ["Instructor", "Field Op"]:
    run_instructor_injector()

export_log()
