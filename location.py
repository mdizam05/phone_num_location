import streamlit as st
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def get_phone_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Check if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number format"
        
        # Get country information
        country = geocoder.description_for_number(parsed_number, "en")
        
        # Get carrier information (if available)
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        # Format the number in international format
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        
        return {
            "formatted_number": formatted_number,
            "country": country if country else "Unknown location",
            "carrier": service_provider if service_provider else "Unknown carrier"
        }
        
    except Exception as e:
        return f"Error: {str(e)}"

# Set up the Streamlit app
st.title("🔢Phone Number Location Finder")
st.write("Enter a phone number with country code to discover its location")

# Input for phone number
phone_input = st.text_input("Enter phone number: ")

# Check examples
st.sidebar.header("Example Numbers")
st.sidebar.write("+92 (Pakistan)")
st.sidebar.write("+52 (Mexico)")
st.sidebar.write("+1 (United States)")
st.sidebar.write("+91 (India)")

# Button to analyze the number
if st.button("Find Location"):
    if phone_input:
        result = get_phone_info(phone_input)
        
        if isinstance(result, dict):
            st.success("Phone number analysis completed!")
            
            # Create three columns
            col1, col2, col3 = st.columns(3)
            
            # Display the results
            with col1:
                st.metric("Formatted Number", result["formatted_number"])
            
            with col2:
                st.metric("Country/Location", result["country"])
            
            with col3:
                st.metric("Service Provider", result["carrier"])
                
        else:
            st.error(result)
    else:
        st.warning("Please enter a phone number")
# Add footer
st.markdown("---")
st.write("This app uses the phonenumbers library to identify the location of phone numbers.")