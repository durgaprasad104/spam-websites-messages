import streamlit as st
import re

# Function to check if a website is a government website
def is_government_website(url):
    # Define a list of government domains
    government_domains = [
        '.gov/', '.gov.in/', '.gov.uk/', '.gov.au/', '.gov.ca/', '.gov.nz/', '.gov.za/','.co.in/','edu.in/','.org.in/','ac.in/','.net.in/','.gen.in/','.gov', '.gov.in', '.gov.uk', '.gov.au', '.gov.ca', '.gov.nz', '.gov.za','.co.in','edu.in','.org.in','ac.in','.net.in','.gen.in'
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

# Streamlit app
def main():
    st.title("India Government Website & Spam Checker")

    st.write("#### Check if a website is india government-authorized")
    url = st.text_input("Enter website URL")
    if st.button("Check Website"):
        if url:
            if is_government_website(url):
                st.success(f"{url} is a india government-authorized website.")
            else:
                st.error(f"{url} is not a india government-authorized website.")

    st.write("\n---\n")

    st.write("# Check the messages is a spam ")
    message = st.text_area("Paste message here", height=100)
    if st.button("Check Message"):
        if message:
            if is_spam_message(message):
                st.error("This message appears to be spam.")
            else:
                st.success("This message is not spam.")

if __name__ == "__main__":
    main()
