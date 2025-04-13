import streamlit as st
import datetime

def run_instructor_injector():
    st.divider()
    st.subheader("🎯 Instructor Mode - Tactical Inject & Coaching Log")

    st.markdown("Use this panel to simulate real-world privacy challenges and capture how users respond.")

    injects = {
        "Doxxing": "You’ve been doxxed on 4chan with home address exposure.",
        "Alias Compromise": "A family member's identity has been tied to your alias.",
        "OpSec Failure": "Burner phone tied to your real identity through call pattern analysis.",
        "Re-Exposure": "Broker site has re-listed your profile after previous suppression.",
        "Facial Recognition Leak": "Stalker used old social images to reverse match your alias via PimEyes."
    }

    selected_inject = st.selectbox("Select an inject scenario:", list(injects.keys()))
    inject_text = injects[selected_inject]

    st.code(inject_text, language="markdown")

    # Optional GPT prompt override
    auto_prompt = st.checkbox("Auto-fill this inject into GPT advisor prompt?")
    if auto_prompt:
        st.session_state["gpt_input"] = inject_text

    # Coach feedback section
    st.markdown("### 🧾 Coaching Log")
    student_response = st.text_area("Student Response", height=150)
    instructor_notes = st.text_area("Instructor Comments", height=150)

    # Export full log to markdown
    if st.button("📥 Export Inject Session Log (.md)"):
        log_md = f"""# 🎯 Simforia Inject Challenge Log

**Date:** {datetime.date.today()}
**Inject Type:** {selected_inject}
**Inject Description:** {inject_text}

---

## Student Response
{student_response}

---

## Instructor Comments
{instructor_notes}
"""
        st.download_button(
            label="Download .md File",
            data=log_md,
            file_name=f"simforia_inject_log_{datetime.date.today()}.md",
            mime="text/markdown"
        )