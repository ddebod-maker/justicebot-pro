import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.13)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: MULTI-JURISDICTIONAL / COMMERCIAL
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Trend Shadows Global", layout="wide")

# --- MASTER CSS OVERHAUL (v1.13 - Global Industrial Silver) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important; border: 2px solid #FFFFFF !important;
        font-weight: 900 !important; font-family: 'Inter', sans-serif !important;
        text-transform: uppercase !important; letter-spacing: 2px !important;
        height: 3.5em !important; width: 100% !important;
    }
    button:hover { background-color: #FFFFFF !important; box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) !important; }
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #C0C0C0 !important;
    }
    label, .stMarkdown p, .stSelectbox label { color: #FFFFFF !important; font-weight: 700 !important; }
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important; padding: 50px 70px !important;
        font-family: 'Times New Roman', serif !important; line-height: 1.6 !important;
        border: 3px solid #000000 !important; margin: 20px auto !important; max-width: 850px !important;
    }
    .blur-zone { filter: blur(12px); background: rgba(20, 20, 20, 0.9); padding: 30px; border: 1px dashed #C0C0C0; color: #FFFFFF !important; }
    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL STATUTE ENGINE ---
JURISDICTIONS = {
    "United States (US)": {
        "Deposit Recovery": "Civil Code Section 1950.5",
        "Unpaid Invoice": "UCC Breach of Contract",
        "Vehicle Sale Agreement": "Standard Bill of Sale & Lemon Law Protocol"
    },
    "United Kingdom (UK)": {
        "Deposit Recovery": "Housing Act 2004",
        "Unpaid Invoice": "Late Payment of Commercial Debts Act 1998",
        "Vehicle Sale Agreement": "Common Law Sale of Goods (Private)"
    },
    "South Africa (ZA)": {
        "Deposit Recovery": "Rental Housing Act 50 of 1999",
        "Unpaid Invoice": "Common Law Contract Breach",
        "Vehicle Sale Agreement": "Standard Private Sale Agreement (Voetstoots)"
    },
    "Australia (AU)": {
        "Deposit Recovery": "Residential Tenancies Act 2010",
        "Unpaid Invoice": "Australian Consumer Law (ACL)",
        "Vehicle Sale Agreement": "Private Vehicle Sale Deed"
    },
    "New Zealand (NZ)": {
        "Deposit Recovery": "Residential Tenancies Act 1986",
        "Unpaid Invoice": "Consumer Guarantees Act 1993",
        "Vehicle Sale Agreement": "Private Sale Receipt & Transfer Deed"
    }
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)"]

if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.markdown("<p style='letter-spacing:5px; color:#888; font-weight:400;'>INTERNATIONAL LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name")
            jurisdiction = st.selectbox("Jurisdiction", list(JURISDICTIONS.keys()))
        with c2:
            res_name = st.text_input("Respondent Name (Company or Person)")
            currency = st.selectbox("Preferred Currency", CURRENCIES)
            
        st.divider()
        category = st.selectbox("Case Category", list(JURISDICTIONS[jurisdiction].keys()))
        amount = st.text_input(f"Total Amount Owed ({currency.split(' ')[1]})")
        details = st.text_area("Dispute Narrative (Be thorough)", height=150)
        
        if st.button("ARCHITECT GLOBAL DEMAND"):
            if cl_name and res_name and details and amount:
                st.session_state.cl_name, st.session_state.res_name = cl_name, res_name
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.jurisdiction, st.session_state.category = jurisdiction, category
                st.session_state.currency = currency.split(' ')[1]
                st.session_state.ready = True
                st.success("Logic Analysis Complete.")
            else: st.error("Please fill all required fields.")

    if st.session_state.ready:
        st.divider()
        st.markdown("### 📄 Encrypted Draft Preview")
        st.info("PROTOCOL: Draft encrypted. Identification verified.")
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.category.upper()}**")
        st.markdown("""<div class="blur-zone">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes. Our AI has identified specific breaches of contract. Failure to remit funds will result in immediate filing... [LEGAL CITATIONS ENCRYPTED]</div>""", unsafe_allow_html=True)
        if st.button("UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            st.session_state.paid = True
            st.rerun()

else:
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    law = JURISDICTIONS[st.session_state.jurisdiction].get(st.session_state.category)
    date_now = datetime.now().strftime("%B %d, %Y")
    
    final_body = f"""Notice is hereby given that your failure to remit the balance of {st.session_state.currency}{st.session_state.amount} constitutes a direct violation of {law}.\n\nUnder the laws of {st.session_state.jurisdiction}, the withholding of these funds is a breach of legal obligations.\n\nLEGAL DEMAND: Demand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days."""

    st.markdown(f"""
        <div class="legal-paper">
            <div style="display:flex; justify-content:space-between; width:100%; color:#000;">
                <div style="text-align:left;"><b>FROM:</b><br>{st.session_state.cl_name}</div>
                <div style="text-align:right;"><b>DATE:</b><br>{date_now}</div>
            </div>
            <br>
            <div style="text-align:left; color:#000;"><b>TO:</b><br>{st.session_state.res_name}</div>
            <br><br>
            <div style="text-align:center; text-decoration:underline; font-size: 20px; color:#000;"><b>FORMAL LETTER OF DEMAND</b></div>
            <br>
            <p style="color:#000; white-space: pre-wrap;">{final_body}</p>
            <br>
            <p style="color:#000;">Sincerely,<br>___________________________<br><b>{st.session_state.cl_name}</b></p>
        </div>
    """, unsafe_allow_html=True)
    st.download_button("DOWNLOAD OFFICIAL WORD DOCUMENT", final_body, file_name="Legal_Demand.doc")
    if st.button("INITIATE NEW CASE"):
        st.session_state.paid = False; st.session_state.ready = False; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.13 | Trend Shadows Executive Tier")
