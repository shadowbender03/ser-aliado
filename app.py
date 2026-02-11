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
