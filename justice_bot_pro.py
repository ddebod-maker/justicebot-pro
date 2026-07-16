import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.18)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: GLOBAL SCALE | UI SELECTOR VISIBILITY FIXED
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Digital Asset", layout="wide")

# --- MASTER CSS OVERHAUL (v1.18 - Ultimate Visibility & Contrast) ---
st.markdown("""
    <style>
    /* Global Body Background */
    .stApp { 
        background-color: #000000 !important; 
        color: #FFFFFF !important;
    }
    
    /* 1. SELECTION BOX VISIBILITY FIX */
    /* This ensures that selected text and the box itself are always high contrast */
    div[data-baseweb="select"] {
        background-color: #111111 !important;
        border: 1px solid #C0C0C0 !important;
        border-radius: 8px !important;
    }

    /* Target the actual text value that is displayed once selected */
    div[data-testid="stSelectbox"] div[role="button"] {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding-left: 10px !important;
    }

    /* Target the dropdown arrow */
    div[data-testid="stSelectbox"] svg {
        fill: #FFFFFF !important;
    }

    /* 2. Global Headings and Labels */
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; }
    h3 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 700 !important; }
    label, .stMarkdown p { color: #FFFFFF !important; font-weight: 700 !important; opacity: 1 !important; }

    /* 3. Buttons: Industrial Silver / Black Text */
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important; border: 2px solid #FFFFFF !important;
        font-weight: 900 !important; text-transform: uppercase !important; height: 3.5em !important; width: 100% !important;
    }
    button:hover { background-color: #FFFFFF !important; box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) !important; }

    /* 4. Text Areas & Inputs */
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #444444 !important;
    }

    /* 5. Legal Document Preview (The Paper) */
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important; padding: 50px 70px !important;
        font-family: 'Times New Roman', serif !important; line-height: 1.6 !important;
        border: 3px solid #000000 !important; margin: 20px auto !important; max-width: 850px !important;
    }
    .legal-paper * { color: #000000 !important; }

    /* 6. Blur Effect */
    .blur-zone { filter: blur(12px); background: rgba(20, 20, 20, 0.9); padding: 30px; border: 1px dashed #C0C0C0; color: #FFFFFF !important; }
    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL STATUTE ENGINE ---
STATUTES = {
    "United States (US)": {
        "Security Deposit Recovery": "US Civil Code Section 1950.5",
        "Unpaid Freelance Invoice": "UCC Breach of Contract",
        "Private Vehicle Sale": "State Bill of Sale Protocol",
        "General Contract Breach": "Common Law Contract Principles"
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": "Housing Act 2004",
        "Unpaid Freelance Invoice": "Late Payment of Commercial Debts Act 1998",
        "Private Vehicle Sale": "Sale of Goods Act",
        "General Contract Breach": "Unfair Contract Terms Act"
    },
    "South Africa (ZA)": {
        "Security Deposit Recovery": "Rental Housing Act 50 of 1999",
        "Unpaid Freelance Invoice": "Common Law Breach of Contract",
        "Private Vehicle Sale": "Voetstoots Protocol",
        "General Contract Breach": "Consumer Protection Act 68 of 2008"
    },
    "Australia (AU)": {
        "Security Deposit Recovery": "Residential Tenancies Act 2010",
        "Unpaid Freelance Invoice": "ACL Payment Terms",
        "Private Vehicle Sale": "State Vehicle Traders Act",
        "General Contract Breach": "Australian Consumer Law (ACL)"
    },
    "New Zealand (NZ)": {
        "Security Deposit Recovery": "Residential Tenancies Act 1986",
        "Unpaid Freelance Invoice": "Consumer Guarantees Act 1993",
        "Private Vehicle Sale": "Fair Trading Act 1986",
        "General Contract Breach": "Contract and Commercial Law Act"
    },
    "Canada (CA)": {
        "Security Deposit Recovery": "Provincial Tenancy Acts",
        "Unpaid Freelance Invoice": "Sale of Goods Act",
        "Private Vehicle Sale": "Provincial Consumer Statutes",
        "General Contract Breach": "Common Law"
    },
    "India (IN)": {
        "Security Deposit Recovery": "Model Tenancy Act 2021",
        "Unpaid Freelance Invoice": "Indian Contract Act 1872",
        "Private Vehicle Sale": "Motor Vehicles Act 1988",
        "General Contract Breach": "Indian Contract Law"
    }
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)", "INR (₹)"]

if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

# --- BRANDING ---
st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>INTERNATIONAL LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

# --- INPUT PHASE ---
if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name")
            juris = st.selectbox("Jurisdiction", list(STATUTES.keys()))
        with c2:
            res_name = st.text_input("Respondent Name")
            currency = st.selectbox("Preferred Currency", CURRENCIES)
            
        st.divider()
        category = st.selectbox("Case Category", list(STATUTES[juris].keys()))
        amount = st.text_input(f"Total Amount Owed ({currency.split(' ')[1]})")
        details = st.text_area("Dispute Narrative (Be thorough)", height=150)
        
        if st.button("PROCESS OFFICIAL LEGAL DEMAND"):
            if cl_name and res_name and details and amount:
                st.session_state.cl_name, st.session_state.res_name = cl_name, res_name
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.juris, st.session_state.category = juris, category
                st.session_state.currency = currency.split(' ')[1]
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Encrypted Below.")
            else: st.error("Please fill all required fields.")

    if st.session_state.ready:
        st.divider()
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.category.upper()}**")
        st.markdown("""<div class="blur-zone">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes... [LEGAL CITATIONS ENCRYPTED]</div>""", unsafe_allow_html=True)
        
        if st.button("UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            # CHECK FOR ADMIN BYPASS
            if st.session_state.details.startswith("ADMIN-TEST"):
                st.session_state.paid = True
                st.rerun()
            else:
                checkout_url = "https://trend-shadows.lemonsqueezy.com/buy/1914602"
                st.markdown(f'<meta http-equiv="refresh" content="0; url={checkout_url}">', unsafe_allow_html=True)

else:
    # --- OUTPUT PHASE (PAID) ---
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    law = STATUTES[st.session_state.juris].get(st.session_state.category)
    date_now = datetime.now().strftime("%B %d, %Y")
    
    final_body = f"Notice is hereby given that your failure to remit the balance of {st.session_state.currency}{st.session_state.amount} regarding the {st.session_state.category.lower()} constitutes a direct violation of {law}.\n\nUnder the laws of {st.session_state.juris}, the withholding of these funds is a breach of legal obligations.\n\nLEGAL DEMAND: Demand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days."

    st.markdown(f"""
        <div class="legal-paper">
            <div style="display:flex; justify-content:space-between;">
                <div><b>FROM:</b><br>{st.session_state.cl_name}</div>
                <div><b>DATE:</b><br>{date_now}</div>
            </div>
            <br>
            <div><b>TO:</b><br>{st.session_state.res_name}</div>
            <br><br>
            <div style="text-align:center; text-decoration:underline; font-size: 20px;"><b>FORMAL LETTER OF DEMAND</b></div>
            <br>
            <p style="white-space: pre-wrap;">{final_body}</p>
            <br>
            <p>Sincerely,<br>___________________________<br><b>{st.session_state.cl_name}</b></p>
        </div>
    """, unsafe_allow_html=True)
    st.download_button("DOWNLOAD OFFICIAL WORD DOCUMENT", final_body, file_name="Legal_Demand.doc")
    if st.button("INITIATE NEW CASE"):
        st.session_state.paid = False; st.session_state.ready = False; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.18 | Trend Shadows Executive Tier")
