import streamlit as st
import pymongo
from pymongo import MongoClient

cluster = pymongo.MongoClient(
    "mongodb+srv://gurleen2113:parika13@cluster0.70n9crp.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Server"]
user = db["Users"]

# def switch_page(page_name: str):
#     from streamlit import _RerunData, _RerunException
#     from streamlit.source_util import get_pages

#     def standardize_name(name: str) -> str:
#         return name.lower().replace("_", " ")
    
#     page_name = standardize_name(page_name)

#     pages = get_pages("main.py")  # OR whatever your main page is called

#     for page_hash, config in pages.items():
#         if standardize_name(config["page_name"]) == page_name:
#             raise _RerunException(
#                 _RerunData(
#                     page_script_hash=page_hash,
#                     page_name=page_name,
#                 )
#             )

#     page_names = [standardize_name(config["page_name"]) for config in pages.values()]

#     raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

# from streamlit_extras.switch_page_button import switch_page
# from st_pages import Page, show_pages, hide_pages

# show_pages([
#     Page("main.py","Login"),
#     #Page("trial.py","Trial")
# ])

# hide_pages(['Dashboard','User','Admin'])

# if st.button('Trial'):
#     switch_page('Trial')

# def open_new_tab():
#     new_page = """
#     <html>
#         <body>
#             <script type="text/javascript">
#                 window.open('https://www.example.com', '_blank');
#                 window.close();
#             </script>
#         </body>
#     </html>
#     """
#     st.write(new_page, unsafe_allow_html=True)

def login():
    st.title("Login")
    username = st.text_input("Username", key="name")
    password = st.text_input("Password", key= "password",type="password")
    login_button = st.button("Login")
    # flag = 1

    if login_button:

        # Add your login logic here
        results = user.find()
        for result in results:
            print(result['Username'])
            if username == result['Username'] and password == result['Password']:
                st.success("Logged in successfully!")
                # flag = 0
                is_logged_in = True
                #switch_page('Dashboard')
                # pagecheck()
                break

        if(is_logged_in == False):
            st.error("Invalid Login")
        # else:
        #     hide_pages(['Login'])
        #     show_pages([
        #             Page("admin.py","Admin"),
        #             Page("dashboard.py","Dashboard"),
        #             Page("user.py","User")])
            #is_logged_in = False


# def secondpage():
#     st.sidebar.title("Dashboard")
#     page = st.sidebar.selectbox("Select Page", ["Dashboard", "Manage Users", "Manage Admins"])

#     if page == "Dashboard":
#         dashboard()
#     elif page == "Manage Users":
#         users()
#     elif page == "Manage Admin":
#         admin()
    


# def pagecheck():
#     # Check if user is logged in
#     is_logged_in = st.session_state.get('is_logged_in', False)

#     # Render login page if user is not logged in
#     if (is_logged_in == True):
#         login()
#     else:
#         # Render the second page if user is logged in
#         secondpage()

# def signup():
#     st.title("Signup")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
#     signup_button = st.button("Signup")

#     if signup_button:
#         # Add your signup logic here
#         if password == confirm_password:
#             post = {"Username": username, "Password": password}
#             user.insert_one(post)
#             st.success("Signup successful!")
#         else:
#             st.error("Passwords do not match")


# def main():
#     # st.sidebar.title("My App")
#     # page = st.sidebar.selectbox("Select Page", ["Login", "Signup"])

#     if page == "Login":
#         login()
#     elif page == "Signup":
#         signup()

def main():
    is_logged_in = st.session_state.get('is_logged_in', False)
    login()

if __name__ == "__main__":
    main()
