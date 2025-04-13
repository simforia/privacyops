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
        # 💬 Simforia GPT Conversation Starters (Civilian-Friendly)
    st.markdown("### 💬 Suggested Conversation Starters")
    st.markdown("""
    - How do I remove my personal data from the internet?  
    - Can you help me audit my online exposure risk?  
    - What’s the best way to shield my identity from tracking?  
    - How do I set up secure communication channels?  
    - Walk me through a phased digital cleanup plan.  
    - Show me how to create a compartmented identity.  
    - How can I detect if I’m being digitally surveilled?  
    - What tools reduce metadata leakage?  
    - Build a data broker opt-out checklist.  
    - Help me train others to do digital cleanup safely.  
    """)
    st.markdown("---")
    st.markdown("🧠 [Access Ghost Protocol GPT](https://chatgpt.com/g/g-67fbb978fa4c8191b8a9c0c1cc13afca-simforia-intelligence-group-ghost-protocol)")
            # ✅ Add this new option:
    advanced_mode = st.checkbox("🔬 Enable Advanced Phases", value=False)
    instructor_mode = st.checkbox("🎓 Instructor Mode", value=False)
    st.session_state["is_instructor"] = instructor_mode
    st.markdown("---")
    if st.session_state.get("is_instructor") or advanced_mode:
    st.markdown("🛡️ **Phase BLACK – Active Surveillance Countermeasures (ASC)**")
    phase_black_trigger = st.checkbox("🔥 Enter Phase BLACK")
    st.session_state["phase_black_active"] = phase_black_trigger
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

if phase == "Phase 1 – Exposure Audit":
    ...
elif phase == "Phase 0 – Threat Modeling & Persona Calibration":
    ...

    st.markdown("### 🧠 Phase 0 – Threat Modeling & Persona Calibration")
    st.radio("Adversary Type", ["Script Kiddie", "Criminal Org", "Corporate", "Nation-State"], key="adversary_type")
    st.radio("Objective", ["Obscurity", "Anonymity", "Untraceability"], key="op_objective")
    st.radio("Persona Model", ["Compartmentalized", "Fused", "Rotational"], key="persona_model")

elif phase == "Phase 1.5 – Infrastructure & Access Hygiene":
    st.markdown("### 🧱 Phase 1.5 – Infrastructure & Access Hygiene")
    tasks = [
        "Use custom domain aliases with Proton/Skiff",
        "De-Google phone (GrapheneOS)",
        "Use router-based VPNs or Tor bridges",
        "MAC spoofing and telemetry hardening",
        "Randomize login timing and browser patterns"
    ]
    for task in tasks:
        if st.checkbox(task, key=f"p15_{task}"):
            log_checkbox("Phase 1.5", task)
    generate_gpt_overlay("Infrastructure Hygiene", task, instructor=st.session_state["is_instructor"])

elif phase == "Phase 2.5 – Legal & Financial Cloaking":
    st.markdown("### 🛠 Phase 2.5 – Legal & Financial Cloaking")
    tasks = [
        "Freeze credit reports (Equifax/TransUnion/Experian)",
        "Opt-out of LexisNexis, CoreLogic, SageStream",
        "Suppress voter and DMV registration leaks",
        "Register LLC or trust to anonymize infrastructure",
        "File FOIA requests for public record removal"
    ]
    for task in tasks:
        if st.checkbox(task, key=f"p25_{task}"):
            log_checkbox("Phase 2.5", task)
    generate_gpt_overlay("Legal Cloaking", task, instructor=st.session_state["is_instructor"])

elif phase == "Phase 4.5 – Synthetic Ecosystem & Decoys":
    st.markdown("### 🕸 Phase 4.5 – Synthetic Ecosystem & Decoys")
    tasks = [
        "Create AI-generated decoy profiles",
        "Seed false data across forums and blogs",
        "Construct mirrored but altered social graphs",
        "Vary behavioral patterns across synthetic identities"
    ]
    for task in tasks:
        if st.checkbox(task, key=f"p45_{task}"):
            log_checkbox("Phase 4.5", task)
    generate_gpt_overlay("Synthetic Identity", task, instructor=st.session_state["is_instructor"])

elif phase == "Phase 5.5 – Burn Network Protocol":
    st.markdown("### 📉 Phase 5.5 – Burn Network Protocol")
    st.warning("⚠️ Initiating this phase means a full identity reset and wiping prior infrastructure.")
    if st.button("💥 Initiate Burn Protocol"):
        st.session_state["simforia_log"] = []
        st.success("All logs wiped. Begin rebuilding a clean digital identity.")

elif phase == "Phase 9.5 – Behavioral Feedback AI Loop":
    st.markdown("### 🔬 Phase 9.5 – Behavioral Feedback AI Loop")
    user_input = st.text_area("Describe your recent activities or privacy concern:")
    if st.button("Run Behavioral Threat Model"):
        from openai import OpenAI
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are Ghost Protocol. Analyze the user's digital behavior and simulate how an adversary might track or correlate their metadata."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=700
        st.markdown(response.choices[0].message.content)

elif phase == "Optional Phase – DNA & Biometric Spoof Prevention":
    st.markdown("### 🧬 DNA & Biometric Spoof Prevention")
    tasks = [
        "Disassociate biometrics from login systems",
        "Check if facial photos are indexed by AI datasets",
        "Avoid genealogy platforms that link family trees",
        "Obfuscate facial data using distortion overlays"
    ]
    for task in tasks:
        if st.checkbox(task, key=f"bio_{task}"):
            log_checkbox("Biometrics", task)
    generate_gpt_overlay("Biometric Spoofing", task, instructor=st.session_state["is_instructor"])


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
    generate_gpt_overlay("Exposure Audit", task, instructor=st.session_state["is_instructor"])

elif phase == "Phase 2 - Broker Opt-Out":
    st.markdown("### 📤 Broker Opt-Out Tracker")
    is_instructor = user_type == "Instructor"

    render_broker_overlay(
        broker="Spokeo",
        description="Aggregates social media and public records data.",
        opt_out_url="https://www.spokeo.com/optout",
        instructor=is_instructor

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
    generate_gpt_overlay("Lockdown Protocols", task, instructor=st.session_state["is_instructor"])

    with st.expander("🛒 Amazon Obfuscation Playbook (Click to Expand)", expanded=True):
        render_amazon_obfuscation_section()

elif phase == "Phase 4 - Cover Identity":
    st.markdown("### 🪪 Cover Identity Generator")
    identity_fields = [
        "Alias Name", "Fake DOB", "Region/City", "Decoy Job Title", "Burner Email", "Burner Phone"
    ]
    for field in identity_fields:
        st.text_input(field)
    generate_gpt_overlay("Cover Identity", field, instructor=st.session_state["is_instructor"])

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
    generate_gpt_overlay("Maintenance", task, instructor=st.session_state["is_instructor"])

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
    generate_gpt_overlay("Surveillance Economy", task, instructor=st.session_state["is_instructor"])

elif phase == "Phase 7 - Cross-Platform Identity Decoupling":
    st.markdown("### 🧬 Cross-Platform Identity Decoupling")
    tactic = st.radio(
        "Select your decoupling strategy:",
        ["Metadata Decoupling", "Account Segmentation", "Full Identity Partitioning"],
        key="phase7_strategy"
    if tactic:
        log_checkbox("Phase 7", tactic)
    generate_gpt_overlay("Cross-Platform Ecosystem", tactic, instructor=st.session_state["is_instructor"])

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
    generate_gpt_overlay("Metadata Cloaking", task, instructor=st.session_state["is_instructor"])

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
    generate_gpt_overlay("Digital Footprint Monitoring", task, instructor=st.session_state["is_instructor"])

# --- PHASE BLACK TRIGGER ---
if st.session_state.get("phase_black_active"):
    st.markdown("## 🛡️ PHASE BLACK – Active Surveillance Countermeasures (ASC)")
    st.error("🚨 This environment is now operating under Phase BLACK protocols. Surveillance indicators detected.")

    with st.expander("🔍 Detection & Validation"):
        st.markdown("- Behavioral anomalies (phantom notifications, lag, geolocation drift)")
        st.markdown("- RF anomalies (sudden signal strength shifts)")
        st.markdown("- Third-party recon indicators (OSINT pings, background checks)")

    with st.expander("🧰 Counter-Surveillance Toolkit"):
        st.markdown("- RF Detector (T10 Sweeper, Kestrel TSCM)")
        st.markdown("- IMSI Catcher Detector (Sitch, Crocodile Hunter)")
        st.markdown("- Power signature analysis")
        st.markdown("- Offline keyloggers for integrity checking")

    response_action = st.selectbox("🧨 Select Phase BLACK Response Option", [
        "Compartment Wipe",
        "OpSec Escalation",
        "Cover Identity Activation",
        "AI-Driven Disinfo Bloom"
    ])

    if response_action:
        generate_gpt_overlay("Phase BLACK", response_action, instructor=True)

    with st.expander("🧭 Strategic Safeguards"):
        st.markdown("- Maintain an Escalation Tree (Green ➝ Amber ➝ Red ➝ BLACK)")
        st.markdown("- Use air-gapped encrypted USB comms kits")
        st.markdown("- Store continuity backups (wallets, aliases, offline comms)")
        st.markdown("- Initiate Synthetic Pattern Noise to confuse surveillance analytics")


run_ghost_gpt(phase)

if user_type in ["Instructor", "Field Op"]:
    run_instructor_injector()

export_log()
