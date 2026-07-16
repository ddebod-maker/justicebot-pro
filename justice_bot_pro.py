import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.23)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: 7 JURISDICTIONS | 10 DOMAINS | VOUCHER SYSTEM ACTIVE
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Elite", layout="wide")

# --- SYSTEM VERSION & VOUCHER (Sidebar) ---
st.sidebar.markdown("`SYSTEM VERSION: v1.23`")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔑 Access Control")
voucher_input = st.sidebar.text_input("Enter Voucher / Admin Code", type="password", help="Enter a promotional code to unlock full document access.")

# --- MASTER CSS (Visibility, Industrial Silver, and High-Court Stationery) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; }
    
    /* 1. SELECTION BOX VISIBILITY FIX */
    div[data-testid="stSelectbox"] > div {
        background-color: #C0C0C0 !important; color: #000000 !important;
        border-radius: 4px !important; border: 2px solid #FFFFFF !important;
    }
    div[data-testid="stSelectbox"] p { color: #000000 !important; font-weight: 900 !important; }
    div[data-testid="stSelectbox"] svg { fill: #000000 !important; }

    /* 2. LABELS & INPUTS */
    label, .stMarkdown p { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.1rem !important; }
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #C0C0C0 !important;
    }

    /* 3. BUTTONS: Solid Industrial Silver */
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important;
        font-weight: 900 !important; text-transform: uppercase !important; border: 2px solid #FFFFFF !important;
        height: 3.5em !important; width: 100% !important;
    }

    /* 4. THE PRO LEGAL DOCUMENT (Premium Bond Stationery) */
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important;
        padding: 80px 100px !important; font-family: 'Times New Roman', serif !important;
        line-height: 1.6 !important; border: 12px double #000000 !important;
        margin: 50px auto !important; max-width: 900px !important; text-align: left !important;
        box-shadow: 0 0 60px rgba(255, 255, 255, 0.1) !important;
    }
    .legal-paper * { color: #000000 !important; }
    .sig-block { margin-top: 60px; border-top: 2px solid #000; width: 300px; padding-top: 10px; }

    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- THE 10-DOMAIN GLOBAL ENGINE (7 COUNTRIES INCLUDING INDIA) ---
STATUTES = {
    "United States (US)": {
        "Security Deposit Recovery": "US Civil Code Section 1950.5",
        "Unpaid Freelance Invoice": "UCC Article 2 / Breach of Contract",
        "Private Vehicle Sale": "State Bill of Sale & Lemon Laws",
        "Electronics/Goods Sale": "Magnuson-Moss Warranty Act",
        "Travel/Flight Refund": "US DOT Refund Mandates",
        "Service Cancellation": "State Consumer Statutes",
        "Employment/Unpaid Wages": "Fair Labor Standards Act (FLSA)",
        "Insurance Claim Dispute": "Insurance Fair Conduct Act",
        "Property Damage Claim": "General Tort Law",
        "General Cease & Desist": "Common Law Defamation/Harassment"
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": "Housing Act 2004",
        "Unpaid Freelance Invoice": "Late Payment of Commercial Debts Act 1998",
        "Private Vehicle Sale": "Sale of Goods Act 1979",
        "Electronics/Goods Sale": "Consumer Rights Act 2015",
        "Travel/Flight Refund": "UK261 Regulations",
        "Service Cancellation": "Consumer Rights Act (Unfair Terms)",
        "Employment/Unpaid Wages": "Employment Rights Act 1996",
        "Insurance Claim Dispute": "FOS Guidelines",
        "Property Damage Claim": "Occupiers' Liability Act",
        "General Cease & Desist": "Protection from Harassment Act 1997"
    },
    "South Africa (ZA)": {
        "Security Deposit Recovery": "Rental Housing Act 50 of 1999",
        "Unpaid Freelance Invoice": "Prescribed Rate of Interest Act 55 of 1975",
        "Private Vehicle Sale": "Private Sale Agreement (Voetstoots Protocol)",
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
        "Unpaid Freelance Invoice": "Australian Consumer Law (ACL)",
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
    },
    "New Zealand (NZ)": {
        "Security Deposit Recovery": "Residential Tenancies Act 1986",
        "Unpaid Freelance Invoice": "Consumer Guarantees Act 1993",
        "Private Vehicle Sale": "Fair Trading Act 1986",
        "Electronics/Goods Sale": "CGA Section 6",
        "Travel/Flight Refund": "Contract and Commercial Law Act 2017",
        "Service Cancellation": "CGA Reasonable Care",
        "Employment/Unpaid Wages": "Employment Relations Act 2000",
        "Insurance Claim Dispute": "Insurance Law Reform Act",
        "Property Damage Claim": "Limitation Act 2010",
        "General Cease & Desist": "Harassment Act 1997"
    },
    "India (IN)": {
        "Security Deposit Recovery": "Model Tenancy Act 2021",
        "Unpaid Freelance Invoice": "Indian Contract Act 1872",
        "Private Vehicle Sale": "Motor Vehicles Act 1988",
        "Electronics/Goods Sale": "Consumer Protection Act 2019",
        "Travel/Flight Refund": "DGCA Passenger Charter",
        "Service Cancellation": "CPA Unfair Contracts",
        "Employment/Unpaid Wages": "Payment of Wages Act 1936",
        "Insurance Claim Dispute": "IRDAI Guidelines",
        "Property Damage Claim": "Tort of Negligence",
        "General Cease & Desist": "Defamation Laws & IT Act 2000"
    }
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)", "INR (₹)"]

if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

# --- BRANDING ---
st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>ELITE LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

# --- VOUCHER CHECK ---
ADMIN_CODE = "TS-GIFT-2026"
is_admin = (voucher_input == ADMIN_CODE)

if not st.session_state.paid and not is_admin:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name (You)")
            juris = st.selectbox("Select Jurisdiction", list(STATUTES.keys()))
        with c2:
            res_name = st.text_input("Respondent Name (Company or Person)")
            curr = st.selectbox("Select Currency", CURRENCIES)
            
        category = st.selectbox("Select Case Category", list(STATUTES[juris].keys()))
        amount = st.text_input(f"Total Amount Owed ({curr.split(' ')[1]})")
        details = st.text_area("Dispute Narrative (Be thorough with dates and facts)", height=150)
        
        if st.button("PROCESS OFFICIAL LEGAL DEMAND"):
            if cl_name and res_name and details:
                st.session_state.cl_name, st.session_state.res_name = cl_name, res_name
                st.session_state.cl_addr = "REDACTED UNTIL UNLOCK"
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.juris, st.session_state.category = juris, category
                st.session_state.curr_sym = curr.split(' ')[1]
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Ready.")

    if st.session_state.ready:
        st.divider()
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.category.upper()}**")
        st.markdown("""<div style="filter:blur(10px); background:#111; padding:30px; border:1px dashed #C0C0C0;">Notice is hereby given that your actions constitute a direct violation...</div>""", unsafe_allow_html=True)
        st.info("💡 **Admin Tip:** Use the sidebar code to unlock for free, or click below for commercial payment.")
        st.link_button("💎 UNLOCK VIA SECURE CHECKOUT ($19.00)", "https://trend-shadows.lemonsqueezy.com/buy/1914602")

else:
    # --- FINAL PRODUCTION OUTPUT ---
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    law = STATUTES[st.session_state.juris].get(st.session_state.category)
    date_now = datetime.now().strftime("%B %d, %Y")
    
    # Paper Content
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
            <p><b>INTENT TO LITIGATE:</b><br>Failure to comply will result in the immediate commencement of legal proceedings in Small Claims Court without further notice. We will pursue the recovery of the full amount, interest, and costs.</p>
            <br><p>Sincerely,</p>
            <div class="sig-block"></div>
            <p><b>{st.session_state.cl_name}</b><br>Claimant</p>
        </div>
    """, unsafe_allow_html=True)
    
    final_text = f"FROM: {st.session_state.cl_name}\nDATE: {date_now}\n\nFORMAL DEMAND: {st.session_state.amount}\nViolation of: {law}\n\nDetails: {st.session_state.details}"
    st.download_button("📥 DOWNLOAD PRINT-READY DOC", final_text, file_name="JusticeBot_Final_Demand.doc")
    if st.button("INITIATE NEW CASE"):
        st.session_state.paid = False; st.session_state.ready = False; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.23 | Trend Shadows Digital Agency")
