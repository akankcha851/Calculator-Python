import streamlit as st

# Page configuration
st.set_page_config(page_title="My Calculator")

# ---------- CSS STYLING ----------
st.markdown("""
<style>
.calculator {
    max-width: 320px;
    margin: auto;
    padding: 20px;
    border-radius: 15px;
    background-color: #f5f5f5;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
}

.display input {
    font-size: 28px !important;
    text-align: right;
    height: 60px;
}

button {
    width: 100%;
    height: 55px;
    font-size: 20px !important;
    border-radius: 10px;
}

.operator button {
    background-color: #ff9800 !important;
    color: white !important;
}

.equal button {
    background-color: #4CAF50 !important;
    color: white !important;
}

.clear button {
    background-color: #f44336 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "expression" not in st.session_state:
    st.session_state.expression = ""

# ---------- FUNCTIONS ----------
def press(key):
    st.session_state.expression += str(key)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Undefined"

# ---------- UI ----------
st.markdown('<div class="calculator">', unsafe_allow_html=True)
st.markdown("### 🧮 My Calculator")

st.text_input(
    "",
    st.session_state.expression,
    key="display",
    disabled=True,
    label_visibility="collapsed"
)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "+", "="]
]

for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if btn in ["/", "*", "-", "+"]:
            cols[i].markdown('<div class="operator">', unsafe_allow_html=True)
            cols[i].button(btn, on_click=press, args=(btn,))
            cols[i].markdown('</div>', unsafe_allow_html=True)

        elif btn == "=":
            cols[i].markdown('<div class="equal">', unsafe_allow_html=True)
            cols[i].button(btn, on_click=calculate)
            cols[i].markdown('</div>', unsafe_allow_html=True)

        else:
            cols[i].button(btn, on_click=press, args=(btn,))

st.markdown('<div class="clear">', unsafe_allow_html=True)
st.button("C", on_click=clear)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

