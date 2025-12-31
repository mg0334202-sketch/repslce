import streamlit as st
import extra_streamlit_components as stx # Required for Browser Cookies
import sqlite3
import hashlib
from datetime import datetime, timedelta

# --- 1. COOKIE SETUP ---
@st.cache_resource
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()

# --- 2. GOOGLE VERIFICATION ---
adsense_id = "ca-pub-5090333021864978"
st.markdown(f'<meta name="google-adsense-account" content="{adsense_id}">', unsafe_allow_html=True)

# --- 3. DATABASE ---
conn = sqlite3.connect('userdata.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS userstable(email TEXT UNIQUE, password TEXT)')
conn.commit()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# --- 4. LOGIN LOGIC WITH COOKIES ---
# This checks if the browser already has a "user_email" saved
saved_user = cookie_manager.get(cookie="user_email")

if 'logged_in' not in st.session_state:
    if saved_user:
        st.session_state.logged_in = True
        st.session_state.user_email = saved_user
    else:
        st.session_state.logged_in = False

# --- 5. APP UI ---
if not st.session_state.logged_in:
    st.title("💰 Expense Hero")
    st.write("Please login to save your expenses permanently.")
    
    with st.sidebar:
        st.header("Login")
        email = st.text_input("Email")
        pw = st.text_input("Password", type="password")
        
        if st.button("Log In"):
            # Check database (simplified for example)
            # If successful, save the cookie for 30 days:
            cookie_manager.set("user_email", email, expires_at=datetime.now() + timedelta(days=30))
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.rerun()
else:
    st.title(f"Welcome back, {st.session_state.user_email}")
    
    # LOGOUT LOGIC
    if st.sidebar.button("Logout"):
        # Delete the cookie from the browser
        cookie_manager.delete("user_email")
        st.session_state.logged_in = False
        st.rerun()

    # (Your Expense Tracking Code Goes Here)
    st.success("You are now permanently logged in on this browser!")

# --- FOOTER ---
st.divider()
st.caption(f"Authorized Seller: google.com, {adsense_id}, DIRECT, f08c47fec0942fa0")
