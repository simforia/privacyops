from openai import OpenAI
import streamlit as st
import datetime

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def run_ghost_gpt(phase):
    st.divider()
    st.subheader("🧠 Ghost Protocol - GPT Privacy Advisor")

    user_input = st.text_area("Ask Ghost Protocol for help with any privacy task:", key="gpt_input")

    if st.button("Run GPT Advisor"):
        if user_input.strip() == "":
            st.warning("Enter a question or task to proceed.")
            return

        with st.spinner("Ghost Protocol is analyzing..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": f"You are Ghost Protocol, a tactical privacy advisor from Simforia. The user is currently working on {phase}. Provide detailed, actionable guidance based on that stage of privacy erasure."
                        },
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.6,
                    max_tokens=600
                )

                reply = response.choices[0].message.content
                st.success("Response from Ghost Protocol:")
                st.write(reply)

                # Generate a markdown export
                log_md = f"""## 🧠 Ghost Protocol GPT Log
**Date:** {datetime.date.today()}
**Phase:** {phase}
**User Input:**  
{user_input}

**Response:**  
{reply}
"""

                st.download_button(
                    label="📥 Download GPT Session Log (.md)",
                    data=log_md,
                    file_name=f"simforia_gpt_log_{datetime.date.today()}.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")
