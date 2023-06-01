import streamlit as st
import pymongo

cluster = pymongo.MongoClient(
    "mongodb+srv://gurleen2113:parika13@cluster0.70n9crp.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Server"]
user = db["Users"]

def login():
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
                break

        if(is_logged_in == False):
            st.error("Invalid Login")


def main():
    is_logged_in = st.session_state.get('is_logged_in', False)
    login()

if __name__ == "__main__":
    main()
