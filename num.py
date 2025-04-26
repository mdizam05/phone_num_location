import streamlit as st
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

st.title("🔢Phone Numbers Location")
number = st.text_input("Enter your Number: ")
if number:
    try:
        x = phonenumbers.parse(number, None)
        st.write("🌐Country: ", geocoder.description_for_number(x, "en"))
        st.write("🗃️Service Provider: ", carrier.name_for_number(x, "en"))
    except Exception as e:
        st.error("❌Invalid phone number")

st.sidebar.write("⬇️Some examples of Numbers are: ")
st.sidebar.write("Pakistan: +92 ")
st.sidebar.write("United Kingdom: +44")
st.sidebar.write("Mexico: +52")
st.sidebar.write("Australia: +61")
st.sidebar.write("Saudi Arabia: +966")
st.sidebar.write("United Arab Emirates: +971")
st.sidebar.write("Nigeria: +234")
st.sidebar.write("Egypt: +20")
st.sidebar.write("India: +91")







