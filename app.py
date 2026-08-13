import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml"
}

text = st.text_area("Enter text:")

source_language = st.selectbox(
    "Select source language:",
    list(languages.keys())
)

target_language = st.selectbox(
    "Select target language:",
    list(languages.keys())
)

if st.button("Translate"):
    if text:
        translated_text = GoogleTranslator(
            source=languages[source_language],
            target=languages[target_language]
        ).translate(text)

        st.session_state["translated_text"] = translated_text
        st.session_state["target_language"] = languages[target_language]

    else:
        st.warning("Please enter some text.")

if "translated_text" in st.session_state:

    translated_text = st.session_state["translated_text"]
    target = st.session_state["target_language"]

    st.success("Translation completed!")

    st.text_area(
        "Translated text:",
        translated_text
    )

    # Copy Translation
    copy_button = f"""
    <script>
    function copyText() {{
        navigator.clipboard.writeText({translated_text!r});
        alert("Translation copied!");
    }}
    </script>

    <button onclick="copyText()">
    📋 Copy Translation
    </button>
    """

    st.components.v1.html(copy_button, height=60)

 
