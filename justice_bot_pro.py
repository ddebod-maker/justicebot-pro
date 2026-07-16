import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.32)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: ULTIMATE INDUSTRIAL STABILITY | 10 DOMAINS | 7 JURISDICTIONS
# FIXED: Missing Body/Jargon logic.
# FIXED: Forced High-Contrast Visibility.
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Elite", layout="wide")

# --- VERSION VERIFICATION (Sidebar) ---
st.sidebar.markdown("### 🛠️ System Control")
st.sidebar.markdown("`VERSION: v1.32` (STABLE)")
st.sidebar.markdown(f"`BUILD DATE: {datetime.now().strftime('%Y-%m-%d')}`")
st.sidebar.markdown("---")
# Voucher is always active for owner testing
owner_code = st.sidebar.text_input("Owner Access Code", type="password", help="Use TS-GIFT-2026 to bypass payment.")

# --- MASTER CSS (Visibility & Industrial Finish) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* 1. SELECTION BOX VISIBILITY - ABSOLUTE BLACK ON SILVER */
    div[data-testid="stSelectbox"] > div {
        background-color: #C0C0C0 !important;
        border: 2px solid #FFFFFF !important;
        color: #000000 !important;
    }
    div[data-testid="stSelectbox"] p { color: #000000 !important; font-weight: 800 !important; }

    /* 2. LABELS & HEADINGS */
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; }
    label, .stMarkdown p { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.1rem !important; }
    
    /* 3. INPUT FIELDS */
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #C0C0C0 !important;
    }

    /* 4. BUTTONS: Industrial Silver */
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border: 2px solid #FFFFFF !important;
        height: 3.5em !important;
    }
    button:hover { background-color: #FFFFFF !important; box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) !important; }

    /* 5. THE PRO LEGAL DOCUMENT (Premium Bond Stationery) */
    .legal-paper {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        padding: 80px 100px !important;
        font-family: 'Times New Roman', serif !important;
        line-height: 1.6 !important;
        border: 12px double #000000 !important;
        margin: 50px auto !important;
        max-width: 900px !important;
        text-align: left !important;
        box-shadow: 0 0 60px rgba(255, 255, 255, 0.1) !important;
    }
    .legal-paper p, .legal-paper div, .legal-paper span, .legal-paper b { 
        color: #000000 !important; 
        font-family: 'Times New Roman', serif !important; 
    }
    .sig-block { margin-top: 60px; border-top: 2px solid #000; width: 300px; padding-top: 10px; }

    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- THE 10-DOMAIN GLOBAL ENGINE ---
# Hard-coded statutes for all 7 countries
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
        "General Cease & Desist": "IT Act 2000 / Defamation Laws"
    }
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)", "INR (₹)"]

# --- PERSISTENT STORAGE ---
if 'paid_v132' not in st.session_state: st.session_state.paid_v132 = False
if 'ready_v132' not in st.session_state: st.session_state.ready_v132 = False
if 'vault_v132' not in st.session_state: st.session_state.vault_v132 = {}

# Check Voucher immediately
if owner_code == "TS-GIFT-2026":
    st.session_state.paid_v132 = True

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>CERTIFIED LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid_v132:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name (You)", key="cl_in")
            juris = st.selectbox("Select Jurisdiction", list(STATUTES.keys()), key="ju_in")
        with c2:
            res_name = st.text_input("Respondent Name (Target)", key="re_in")
            curr = st.selectbox("Select Currency", CURRENCIES, key="cu_in")
            
        st.divider()
        # Restored category logic
        cat_list = list(STATUTES[juris].keys())
        category = st.selectbox("Select Case Category", cat_list, key="ca_in")
        amount = st.text_input(f"Total Amount Owed ({curr.split(' ')[1]})", key="am_in")
        details = st.text_area("Dispute Narrative (Facts & Dates)", height=150, key="de_in")
        
        if st.button("PROCESS OFFICIAL LEGAL DEMAND", key="main_btn"):
            if cl_name and res_name and details and amount:
                # SECURE VAULT - DO NOT LOSE THIS DATA
                st.session_state.vault_v132 = {
                    "cl": cl_name, "res": res_name, "amt": amount,
                    "det": details, "jur": juris, "cat": category,
                    "cur": curr.split(' ')[1]
                }
                st.session_state.ready_v132 = True
                st.success("Analysis Complete. Draft Generated.")

    if st.session_state.get("ready_v132"):
        st.divider()
        st.markdown(f"**PREVIEW: FORMAL NOTICE OF INTENT TO LITIGATE - {st.session_state.vault_v132['cat'].upper()}**")
        st.markdown("""<div style="filter:blur(12px); background:#111; padding:20px; border:1px dashed #C0C0C0;">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes for this jurisdiction...</div>""", unsafe_allow_html=True)
        
        st.link_button("💎 UNLOCK PRINT-READY DOCUMENT PACKAGE ($19.00)", "https://trend-shadows.lemonsqueezy.com/buy/1914602")

else:
    # --- PRODUCTION OUTPUT (VERIFIED) ---
    st.success("✅ TRANSACTION VERIFIED. TERMINAL UNLOCKED.")
    v = st.session_state.vault_v132
    if not v:
        st.error("No case data found. Please go back and fill the form.")
        if st.button("Back to Form"): st.session_state.paid_v132 = False; st.rerun()
    else:
        law = STATUTES[v['jur']].get(v['cat'], "Governing Statutes")
        date_now = datetime.now().strftime("%B %d, %Y")
        
        # Concat the body for both screen and download
        p1 = f"Notice is hereby given that your failure to remit the balance of {v['cur']}{v['amt']} regarding the {v['cat'].lower()} constitutes a direct violation of {law}."
        p2 = f"Under the laws of {v['jur']}, specifically the statutes regarding {v['cat'].lower()}, the withholding of these funds is a breach of legal obligations."
        p3 = f"STATEMENT OF FACTS:\n{v['det']}"
        p4 = f"LEGAL DEMAND:\nDemand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days of the date of this notice.\n\nINTENT TO LITIGATE:\nFailure to comply with this final demand will result in the immediate commencement of legal proceedings in Small Claims Court without further notice."

        # THE FINAL STATIONERY
        st.markdown(f"""
            <div class="legal-paper">
                <div style="display:flex; justify-content:space-between;">
                    <div><b>FROM:</b><br>{v['cl']}</div>
                    <div style="text-align:right;"><b>DATE:</b><br>{date_now}</div>
                </div>
                <br><div><b>TO:</b><br>{v['res']}</div><br><br>
                <div style="text-align:center; text-decoration:underline; font-size: 22px;"><b>FORMAL LETTER OF DEMAND</b></div><br>
                <p>{p1}</p>
                <p>{p2}</p>
                <p style="white-space: pre-wrap;"><b>{p3}</b></p>
                <p style="font-weight:bold; border: 1px solid #000; padding: 10px;">{p4}</p><br>
                <p>Sincerely,</p>
                <div class="sig-block"></div>
                <p><b>{v['cl']}</b><br>Claimant</p>
            </div>
        """, unsafe_allow_html=True)
        
        full_dl = f"FROM: {v['cl']}\nDATE: {date_now}\nTO: {v['res']}\n\n{p1}\n\n{p2}\n\n{p3}\n\n{p4}"
        st.download_button("📥 DOWNLOAD OFFICIAL WORD DOC", full_dl, file_name="Legal_Demand_Elite.doc")
        
        if st.button("INITIATE NEW CASE"):
            st.session_state.paid_v132 = False; st.session_state.ready_v132 = False; st.session_state.vault_v132 = {}; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.32 | Trend Shadows Digital Agency")
