import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("My Portfolio")
st.divider()

col1,empty_col, col2 = st.columns([1.5, 0.5, 3])

with col1:
    st.title("")
    st.image("portfolio/images/profile.jpg")

with col2:
    st.title("DHRUVA TEJA D R")
    container = st.container(border=True)
    container.write("Hello!, I am currently pursuing my Bachelor Degree in Dayananda Sagar College Of Engineering\
                , Bangalore.")
    container.write("<b>Languages</b>: Python", unsafe_allow_html=True)
    container.write("<b>Frameworks:</b> Flask | Django | Streamlit", unsafe_allow_html=True)
    container.write("<b>GUI Libraries</b>: PySimpleGUI | PyQt6", unsafe_allow_html=True) 
    container.write("<b>Developer tools:</b> VS Code | Notion AI | Github | Pycharm ", unsafe_allow_html=True)
    
    container.write("My Hobbies are Journaling, Listening to Music, Watching web series, eating, Somtimes reading some self-\
                motivation books or sometimes even novels. Am very much intrested in Automation and Machine Learning, yet to do my research.")
    

st.divider()
st.write("<h4>Below you can find some of the apps I have built using python. Feel free to contact me!<h4>", unsafe_allow_html=True)

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("portfolio/data.csv", sep=";")

with col3:
    for index, row in data[:7].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("portfolio/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[7:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("portfolio/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
