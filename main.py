import streamlit as st

def replace_punctuation(text):
    if not text:
        return ""

    # 1. Handle multi-char first
    text = text.replace('……', '...')
    text = text.replace('——', '--')

    # 2. Handle single-char
    punctuation_map = {
        '。': '. ',
          '，': ', ',
            '、': ', ',
              '？': '? ',
                '！': '! ',
                '：': ': ',
                  '；': '; ',
                    '“': '" ',
                      '”': '" ',
                        '‘': "' ",
                        '’': "'"
    }
    
    table = str.maketrans(punctuation_map)
    text = text.translate(table)
    text = text.replace('  ', ' ')  # Clean up double spaces if any
    return text

# --- App Layout ---
st.set_page_config(page_title="Punctuation Switcher", page_icon="🔀")

# CSS to force text wrapping in st.code
st.markdown("""
<style>
    code { white-space: pre-wrap !important; }
</style>
""", unsafe_allow_html=True)

st.title("🔀 Chinese to English Punctuation Switcher")

st.info("Notice any punctuations not changing? Inform the developer to add more to the map.")

st.write("""**How to use this app:**""")
st.write("""
1. Paste your Chinese text into the text area.
2. Click the **Submit** button to convert the punctuation.
3. The converted text will appear below, ready to be copied.
         """)

with st.expander("🔀 **Punctuation Conversion Rules**", expanded=False):
    st.write("""
    - `。` → `. `  
    - `，` → `, `  
    - `、` → `, `  
    - `？` → `? `  
    - `！` → `! `  
    - `：` → `: `  
    - `；` → `; `  
    - `“` → `" `  
    - `”` → `" `  
    - `‘` → `' `  
    - `’` → `' `  
    - `……` → `...`  
    - `——` → `--`  
    """)

# Initialize session state for text input if it doesn't exist
if 'text_content' not in st.session_state:
    st.session_state.text_content = ""

def clear_text():
    st.session_state.text_content = ""

# Text Area linked to Session State
input_val = st.text_area(
    "Input Text", 
    height=200, 
    key="text_content", # Links this widget to st.session_state.text_content
    placeholder="Paste Chinese text here..."
)

# Buttons Layout
col1, col2 = st.columns([1, 5])

with col1:
    submit_clicked = st.button("Submit", type="primary")

with col2:
    st.button("Clear Text", on_click=clear_text)

# Logic: Show result if Submit is clicked OR if there is already text (live update)
# If you want it to ONLY run on click, use: `if submit_clicked and input_val:`
if input_val:
    converted_text = replace_punctuation(input_val)
    
    st.divider()
    st.subheader("Result")
    st.caption("Click the copy icon in the top right of the box below.")
    st.code(converted_text, language=None)