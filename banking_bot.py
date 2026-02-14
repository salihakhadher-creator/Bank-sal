"""
Banking Bot using Mistral AI
A conversational banking assistant powered by Mistral's largest model
"""

import streamlit as st
from mistralai import Mistral
from config import (
    MISTRAL_API_KEY,
    MISTRAL_MODEL,
    MISTRAL_MAX_TOKENS,
    MISTRAL_TEMPERATURE,
    BANKING_SYSTEM_PROMPT,
    APP_TITLE,
    APP_PAGE_TITLE,
    APP_ICON,
    APP_LAYOUT,
    CHAT_INPUT_PLACEHOLDER,
    validate_config
)

# Validate configuration
try:
    validate_config()
except ValueError as e:
    st.error(f"Configuration Error: {str(e)}")
    st.stop()

# Initialize Streamlit page config
st.set_page_config(
    page_title=APP_PAGE_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT
)

# Title
st.title(APP_TITLE)
st.markdown("---")

# Initialize Mistral client
@st.cache_resource
def get_mistral_client():
    return Mistral(api_key=MISTRAL_API_KEY)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input(CHAT_INPUT_PLACEHOLDER)

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get response from Mistral
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            client = get_mistral_client()
            
            # Prepare messages for API
            messages = [
                {
                    "role": "system",
                    "content": BANKING_SYSTEM_PROMPT
                }
            ]
            
            # Add conversation history
            for msg in st.session_state.messages[:-1]:  # Exclude the current user message we just added
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            
            # Add the current user message
            messages.append({
                "role": "user",
                "content": user_input
            })
            
            try:
                # Call Mistral API
                response = client.chat.complete(
                    model=MISTRAL_MODEL,
                    messages=messages,
                    max_tokens=MISTRAL_MAX_TOKENS,
                    temperature=MISTRAL_TEMPERATURE
                )
                
                assistant_message = response.choices[0].message.content
                st.markdown(assistant_message)
                
                # Add assistant message to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
            except Exception as e:
                st.error(f"Error communicating with Mistral AI: {str(e)}")

# Sidebar with additional features
with st.sidebar:
    st.markdown("### 📚 About This Bot")
    st.markdown(f"""
    This banking bot uses **{MISTRAL_MODEL}** to provide:
    - 24/7 Customer Support
    - Banking Information
    - Account Assistance
    - Financial Guidance
    
    **Note:** For real account transactions or sensitive operations, 
    please contact your bank directly.
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("#### 💡 Sample Questions")
    st.markdown("""
    - What's a good savings strategy?
    - How do I transfer money?
    - What are your loan options?
    - What fees do you charge?
    - How do I improve my credit score?
    """)
