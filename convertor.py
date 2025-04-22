# Build a Google Unit Converter using Python and Streamlit
import streamlit as st

# ----- Custom CSS Styling -----
st.markdown("""
<style>
body {
    background-color: #1e1e2f;
    color: white;
}
.stApp {
    background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
}
h1 {
    text-align: center;
    font-size: 36px;
    color: white;
}
.stButton>button {
    background: linear-gradient(45deg, #0b5394, #351c75);
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 10px;
    transition: 0.3s;
    box-shadow: 0px 5px 15px rgba(0,201,255,0.4);
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg, #92fe9d, #00c9ff);
    color: black;
}
.result-box {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 10px;
    margin-top: 20px;
    box-shadow: 0px 5px 15px rgba(0,201,255,0.3);
}
.footer {
    text-align: center;
    font-size: 14px;
    color: #666;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ----- App Header -----
st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert units with our intuitive unit converter.")

# ----- Sidebar -----
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet", "Inches", "Centimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet", "Inches", "Centimeters"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Pounds", "Grams", "Ounces", "Milligrams"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Pounds", "Grams", "Ounces", "Milligrams"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# ----- Conversion Functions -----
def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters': 1,
        'Kilometers': 0.001,
        'Centimeters': 100,
        'Miles': 0.000621371,
        'Feet': 3.28084,
        'Inches': 39.3701,
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1,
        'Pounds': 2.20462,
        'Grams': 1000,
        'Ounces': 35.274,
        'Milligrams': 1000000
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9 / 5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "Kelvin":
            return (value + 459.67) * 5 / 9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return value * 9 / 5 - 459.67

# ----- Convert Button -----
if st.button("🤖 Convert"):
    if from_unit == to_unit:
        result = value
    elif conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)

    st.markdown(f"""
    <div class="result-box">
    <h2>Result</h2>
    <p>{value} {from_unit} is equal to {result:.4f} {to_unit}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='footer'>Developed by Syed-Ahsan😎</div>", unsafe_allow_html=True)

