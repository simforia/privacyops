import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_gpt_overlay(broker_name, tactic, instructor=False):
    system = (
        "You are Ghost Protocol, a tactical privacy advisor and red cell instructor."
        if instructor else
        "You are Ghost Protocol, a privacy AI helping users delete, remove, or obfuscate their data from surveillance systems."
    )

    prompt = f"How to {tactic} your data from {broker_name}. Give step-by-step instructions and note any risks, verification needs, or common pitfalls."

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

    generate_gpt_overlay(broker, tactic, instructor)

def run_broker_warroom(is_instructor=False):
    st.title("🎯 Data Broker War Room")

    brokers = [
        {
            "name": "Acxiom (LiveRamp)",
            "desc": "Claims over 3,000 data points per person, used in marketing & profiling at global scale.",
            "url": "https://liveramp.com/opt_out/"
        },
        {
            "name": "Experian",
            "desc": "Credit bureau also selling behavioral and marketing data.",
            "url": "https://www.experian.com/privacy/opting-out"
        },
        {
            "name": "LexisNexis",
            "desc": "Government-linked, used for legal, law enforcement, and commercial surveillance.",
            "url": "https://privacyportal.onetrust.com/webform/4b5d2a5b-8f4d-403b-8bfb-e5a0cf157d68/8c5037ba-e72a-4e10-b71d-79d1b9e4d262"
        },
        {
            "name": "Spokeo",
            "desc": "People search aggregator known for persistent re-indexing.",
            "url": "https://www.spokeo.com/optout"
        },
        {
            "name": "SafeGraph",
            "desc": "Location data vendor with ties to government and law enforcement.",
            "url": "https://www.safegraph.com/privacy"
        },
        {
            "name": "PeekYou",
            "desc": "Web content aggregator that builds composite personal profiles.",
            "url": "https://www.peekyou.com/about/contact/"
        }
    ]

    for broker in brokers:
        render_broker_overlay(broker["name"], broker["desc"], broker["url"], instructor=is_instructor)