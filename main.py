import streamlit as st
import pymongo
from datetime import datetime
import webbrowser

global cluster
global db
global user
# cluster = pymongo.MongoClient(
#     "mongodb+srv://gurleen2113:parika13@cluster0.70n9crp.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS=60000)
# db = cluster["Server"]
# user = db["Users"]
#serverSelectionTimeoutMS=60000
def connection():
    global user
    cluster = pymongo.MongoClient(
    "mongodb+srv://gurleen2113:parika13@cluster0.70n9crp.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["Server"]
    user = db["Users"]
    return user
# def open_new_page():
#     url='https://gurleen21-capstoneserverdashboard-app-o649ro.streamlit.app/'
#     webbrowser.open_new_tab(url)

def login(user):
    st.title("Login")
    username = st.text_input("Username", key="name")
    password = st.text_input("Password", key= "password",type="password")
    login_button = st.button("Login")


    if login_button:
        # Add your login logic here
        results = user.find()
        for result in results:
            print(result['Username'])
            if username == result['Username'] and password == result['Password']:
                st.success("Logged in successfully!")
                is_logged_in = True
                # open_new_page()
                # new_app_url = "https://gurleen21-capstoneserverdashboard-app-o649ro.streamlit.app/"
                # js_code = f"window.open('{new_app_url}')"
                # st.write(f'<script>{js_code}</script>', unsafe_allow_html=True)
                #st.markdown('<a href="C:/Users/HP/Desktop/Main/Thapar/Capstone Project/Drone Based Surveillance System/App/ServerApp/Pages/Dashboard/app.py" target="_self">Dashboarde</a>', unsafe_allow_html=True)
                st.markdown('<a href="https://gurleen21-capstoneserverdashboard-app-o649ro.streamlit.app/" target="_self">Go to Dashboard</a>', unsafe_allow_html=True)
                break

        if(is_logged_in == False):
            st.error("Invalid Login")

# def open_new_page():
#     new_page_url = "https://www.google.com/"  # Replace with the desired URL
#     new_page_script = f"""
#     <script type="text/javascript">
#         window.location.href = "{new_page_url}";
#     </script>
#     """
#     st.write(new_page_script, unsafe_allow_html=True)
def main(user):
    now = datetime.now()
    now = now.strftime("%S")
    now=str(now)
    if(now==0 or now==00 or now==30):
        user = connection()
    is_logged_in = st.session_state.get('is_logged_in', False)
    login(user)

if __name__ == "__main__":
    user = connection()
    main(user)
