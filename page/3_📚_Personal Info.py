import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.title("Personal Info")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_coding = load_lottieurl("https://lottie.host/03ee82d1-a25f-453d-a094-3850d964a340/izzaPyU5n1.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Personal Info")
        st.write("##")
        st.write(
            """
            On my Webpage I am explaining about myself:
            - Name: James Carl Edradan Bituin
            - Age: 18 years old
            - Address: Brgy. Poctoy, Surigao City
            - Birth Place: Surigao City, Surigao Del Norte
            - Graduated in J.R. Clavero Memorial Elementary School
            - Graduated in Surigao del Norte National High School
            - Currently at Surigao del Norte State University as a 1st year collage
            - Course: BSCpE - Bachelor of Science in Computer Engineering
            """
            )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
