import streamlit as st
from openai import OpenAI
import pandas as pd
from datetime import datetime

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# === Global log store ===
if 'simforia_log' not in st.session_state:
    st.session_state.simforia_log = []

# === Tactical Broker Overlay ===
def generate_gpt_overlay(broker_name, tactic, instructor=False):
    system = (
        "You are Ghost Protocol, a tactical privacy advisor and red cell instructor."
        if instructor else
        "You are Ghost Protocol, a privacy AI helping users delete, remove, or obfuscate their data from surveillance systems."
    )

    if tactic.lower() == "both (layered attack)":
        prompt = (
            f"You are Ghost Protocol. Execute a layered strategy to erase and obfuscate data from {broker_name}. "
            f"This includes formal deletion/removal steps and parallel misdirection (false trails, decoy submissions, etc.). "
            f"Outline both vectors clearly and include risks, timing, and signals of success."
        )
    else:
        prompt = f"How to {tactic.lower()} your data from {broker_name}. Give step-by-step instructions and note any risks, verification needs, or common pitfalls."

    with st.expander(f"🧠 {tactic.title()} Guidance from Ghost Protocol"):
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=600
        )
        st.markdown(response.choices[0].message.content)
    )

    with st.expander(f"🧠 {tactic.title()} Guidance from Ghost Protocol"):
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=600
        )
        st.markdown(response.choices[0].message.content)

def render_broker_overlay(broker, description, opt_out_url, instructor=False):
    st.markdown(f"### 🛰 {broker}")
    st.markdown(f"**Profile:** {description}")
    st.markdown(f"[🔗 Opt-Out Link]({opt_out_url})")

    tactic = st.radio(
        f"What do you want to do with your data on **{broker}**?",
        ["Delete/Remove", "Obfuscate", "Both (Layered Attack)"],
        key=broker
    )

    # Log selection
    st.session_state.simforia_log.append({
        "timestamp": str(datetime.utcnow()),
        "broker": broker,
        "tactic": tactic,
        "action_type": "broker_tactic"
    })

    generate_gpt_overlay(broker, tactic, instructor)

# === Checkbox Logger ===
def log_checkbox(phase, action_desc):
    st.session_state.simforia_log.append({
        "timestamp": str(datetime.utcnow()),
        "phase": phase,
        "action": action_desc,
        "action_type": "checkbox"
    })

# === Inject Challenge Simulator ===
def trigger_inject_alert(broker="Whitepages", level="critical"):
    st.warning(f"⚠️ Inject Alert: {broker} has relisted your profile. Reactivate your broker kill chain.")

    st.session_state.simforia_log.append({
        "timestamp": str(datetime.utcnow()),
        "inject": f"{broker} relisted warning",
        "severity": level,
        "action_type": "inject"
    })

# === Export Session Log ===
def export_log():
    if st.session_state.simforia_log:
        df = pd.DataFrame(st.session_state.simforia_log)
        st.download_button("💾 Download Session Log", df.to_csv(index=False), "simforia_log.csv", "text/csv")
    else:
        st.info("No activity logged yet.")
