
import streamlit as st
from salter import marangoni_salter, marangoni_deflator

# Large, Bold Title for high visibility
st.markdown("# *SER ALIADO: PRIVATE CHAT*")
st.markdown("### *WRITTEN IN WATER*")

# The Message Input box
user_msg = st.text_input("Type your message to a friend:")

if user_msg:
    # 1. Salt the message (The Marangoni Effect)
    salted = marangoni_salter(user_msg)
    
    st.write("---")
    st.markdown("### *PROTECTED DATA (What scrapers see):*")
    st.code(salted)
    
    # 2. De-flate the message (The Truth)
    st.write("---")
    if st.button("REVEAL ORIGINAL MESSAGE"):
        original = marangoni_deflator(salted)
        # Display the result in Large Bold text
        st.write(f"## *{original}*")
from flask import Flask, request
import threading
import webbrowser

# This is the background server for Tasker
app_listener = Flask(__name__)

@app_listener.route('/call_event', methods=['POST'])
def receive_call():
    # Grabs the caller's number from the phone
    caller_number = request.args.get('number')
    print(f"James Byron: New call detected from {caller_number}")
    
    # Replace the zeros with your actual WhatsApp number
    whatsapp_url = f"https://wa.me/4129807347?text=Hi,%20James%20Byron%20here.%20I'm%20screening%20calls%20for%20my%20partner."
    
    # This automatically opens the chat link on your Mac
    webbrowser.open(whatsapp_url)
    return "OK", 200

# This keeps the listener running alongside Ser Aliado
def run_listener():
    app_listener.run(host='0.0.0.0', port=5000)

threading.Thread(target=run_listener, daemon=True).start()