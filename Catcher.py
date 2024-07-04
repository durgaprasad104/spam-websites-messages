import streamlit as st
import re

# Function to check if a website is a government website
def is_government_website(url):
    # Define a list of government domains
    government_domains = [
        '.nic.in','.gov', '.gov.in','gov.in', '.gov.uk', '.gov.au', '.gov.ca', '.gov.nz', '.gov.za','.co.in','edu.in','.org.in','ac.in','.net.in','.gen.in'
        # Add other government domains as needed
    ]
    
    # Check if the URL contains any part of the government domains
    for domain in government_domains:
        if domain in url:
            return True
    return False

# Function to check if a message is spam
def is_spam_message(message):
    # Define spam detection criteria (example)
    spam_keywords = [
        "lottery", "free", "money", "prize", "click here", "urgent"," job openings","contests ","promotional content"
        # Add more spam keywords as needed
    ]
    
    # Check if any spam keywords are present in the message
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
            return True
    return False

# Function to check if a number is authorized (e.g., hospitals, police stations)
def is_authorized_number(number):
    # Define authorized numbers (example)
    authorized_numbers = {
        "Emergency Services": ["911", "112", "999"],
        "Hospitals": ["100", "108"],
        "Police Stations": ["101", "100"],
        # Add more authorized numbers as needed
    }
    
    # Check if the number matches any authorized category
    for category, numbers in authorized_numbers.items():
        if number in numbers:
            return category
    return None

# Function to check if a phone number belongs to an authorized brand
def is_authorized_brand_number(number):
    # Define authorized brands and their phone numbers
    authorized_brand_numbers = {
        "Brand A": ["8001234567", "8009876543"],
        "Brand B": ["8001112222", "8003334444"],
        "Brand C": ["8005556666", "8007778888"],
        # Add more authorized brands and their numbers as needed
    }
    
    # Check if the number matches any authorized brand
    for brand, numbers in authorized_brand_numbers.items():
        if number in numbers:
            return brand
    return None

# Function to check if an email address is government authorized
def is_government_authorized_email(email):
    # Define authorized government domains
    authorized_domains = [
        ".gov", ".gov.in","gov.in", ".gov.uk", ".gov.au", ".gov.ca", ".gov.nz", ".gov.za",
        ".co.in", ".edu.in", ".org.in", ".ac.in", ".net.in", ".gen.in","nic.in",".nic.in"
        # Add more authorized domains as needed
    ]
    
    # Extract domain from email address
    parts = email.split('@')
    if len(parts) == 2:
        domain = parts[1]
        # Check if the domain ends with any of the authorized government domains
        for auth_domain in authorized_domains:
            if auth_domain in domain.lower():
                return True
    return False

# Function to check if an email content is spam
def is_email_spam(email_content):
    # Simplified spam detection for demo purposes
    # Check for common spam keywords in email content
    spam_keywords = [
        "lottery", "free", "money", "prize", "click here", "urgent"," job openings","contests ","promotional content"
        # Add more spam keywords as needed
    ]
    
    # Check if any spam keywords are present in the email content
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', email_content, re.IGNORECASE):
            return True
    return False

# Page for displaying project information
def home_page():
    st.title("Welcome to the Multi-Tool Checker App")
    st.write("""
    You can check the website or mail-ids or messages 
    if is it original or not:
    This app provides various tools for checking:
    - Government authorized websites
    - Spam messages
    - Authorized numbers (e.g., emergency services, hospitals, police stations)
    - Authorized brand phone numbers
    - Government authorized email addresses
    
    You can select a tool from the sidebar to get started.
    """)

# Page for checking government websites
def government_website_page():
    st.write("### Check if a website is indian government-authorized")
    url = st.text_input("Enter website URL")
    if st.button("Check Website"):
        if url:
            if is_government_website(url):
                st.success(f"{url} is a indian government-authorized website.")
            else:
                st.error(f"{url} is not a indian government-authorized website.")

# Page for checking spam messages
def spam_message_page():
    st.write("### Check if a message is spam")
    message = st.text_area("Paste message here", height=100)
    if st.button("Check Message"):
        if message:
            if is_spam_message(message):
                st.error("This message appears to be spam.")
            else:
                st.success("This message is not spam.")

# Page for checking authorized numbers
def authorized_number_page():
    st.write("### Check if a number is authorized")
    number = st.text_input("Enter number (e.g., emergency, hospital, police)")
    if st.button("Check Number"):
        if number:
            category = is_authorized_number(number)
            if category:
                st.success(f"{number} is an authorized {category} number.")
            else:
                st.error(f"{number} is not recognized as an authorized number.")

# Page for checking authorized brand phone numbers
def authorized_brand_number_page():
    st.write("### Check if a phone number belongs to an authorized brand")
    brand_number = st.text_input("Enter brand phone number")
    if st.button("Check Brand Number"):
        if brand_number:
            brand = is_authorized_brand_number(brand_number)
            if brand:
                st.success(f"{brand_number} is an authorized phone number for {brand}.")
            else:
                st.error(f"{brand_number} is not recognized as an authorized brand phone number.")

# Page for checking email content for government authorization and spam
def email_checker_page():
    st.write("### Check if an email address is indian government authorized and if email content is spam")
    email = st.text_input("Enter email address")
    email_content = st.text_area("Paste email content here", height=200)
    
    if st.button("Check Email"):
        if email:
            if is_government_authorized_email(email):
                st.success(f"{email} is a indian government authorized email address.")
            else:
                st.error(f"{email} is not a indian government authorized email address.")
        
        if email_content:
            if is_email_spam(email_content):
                st.error("This email content appears to be spam.")
            else:
                st.success("This email content is not spam.")

# Main function for the Streamlit app
def main():
    st.sidebar.title("Navigation")
    
    # Checkboxes for selecting pages (only one can be selected)
    selected_page = st.sidebar.radio(
        "Select a Tool",
        ["Home", "India Government Website Checker", "Spam Message Checker", "Authorized Number Checker",
         "Authorized Brand Number Checker", "Email Checker"]
    )

    # Display selected pages
    if selected_page == "Home":
        home_page()
    elif selected_page == "India Government Website Checker":
        government_website_page()
    elif selected_page == "Spam Message Checker":
        spam_message_page()
    elif selected_page == "Authorized Number Checker":
        authorized_number_page()
    elif selected_page == "Authorized Brand Number Checker":
        authorized_brand_number_page()
    elif selected_page == "Email Checker":
        email_checker_page()

    # Display developer name in the sidebar
    st.sidebar.write("\n---\n")
    st.sidebar.write("Developed by DP")

if __name__ == "__main__":
    main()
