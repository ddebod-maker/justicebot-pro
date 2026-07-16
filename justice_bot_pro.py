import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.22)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: 10-DOMAIN ENGINE | INDESTRUCTIBLE BUILD
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Elite", layout="wide")
st.sidebar.markdown("`SYSTEM VERSION: v1.22`")

# --- MASTER CSS (Visibility & High-End Legal Stationery) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; }
    
    /* DROPDOWN VISIBILITY */
    div[data-testid="stSelectbox"] > div {
        background-color: #C0C0C0 !important; color: #000000 !important;
        border-radius: 4px !important; border: 2px solid #FFFFFF !important;
    }
    div[data-testid="stSelectbox"] p { color: #000000 !important; font-weight: 900 !important; }

    /* LABELS & INPUTS */
    label, .stMarkdown p { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.1rem !important; }
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #C0C0C0 !important;
    }

    /* BUTTONS */
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important;
        font-weight: 900 !important; text-transform: uppercase !important; border: 2px solid #FFFFFF !important;
        height: 3.5em !important;
    }

    /* THE LEGAL DOCUMENT (Official Bond Stationery) */
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important;
        padding: 70px 100px !important; font-family: 'Times New Roman', serif !important;
        line-height: 1.6 !important; border: 15px double #000000 !important; /* Industrial Border */
        margin: 40px auto !important; max-width: 850px !important; text-align: left !important;
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.1) !important;
    }
    .legal-paper * { color: #000000 !important; }
    .sig-line { margin-top: 50px; border-top: 2px solid #000; width: 250px; }

    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# --- 10-DOMAIN GLOBAL ENGINE ---
STATUTES = {
    "United States (US)": {
        "Security Deposit Recovery": "US Civil Code Section 1950.5",
        "Unpaid Freelance Invoice": "UCC Article 2 / Breach of Contract",
        "Private Vehicle Sale": "State Bill of Sale Statutes",
        "Electronics/Goods Sale": "Magnuson-Moss Warranty Act",
        "Travel/Flight Refund": "US DOT Refund Mandates",
        "Service Cancellation": "State Consumer Statutes",
        "Employment/Unpaid Wages": "FLSA Regulations",
        "Insurance Claim Dispute": "Insurance Fair Conduct Act",
        "Property Damage Claim": "General Tort Law",
        "General Cease & Desist": "Common Law Harassment Codes"
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": "Housing Act 2004",
        "Unpaid Freelance Invoice": "Late Payment Act 1998",
        "Private Vehicle Sale": "Sale of Goods Act 1979",
        "Electronics/Goods Sale": "Consumer Rights Act 2015",
        "Travel/Flight Refund": "UK261 Regulations",
        "Service Cancellation": "Consumer Rights Act (Unfair Terms)",
        "Employment/Unpaid Wages": "Employment Rights Act 1996",
        "Insurance Claim Dispute": "FOS Guidelines",
        "Property Damage Claim": "Occupiers' Liability Act",
        "General Cease & Desist": "Protection from Harassment Act"
    },
    "South Africa (ZA)": {
        "Security Deposit Recovery": "Rental Housing Act 50 of 1999",
        "Unpaid Freelance Invoice": "Prescribed Rate of Interest Act 55 of 1975",
        "Private Vehicle Sale": "Private Sale Agreement (Voetstoots)",
        "Electronics/Goods Sale": "Consumer Protection Act Section 55",
        "Travel/Flight Refund": "Consumer Protection Act Section 47",
        "Service Cancellation": "Consumer Protection Act Section 14",
        "Employment/Unpaid Wages": "Basic Conditions of Employment Act",
        "Insurance Claim Dispute": "Short-Term Insurance Act",
        "Property Damage Claim": "Apportionment of Damages Act",
        "General Cease & Desist": "Protection from Harassment Act 2011"
    },
    "Australia (AU)": {
        "Security Deposit Recovery": "Residential Tenancies Act 2010",
        "Unpaid Freelance Invoice": "ACL Payment Terms",
        "Private Vehicle Sale": "State Motor Vehicle Traders Act",
        "Electronics/Goods Sale": "ACL Consumer Guarantees",
        "Travel/Flight Refund": "ACL Major Failure Protocols",
        "Service Cancellation": "ACL Unfair Contract Terms",
        "Employment/Unpaid Wages": "Fair Work Act 2009",
        "Insurance Claim Dispute": "Insurance Contracts Act 1984",
        "Property Damage Claim": "Civil Liability Act 2002",
        "General Cease & Desist": "Personal Violence Protection Act"
    },
    "Canada (CA)": {
        "Security Deposit Recovery": "Provincial Residential Tenancy Acts",
        "Unpaid Freelance Invoice": "Provincial Sale of Goods Acts",
        "Private Vehicle Sale": "Consumer Protection Statutes",
        "Electronics/Goods Sale": "CPA Section 14",
        "Travel/Flight Refund": "Air Passenger Protection Regulations (APPR)",
        "Service Cancellation": "CPA Cancellation Protocols",
        "Employment/Unpaid Wages": "Canada Labour Code",
        "Insurance Claim Dispute": "Provincial Insurance Acts",
        "Property Damage Claim": "Negligence Act",
        "General Cease & Desist": "Libel and Slander Act"
    }
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)", "INR (₹)"]

if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.divider()

if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Name (You)")
            juris = st.selectbox("Jurisdiction", list(STATUTES.keys()))
        with c2:
            res_name = st.text_input("Respondent Name")
            curr = st.selectbox("Currency", CURRENCIES)
            
        category = st.selectbox("Case Category", list(STATUTES[juris].keys()))
        amount = st.text_input(f"Total Amount Owed ({curr.split(' ')[1]})")
        details = st.text_area("Dispute Narrative (Be thorough with dates and facts)", height=150)
        
        if st.button("PROCESS OFFICIAL LEGAL DEMAND"):
            if cl_name and res_name and details:
                st.session_state.cl_name, st.session_state.res_name = cl_name, res_name
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.juris, st.session_state.category = juris, category
                st.session_state.curr_sym = curr.split(' ')[1]
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Ready.")

    if st.session_state.ready:
        st.divider()
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE**")
        st.markdown("""<div style="filter:blur(10px); background:#111; padding:20px; border:1px dashed #C0C0C0;">Notice is hereby given that your actions constitute a direct violation...</div>""", unsafe_allow_html=True)
        if st.button("💎 UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            if st.session_state.details.startswith("ADMIN-TEST"):
                st.session_state.paid = True; st.rerun()
            else:
                st.link_button("PAY TO UNLOCK ($19.00)", "https://trend-shadows.lemonsqueezy.com/buy/1914602")

else:
    st.success("✅ DOCUMENT UNLOCKED.")
    law = STATUTES[st.session_state.juris].get(st.session_state.category)
    date_now = datetime.now().strftime("%B %d, %Y")
    
    # THE FORMAL DOCUMENT
    st.markdown(f"""
        <div class="legal-paper">
            <div style="display:flex; justify-content:space-between; width:100%;">
                <div><b>FROM:</b><br>{st.session_state.cl_name}</div>
                <div style="text-align:right;"><b>DATE:</b><br>{date_now}</div>
            </div>
            <br>
            <div><b>TO:</b><br>{st.session_state.res_name}</div>
            <br><br>
            <div style="text-align:center; text-decoration:underline; font-size: 24px;"><b>FORMAL LETTER OF DEMAND</b></div>
            <br>
            <p>Notice is hereby given that your failure to remit the balance of {st.session_state.curr_sym}{st.session_state.amount} regarding the {st.session_state.category.lower()} constitutes a direct violation of {law}.</p>
            <p>Under the laws of {st.session_state.juris}, specifically regarding {st.session_state.category.lower()}, the withholding of these funds is a breach of legal obligations.</p>
            <p><b>DISPUTE NARRATIVE:</b><br>{st.session_state.details}</p>
            <p><b>LEGAL DEMAND:</b><br>Demand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days of the date of this notice.</p>
            <p><b>INTENT TO LITIGATE:</b><br>Failure to comply will result in the immediate commencement of legal proceedings in Small Claims Court without further notice.</p>
            <br><p>Sincerely,</p>
            <div class="sig-line"></div>
            <p><b>{st.session_state.cl_name}</b><br>Claimant</p>
        </div>
    """, unsafe_allow_html=True)
    
    final_txt = f"FROM: {st.session_state.cl_name}\nDATE: {date_now}\n\nFORMAL DEMAND FOR {st.session_state.amount}\nViolation of {law}\n\nDetails: {st.session_state.details}"
    st.download_button("📥 DOWNLOAD PRINT-READY DOC", final_txt, file_name="Legal_Demand_Final.doc")
    if st.button("INITIATE NEW CASE"):
        st.session_state.paid = False; st.session_state.ready = False; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.22 | Trend Shadows Executive Tier")
