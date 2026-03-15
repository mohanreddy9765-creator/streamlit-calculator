import streamlit as st
import math

st.set_page_config(page_title="Advanced Calculator", layout="centered")

st.title("🧮 Advanced Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to update expression
def update_expression(value):

    if value == "C":
        st.session_state.expression = ""

    elif value == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]

    elif value == "=":
        try:
            expr = st.session_state.expression
            expr = expr.replace("×", "*").replace("÷", "/").replace("^", "**")
            result = eval(expr)
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"

    elif value == "√":
        try:
            expr = st.session_state.expression
            expr = expr.replace("×", "*").replace("÷", "/")
            result = math.sqrt(eval(expr))
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"

    elif value == "x²":
        try:
            expr = st.session_state.expression
            expr = expr.replace("×", "*").replace("÷", "/")
            result = eval(expr) ** 2
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"

    else:
        if st.session_state.expression == "Error":
            st.session_state.expression = ""
        st.session_state.expression += value

# Display
st.markdown(f"### {st.session_state.expression}")
# Calculator buttons
buttons = [
    ["(", ")", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "^"]
]
for r, row in enumerate(buttons):
    cols = st.columns(4)
    for c, btn in enumerate(row):

        display = btn

        if btn == "+":
            display = "➕"
        elif btn == "-":
            display = "➖"
        elif btn == "÷":
            display = "➗"
        elif btn == "×":
            display = "✖️"

        cols[c].button(
            display,
            key=f"btn_{r}_{c}",
            use_container_width=True,
            on_click=update_expression,
            args=(btn,)
        )
    

# Extra operations
col1, col2 = st.columns(2)

if col1.button("√", use_container_width=True):
    update_expression("√")

if col2.button("x²", use_container_width=True):
    update_expression("x²")

# Clear and backspace
c1, c2 = st.columns(2)

c1.button(
    "C",
    key="clear",
    use_container_width=True,
    on_click=update_expression,
    args=("C",)
)

if c2.button("⌫", use_container_width=True):
    update_expression("⌫")