=import streamlit as st
import streamlit.components.v1 as components

def add_sidebar_ad():
    # Replace this with your actual Google AdSense code
    adsense_code = """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
     crossorigin="anonymous"></script>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
         data-ad-slot="XXXXXXXXXX"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    """
    
    # Use components.html to render the ad
    with st.sidebar:
        st.markdown("---") # Visual separator
        components.html(adsense_code, height=600)

# Call the function in your app
add_sidebar_ad()
