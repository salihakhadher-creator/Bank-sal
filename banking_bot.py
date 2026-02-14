import streamlit as st
from mistralai import Mistral

# Initialize Streamlit page config
st.set_page_config(page_title="Banking Bot", layout="wide")

# Initialize Mistral client with API key
api_key = "3CCVJBzyN6vp93lqdrIxBX1OZavAPpal"
client = Mistral(api_key=api_key)

# App title and description
st.title("🏦 Banking Bot")
st.markdown("---")
st.write("Welcome to the Banking Bot! Ask me anything about banking services, account management, loans, and more.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm your banking assistant. How can I help you today? I can help with account inquiries, transaction information, loan details, credit card services, and general banking questions."
        }
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if user_input := st.chat_input("Type your banking question here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get response from Mistral
    try:
        # Prepare system message for banking context
        system_message = """You are a professional banking assistant with expertise in:
- Account management and services
- Online banking and digital payments
- Loans and credit products
- Investment and savings options
- Credit cards and debit cards
- Transaction assistance
- Banking security and fraud prevention

Provide helpful, accurate, and professional responses to all banking-related inquiries. 
If a question is outside banking scope, politely redirect the conversation back to banking topics."""
        
        # Call Mistral API with conversation history
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "system", "content": system_message},
                *st.session_state.messages
            ],
            max_tokens=1024,
            temperature=0.7
        )
        
        # Extract assistant response
        assistant_message = response.choices[0].message.content
        
        # Add assistant message to history
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(assistant_message)
    
    except Exception as e:
        st.error(f"Error communicating with Mistral API: {str(e)}")

# Sidebar with additional information
st.sidebar.title("About")
st.sidebar.write("""
**Banking Bot v1.0**

Powered by Mistral AI's Large Language Model using the Mistral API.

This bot can assist with:
- General banking inquiries
- Account information
- Transaction queries
- Loan information
- Credit card services
- Financial advice
""")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Banking Bot - Powered by Mistral AI")
