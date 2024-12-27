# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 11:17:06 2024

@author: CK
"""

import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="Frank Cafe", page_icon="🍔", layout="wide")

    # Header Section
    st.title("Frank Cafe")
    st.subheader("Where Flavors Meet Comfort")

    # About Us Section
    st.header("About Us")
    st.write(
        "Frank Cafe is your cozy neighborhood coffee spot in the heart of Malaysia, "
        "dedicated to serving freshly brewed coffee, delicious meals, and warm hospitality. "
        "At Frank Cafe, we believe in creating memorable experiences through our exceptional food, "
        "inviting ambiance, and genuine service."
    )

    # Other Sections...

    # Conversation Widget Section
    st.header("Conversation with Us")
    st.write(
        "Have questions or need assistance? Chat with our virtual assistant below!"
    )

    # Embedding the ElevenLabs Widget
    widget_code = '''
    <elevenlabs-convai agent-id="JaskEOvIC4gyY5aqXpAL"></elevenlabs-convai>
    <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
    '''
    components.html(widget_code, height=400)

    # Footer
    st.markdown("---")
    st.write(
        "Come and experience the warm vibes and delightful flavors at Frank Cafe! "
        "We look forward to welcoming you."
    )

if __name__ == "__main__":
    main()
