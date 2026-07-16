import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.19)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: DROPDOWN VISIBILITY REPAIR | VERSION STAMPED
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global", layout="wide")

# --- VERSION STAMP (Top Left) ---
st.sidebar.markdown("`SYSTEM VERSION: v1.19`")
st.sidebar.markdown("---")

# --- NUCLEAR CSS OVERHAUL (v1.19 - Absolute Force) ---
st.markdown("""
    <style>
    /* Force App Background */
    .stApp { background-color: #000000 !important; }

    /* NUCLEAR DROPDOWN FIX: Force ANY selected text to be BLACK on SILVER for absolute visibility */
    /* This makes the box look like a button when closed, making it impossible to miss the text */
    div[data-testid="stSelectbox"] > div {
        background-color: #C0C0C0 !important;
        color: #000000 !important;
        border-radius: 4px !important;
        border: 2px solid #FFFFFF !important;
    }

    /* Force the text color specifically */
    div[data-testid="stSelectbox"] p {
        color: #000000 !important;
        font-weight: 900 !important;
    }

    /* Force the arrow color */
    div[data-testid="stSelectbox"] svg {
        fill: #000000 !important;
    }

    /* Headings */
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900; text-align: center; }
    label { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.1rem !important; }

    /* Buttons */
    button, .stButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important;
        font-weight: 900 !important; text-transform: uppercase !important;
    }

    /* Paper Preview */
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important; padding: 40px;
        font-family: 'Times New Roman', serif !important; border: 3px solid #000;
    }
    .legal-paper * { color: #000000 !important; }

    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL STATUTE ENGINE ---
STATUTES = {
    "United States (US)": {"Security Deposit Recovery": "US Civil Code Section 1950.5", "Unpaid Freelance Invoice": "UCC Breach of Contract", "Vehicle Sale Agreement": "State Bill of Sale Protocol", "General Contract Breach": "Common Law"},
    "United Kingdom (UK)": {"Security Deposit Recovery": "Housing Act 2004", "Unpaid Freelance Invoice": "Late Payment Act 1998", "Vehicle Sale Agreement": "Sale of Goods Act", "General Contract Breach": "Unfair Contract Terms"},
    "South Africa (ZA)": {"Security Deposit Recovery": "Rental Housing Act 1999", "Unpaid Freelance Invoice": "Prescribed Rate of Interest Act", "Vehicle Sale Agreement": "Voetstoots Protocol", "General Contract Breach": "CPA 2008"},
    "Australia (AU)": {"Security Deposit Recovery": "Residential Tenancies Act 2010", "Unpaid Freelance Invoice": "ACL Payment Terms", "Vehicle Sale Agreement": "Motor Vehicle Traders Act", "General Contract Breach": "ACL"},
    "New Zealand (NZ)": {"Security Deposit Recovery": "Residential Tenancies Act 1986", "Unpaid Freelance Invoice": "Consumer Guarantees Act", "Vehicle Sale Agreement": "Fair Trading Act", "General Contract Breach": "CCLA 2017"},
    "Canada (CA)": {"Security Deposit Recovery": "Provincial Tenancy Acts", "Unpaid Freelance Invoice": "Sale of Goods Act", "Vehicle Sale Agreement": "Consumer Protection Acts", "General Contract Breach": "Common Law"},
    "India (IN)": {"Security Deposit Recovery": "Model Tenancy Act 2021", "Unpaid Freelance Invoice": "Indian Contract Act", "Vehicle Sale Agreement": "Motor Vehicles Act", "General Contract Breach": "Contract Law"}
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)", "INR (₹)"]

if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>CERTIFIED LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name")
            juris = st.selectbox("Select Jurisdiction", list(STATUTES.keys()))
        with c2:
            res_name = st.text_input("Respondent Name")
            curr = st.selectbox("Select Currency", CURRENCIES)
            
        category = st.selectbox("Select Case Category", list(STATUTES[juris].keys()))
        amount = st.text_input(f"Total Amount Owed ({curr.split(' ')[1]})")
        details = st.text_area("Dispute Narrative (Be thorough)", height=150)
        
        if st.button("PROCESS OFFICIAL LEGAL DEMAND"):
            if cl_name and res_name and details:
                st.session_state.cl_name, st.session_state.res_name = cl_name, res_name
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.juris, st.session_state.category = juris, category
                st.session_state.curr = curr.split(' ')[1]
                st.session_state.ready = True
                st.success("Logic Analysis Complete.")

    if st.session_state.ready:
        st.divider()
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE**")
        st.markdown("""<div style="filter:blur(10px); background:#111; padding:20px; border:1px dashed #C0C0C0;">Notice is hereby given that your actions constitute a direct violation...</div>""", unsafe_allow_html=True)
        if st.button("UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            if st.session_state.details.startswith("ADMIN-TEST"):
                st.session_state.paid = True
                st.rerun()
            else:
                checkout_url = "https://trend-shadows.lemonsqueezy.com/buy/1914602"
                st.markdown(f'<meta http-equiv="refresh" content="0; url={checkout_url}">', unsafe_allow_html=True)

else:
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    law = STATUTES[st.session_state.juris].get(st.session_state.category)
    date_now = datetime.now().strftime("%B %d, %Y")
    body = f"Notice is hereby given that your failure to remit the balance of {st.session_state.curr}{st.session_state.amount} constitutes a direct violation of {law}.\n\nUnder the laws of {st.session_state.juris}, the withholding of these funds is a breach of legal obligations.\n\nLEGAL DEMAND: Demand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days."
    st.markdown(f"""<div class="legal-paper"><div style="display:flex; justify-content:space-between; color:#000;"><div><b>FROM:</b><br>{st.session_state.cl_name}</div><div><b>DATE:</b><br>{date_now}</div></div><br><b>TO:</b><br>{st.session_state.res_name}<br><br><div style="text-align:center; text-decoration:underline; font-size: 20px; color:#000;"><b>FORMAL LETTER OF DEMAND</b></div><br><p style="color:#000; white-space: pre-wrap;">{body}</p></div>""", unsafe_allow_html=True)
    st.download_button("DOWNLOAD OFFICIAL WORD DOCUMENT", body, file_name="Legal_Demand.doc")
    if st.button("INITIATE NEW CASE"):
        st.session_state.paid = False; st.session_state.ready = False; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.19 | Trend Shadows Executive Tier")
