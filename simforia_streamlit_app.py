import streamlit as st
import pandas as pd
import datetime

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
    st.checkbox("Setup SimpleLogin or AnonAddy aliases")
    st.checkbox("Create MySudo burner phone")
    st.checkbox("Freeze credit with all bureaus")
    st.checkbox("Install Mullvad VPN")
    st.checkbox("Harden Firefox with uBlock + PrivacyBadger")

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

st.info("Instructor mode, API integration, and GPT handoff coming in Phase 2 deployment.")

# --- GPT Chat Interface ---
st.divider()
st.subheader("🧠 Ghost Protocol - GPT Privacy Advisor")

user_input = st.text_area("Ask Ghost Protocol for help with any privacy task:")

if st.button("Run GPT Advisor"):
    if user_input.strip() == "":
        st.warning("Enter a question or task to proceed.")
    else:
        with st.spinner("Ghost Protocol is analyzing..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are Ghost Protocol, a tactical privacy advisor from Simforia. The user is currently working on {phase}. Help them erase their digital footprint and protect their identity."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.6,
                max_tokens=600
            )
            st.success("Response from Ghost Protocol:")
            st.write(response.choices[0].message.content)
