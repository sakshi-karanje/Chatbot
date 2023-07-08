import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json

# This project is developed by Sakshi Karanje
# This project uses Bard API to demonstrate chatbot functionality
with open('credentials.json', 'r') as f:
    file = json.load(f)
    token = file['token']

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Mobile phone")
# )

# Function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

# Function to recieve user querries
def get_text():
    input_text = st.text_input("My Bot:", key = 'input')
    return input_text

# Title of the streamlit app
st.title("🤖 Personal Tutoring Bot")

# url = 'https://images.pexels.com/photos/2085998/pexels-photo-2085998.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
# data-testid="stAppViewContainer"

changes = '''
<style>
[data-testid="stAppViewContainer"]
    {
    background-image:url('https://images.pexels.com/photos/2085998/pexels-photo-2085998.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
    background-color: #cccccc; /* Used if the image is unavailable */
    height: 750px; /* You must set a specified height */
    width: 1550px;
    background-position: center; /* Center the image */
    background-repeat: no-repeat; /* Do not repeat the image */
    background-size: cover; /* Resize the background image to cover the entire container */
    }
    html{
    background="transparent"
    }
    div.esravye2 > iframe
    {
    background-colour:transparent
    }
    </style>
'''
st.markdown(changes, unsafe_allow_html=True)

hide_st_style = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)

footer = '''
    <style>
    .footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: white;
    text-align: center;
    }
    </style>
    <div class="footer">
    <p>Developed with ❤ by Sakshi Karanje</p>
    </div>
'''
st.markdown(footer,unsafe_allow_html=True)

print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated']=[]

    if 'past' not in st.session_state:
        st.session_state['past'] = []

# Accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key = str(i))
        message(st.session_state['past'][i], key = "user_"+str(i), is_user=True)