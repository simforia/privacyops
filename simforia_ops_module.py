import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
GPT_MODEL = "gpt-4"  # ✅ Model fixed and scoped correctly

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
            model=GPT_MODEL,
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

    if tactic:
        generate_gpt_overlay(broker, tactic, instructor)

def log_checkbox(phase, task_name):
    if "simforia_log" not in st.session_state:
        st.session_state.simforia_log = []

    st.session_state.simforia_log.append({
        "Phase": phase,
        "Task": task_name,
        "Timestamp": datetime.datetime.now().isoformat()
    })

def trigger_inject_alert(message):
    st.warning(f"🚨 Inject Triggered: {message}")

def export_log():
    if st.button("📥 Export Simforia Log"):
        df = pd.DataFrame(st.session_state.simforia_log)
        st.download_button(
            "Download Log as CSV",
            df.to_csv(index=False),
            file_name="simforia_privacy_log.csv",
            mime="text/csv"
        )
