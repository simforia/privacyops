import openai
import streamlit as st

# Set your OpenAI API key (secure this in production)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.subheader("🧠 Ghost Protocol - GPT Privacy Advisor")

# User input prompt
user_input = st.text_area("Ask Ghost Protocol for help with any privacy task:")

if st.button("Run GPT Advisor"):
    if user_input.strip() == "":
        st.warning("Enter a question or task to proceed.")
    else:
        with st.spinner("Ghost Protocol is analyzing..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are Ghost Protocol, a tactical privacy advisor from Simforia. Help the user erase their digital footprint and protect their identity through strategic data removal, cover identity creation, and surveillance countermeasures."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.6,
                max_tokens=600
            )
            st.success("Response from Ghost Protocol:")
            st.write(response.choices[0].message.content)  
# GPT-4 integrated – Simforia PrivacyOps
