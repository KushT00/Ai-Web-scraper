import streamlit as st
from scrape import (
    scrap_website,
    split_dom_content,
    extract_body_content,
    clean_body_content)
from parse import parse_with_ollama

st.title("AI Web Scrapper")

url=st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
   
    st.write("Scraping Data")
    result=scrap_website(url)
    body_content=extract_body_content(result)
    clean_Body=clean_body_content(body_content)
    st.session_state.dom_content=clean_Body

    with st.expander("View Dom Content"):
        st.text_area("Dom content", clean_Body, height=300)
   

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

             # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)