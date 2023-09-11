import streamlit as st
#sets up website
st.set_page_config(page_title="Fynn's website", page_icon="🤥", layout="wide")
#contents
with st.container():
  st.subheader("Hi!, My name is Fynn! :wave:")
  st.title("I am a first year student majoring in electronics and computer systems.")
  st.write("I am passionate about the way electricity works and how the average person can use forms of eletrical and computer theory in the real world.")
  st.write("hopefully by the time I graduate Ive put enough energy into this project that i can show you other websites that I have made, Maybe ill even start up a blog?")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("More about me")
    st.write("##")
    st.write(
      """
      - Im currently 20 years old, 21 in december! Im studying semi-full time at victoria university of wellington
        and I have been living in wellington for the past 20 years.
        
      - I enjoy video games, programming and camping out on the tararua and rimutaka mountain ranges or exploring new tracks with my friends.
      
      - I spent a year at a polytechnic learning eletrical engineering up to level 3 and used my qualification to get out into the industry 
      where I found my allergys were far too overwhelming. After leaving the trades I took up driving and worked part time to deliver large amounts of catering food to clients,
      i worked there for about a year before I finally decided to dedcate myself to my education.

      """
            )
