import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Multipage App",
    page_icon="tada",
)

st.title("Main Page")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_coding = load_lottieurl("https://lottie.host/03ee82d1-a25f-453d-a094-3850d964a340/izzaPyU5n1.json")

with st.container():
    st.subheader("Hi, I am James Carl :wave:")
    st.title("Exploring About My Life")
    st.write("Let's talk about myself so come on let's go!!!")

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

            If your curious about me, try adding me in facebook so we can communicate to each other. If there's something you want to know about myself. Take care!!!
            """
            )
        st.write("[Facebook >]https://www.facebook.com/jamecarl.bituin/")
        st.write("Contact me: jamescarlbituin017@gmail.com")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
