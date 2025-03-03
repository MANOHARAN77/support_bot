import streamlit as st
from fuzzywuzzy import process

# Predefined FAQ responses
faq_responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what is your name": "I'm your Customer Support Bot 🤖",
    "return policy": "Our return policy allows returns within 30 days with a receipt.",
    "shipping time": "Shipping typically takes 3-5 business days.",
    "contact support": "You can reach our support at support@example.com",
    "bye": "Goodbye! Have a great day! 😊"
}

# Function to get best matching response
def chatbot_response(user_input):
    user_input = user_input.lower()
    best_match, score = process.extractOne(user_input, faq_responses.keys())

    if score > 60:  # Confidence threshold
        return faq_responses[best_match]
    else:
        return "I'm sorry, I don't understand. Can you rephrase your question?"

# Streamlit UI
st.title("🛎️ Customer Support Chatbot")
st.write("Ask me anything about our service!")

user_input = st.text_input("Type your message here:")
if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"🤖 Bot: {response}")
    else:
        st.write("Please enter a message.")
