import streamlit as st


def header_home():

    logo_url = "https://i.postimg.cc/cCMBzhpP/Chat-GPT-Image-May-16-2026-08-31-19-PM-removebg-preview.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:150px;' />
            <h1 style='text-align:center; color:#E0E3FF'>Marked</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.postimg.cc/Cxjwm7Yt/Chat-GPT-Image-May-20-2026-10-37-59-PM-removebg-preview.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:100px;' />
            <h2 style='text-align:left; color:#149AF3'>Marked</h2>

        </div>   
                
                """, unsafe_allow_html=True)