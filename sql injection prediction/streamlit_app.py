import streamlit as st
from prediction_module import predict_class

st.set_page_config(page_title="SQLi Detection", page_icon="👾", layout="wide")  # Set the page title and icon


def home_page():
    st.title("Home Page")
    st.image("sql img.webp", width=700)
    st.write("Welcome to the SQL Injection Detection App!")
    st.write("Worried about SQL injection attacks on your SQL database?")
    st.write("We are here to help you by detecting whether the queries are vulnerable or not for SQL Injection attacks.")



if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


def prediction_page():
    st.title("SQLi Detection")
    st.text("""This page is used to detect SQLi attacks.
            Please enter the SQL query in the text box below to detect if this query is vulnerable or not.""")
    
    st.header("Enter SQL query")
    with st.form("SQLi Detection"):
        query = st.text_input("Enter SQL query here")
        if st.form_submit_button("Submit"):
            isSQLi = predict_class(query)
            st.write("Your query is:", query)
            if isSQLi:
                st.write("This query is Vulnarable to SQLi attack")
            else:
                st.write("This query is not Vulnarable to SQLi attack")

def about_page():
    st.title("About Page")
    
    # Introduction Section
    st.header("Introduction")
    st.write("Welcome to the SQL Injection Detection App!")
    
    # Purpose Section
    st.markdown("<h2 style='color:#ff5733'>Purpose</h2>", unsafe_allow_html=True)
    st.write("This app is designed to detect SQL injection attacks in input queries.")
    
    # Functionality Section
    st.markdown("<h2 style='color:#ff5733'>Functionality</h2>", unsafe_allow_html=True)
    st.write("The app utilizes a pre-trained Random Forest classifier to analyze input SQL queries.")
    st.write("It predicts whether a given query is likely to be a SQL injection attack or not.")
    
    # Features Section
    st.markdown("<h2 style='color:#ff5733'>Features</h2>", unsafe_allow_html=True)
    st.write("Users can input SQL queries in the provided text box.")
    st.write("The app then processes the query and displays whether it is identified as a SQL injection attack.")
    
    
    # Usage Section
    st.markdown("<h2 style='color:#ff5733'>Usage</h2>", unsafe_allow_html=True)
    st.write("This app can be used by developers, security professionals, and anyone interested in SQL injection prevention.")
    st.write("It aids in understanding the potential risks associated with SQL injection attacks and the importance of secure coding practices.")
    
    # Conclusion Section
    st.markdown("<h2 style='color:#ff5733'>Conclusion</h2>", unsafe_allow_html=True)
    st.write("By utilizing machine learning techniques, this app contributes to enhancing the security of web applications by detecting and preventing SQL injection vulnerabilities.")
    
    # Additional Information Section
    st.markdown("<h2 style='color:#ff5733'>Additional Information</h2>", unsafe_allow_html=True)
    st.markdown("**Disclaimer:**")
    st.write("The predictions made by this app are based on the provided input and the performance of the underlying machine learning model.")
    st.write("While efforts have been made to ensure accuracy, users should exercise caution and verify the results in real-world scenarios.")

    st.markdown(
        """
        <style>
        .css-145kmo2 a {
            color: #ff5733;
        }
        .css-2trqyj {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
def login():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        # Add authentication logic here
        if username == 'admin' and password == 'admin':
            st.session_state.logged_in = True
            st.session_state.selected_page = "Home"
            st.success(f'Logged in as {username}')
        else:
            st.error('Invalid username or password')


def logout():
    st.session_state.logged_in = False
    st.session_state.selected_page = 'Login'
    st.success('You have been logged out successfully.')
    login_url = f"{st.get_option('server.baseUrlPath')}?page=login"
    st.markdown(f"[Go to login page]({login_url})")


st.sidebar.title("SQL Injection Detection using machine learning")

# Sidebar buttons
if not st.session_state.logged_in:
    selected_page = st.sidebar.radio("Select Page", ['Login'])
else:
    selected_page = st.sidebar.radio("Select Page", ["Home", "Prediction", "About", "Logout"])

# Store the selected page in session state for automatic navigation
st.session_state.selected_page = selected_page

# Navigation based on the selected page and login status
if not st.session_state.logged_in:
    if st.session_state.selected_page == 'Login':
        login()
else:
    if st.session_state.selected_page == "Home":
        home_page()
    elif st.session_state.selected_page == "Prediction":
        prediction_page()
    elif st.session_state.selected_page == "About":
        about_page()
    elif st.session_state.selected_page == "Logout":
        logout()
