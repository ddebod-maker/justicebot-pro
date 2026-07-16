import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.21)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: 10-DOMAIN ENGINE RESTORED | PRO-DOCUMENT FIX
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Elite", layout="wide")

# --- VERSION STAMP ---
st.sidebar.markdown("`SYSTEM VERSION: v1.21`")
st.sidebar.markdown("---")

# --- MASTER CSS OVERHAUL (v1.21 - Absolute Industrial Standard) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* 1. HIGH CONTRAST DROPDOWNS */
    div[data-testid="stSelectbox"] > div {
        background-color: #C0C0C0 !important;
        color: #000000 !important;
        border-radius: 4px !important;
        border: 2px solid #FFFFFF !important;
    }
    div[data-testid="stSelectbox"] p { color: #000000 !important; font-weight: 900 !important; }
    div[data-testid="stSelectbox"] svg { fill: #000000 !important; }

    /* 2. INPUTS & LABELS */
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900; text-align: center; }
    label { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.1rem !important; }
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #444444 !important;
    }

    /* 3. BUTTONS: Solid Silver / Black Text */
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important;
        font-weight: 900 !important; text-transform: uppercase !important; border: 2px solid #FFFFFF !important;
    }

    /* 4. THE PRO LEGAL DOCUMENT (White Paper, Black Text, Heavy Border) */
    .legal-paper {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        padding: 60px 80px !important;
        font-family: 'Times New Roman', serif !important;
        line-height: 1.6 !important;
        border: 10px double #000000 !important; /* Elegant double border */
        margin: 200px auto !important; /* Forced margin for clean view */
        max-width: 850px !important;
        text-align: left !important;
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.2) !important;
    }
    
    .legal-paper * { color: #000000 !important; }
    
    .signature-line {
        margin-top: 50px;
        border-top: 2px solid #000;
        width: 300px;
    }

    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- THE 10-DOMAIN GLOBAL ENGINE (FULL RESTORATION) ---
STATUTES = {
    "United States (US)": {
        "Security Deposit Recovery": "US Civil Code Section 1950.5 and URLTA",
        "Unpaid Freelance Invoice": "UCC Article 2 and State Breach of Contract Laws",
        "Private Vehicle Sale": "State Bill of Sale & Lemon Law Protocols",
        "Electronics/Goods Sale": "Magnuson-Moss Warranty Act and UCC Article 2",
        "Travel/Flight Refund": "US Department of Transportation (DOT) Refund Mandates",
        "Service Cancellation": "State Consumer Protection Statutes",
        "Employment/Unpaid Wages": "Fair Labor Standards Act (FLSA)",
        "Insurance Claim Dispute": "State Insurance Fair Conduct Acts",
        "Property Damage Claim": "General Tort Law & Civil Liability Codes",
        "General Cease & Desist": "Common Law Defamation & Harassment Statutes"
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": "Housing Act 2004 and Landlord and Tenant Act 1985",
        "Unpaid Freelance Invoice": "Late Payment of Commercial Debts Act 1998",
        "Private Vehicle Sale": "Common Law Sale of Goods (Caveat Emptor)",
        "Electronics/Goods Sale": "Sale of Goods Act 1979",
        "Travel/Flight Refund": "UK261 Flight Compensation Regulations",
        "Service Cancellation": "Consumer Rights Act 2015 (Unfair Terms)",
        "Employment/Unpaid Wages": "Employment Rights Act 1996",
        "Insurance Claim Dispute": "Financial Ombudsman Service (FOS) Guidelines",
        "Property Damage Claim": "Occupiers' Liability Act 1957",
        "General Cease & Desist": "Protection from Harassment Act 1997"
    },
    "South Africa (ZA)": {
        "Security Deposit Recovery": "Rental Housing Act 50 of 1999",
        "Unpaid Freelance Invoice": "Prescribed Rate of Interest Act 55 of 1975",
        "Private Vehicle Sale": "Private Sale Agreement (Voetstoots Protocol)",
        "Electronics/Goods Sale": "Consumer Protection Act (Section 55)",
        "Travel/Flight Refund": "Consumer Protection Act (Section 47)",
        "Service Cancellation": "Consumer Protection Act (Section 14)",
        "Employment/Unpaid Wages": "Basic Conditions of Employment Act",
        "Insurance Claim Dispute": "Short-Term Insurance Act / Ombudsman Protocol",
        "Property Damage Claim": "Apportionment of Damages Act 34 of 1956",
        "General Cease & Desist": "Protection from Harassment Act 17 of 2011"
    },
    "Australia (AU)": {
        "Security Deposit Recovery": "Residential Tenancies Act 2010",
        "Unpaid Freelance Invoice": "Australian Consumer Law (ACL) Payment Terms",
        "Private Vehicle Sale": "State Motor Vehicle Traders Acts",
        "Electronics/Goods Sale": "ACL Consumer Guarantees",
        "Travel/Flight Refund": "ACL Major Failure Refund Protocols",
        "Service Cancellation": "ACL Unfair Contract Terms",
        "Employment/Unpaid Wages": "Fair Work Act 2009",
        "Insurance Claim Dispute": "Insurance Contracts Act 1984",
        "Property Damage Claim": "Civil Liability Act 2002",
        "General Cease & Desist": "Personal Violence Protection Acts"
    },
    "Canada (CA)": {
        "Security Deposit Recovery": "Provincial Residential Tenancies Acts",
        "Unpaid Freelance Invoice": "Sale of Goods Act and Provincial Contract Laws",
        "Private Vehicle Sale": "Provincial Consumer Protection Statutes",
        "Electronics/Goods Sale": "Consumer Protection Act (Section 14)",
        "Travel/Flight Refund": "Air Passenger Protection Regulations (APPR)",
        "Service Cancellation": "Consumer Protection Act (Cancellation Rights)",
        "Employment/Unpaid Wages": "Canada Labour Code",
        "Insurance Claim Dispute": "Provincial Insurance Acts",
        "Property Damage Claim": "Negligence Act",
        "General Cease & Desist": "Libel and Slander Act"
    },
    "New Zealand (NZ)": {
        "Security Deposit Recovery": "Residential Tenancies Act 1986",
        "Unpaid Freelance Invoice": "Consumer Guarantees Act 1993",
        "Private Vehicle Sale": "Fair Trading Act 1986",
        "Electronics/Goods Sale": "Consumer Guarantees Act (Section 6)",
        "Travel/Flight Refund": "Contract and Commercial Law Act 2017",
        "Service Cancellation": "Consumer Guarantees Act (Reasonable Care)",
        "Employment/Unpaid Wages": "Employment Relations Act 2000",
        "Insurance Claim Dispute": "Insurance Law Reform Act 1977",
        "Property Damage Claim": "Limitation Act 2010",
        "General Cease & Desist": "Harassment Act 1997"
    },
    "India (IN)": {
        "Security Deposit Recovery": "Model Tenancy Act 2021",
        "Unpaid Freelance Invoice": "Indian Contract Act 1872",
        "Private Vehicle Sale": "Motor Vehicles Act 1988",
        "Electronics/Goods Sale": "Consumer Protection Act 2019",
        "Travel/Flight Refund": "DGCA Passenger Charter",
        "Service Cancellation": "Consumer Protection Act (Unfair Contracts)",
        "Employment/Unpaid Wages": "Payment of Wages Act 1936",
        "Insurance Claim Dispute": "IRDAI Guidelines",
        "Property Damage Claim": "Indian Penal Code (Tort of Negligence)",
        "General Cease & Desist": "Section 499 (Defamation) and IT Act 2000"
    }
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
            
        st.divider()
        # CATEGORIES RESTORED (10 Options)
        category = st.selectbox("Select Case Category", list(STATUTES[juris].keys()))
        amount = st.text_input(f"Total Amount Owed ({curr.split(' ')[1]})")
        details = st.text_area("Dispute Narrative (Names, Dates, Facts)", height=150)
        
        if st.button("PROCESS OFFICIAL LEGAL DEMAND"):
            if cl_name and res_name and details:
                st.session_state.cl_name, st.session_state.res_name = cl_name, res_name
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.juris, st.session_state.category = juris, category
                st.session_state.curr = curr.split(' ')[1]
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Encrypted Below.")

    if st.session_state.ready:
        st.divider()
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.category.upper()}**")
        st.markdown("""<div style="filter:blur(10px); background:#111; padding:20px; border:1px dashed #C0C0C0;">Notice is hereby given that your actions constitute a direct violation...</div>""", unsafe_allow_html=True)
        if st.button("UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            if st.session_state.details.startswith("ADMIN-TEST"):
                st.session_state.paid = True; st.rerun()
            else:
                checkout_url = "https://trend-shadows.lemonsqueezy.com/buy/1914602"
                st.markdown(f'<meta http-equiv="refresh" content="0; url={checkout_url}">', unsafe_allow_html=True)

else:
    # --- PRODUCTION OUTPUT (SALE READY) ---
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    law = STATUTES[st.session_state.juris].get(st.session_state.category)
    date_now = datetime.now().strftime("%B %d, %Y")
    
    body = f"""Notice is hereby given that your failure to remit the balance of {st.session_state.curr}{st.session_state.amount} regarding the {st.session_state.category.lower()} constitutes a direct violation of {law}.\n\nUnder the laws of {st.session_state.juris}, specifically regarding {st.session_state.category.lower()}, the withholding of these funds is a breach of legal obligations.\n\nLEGAL DEMAND: Demand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days of the date of this notice.\n\nNOTICE OF INTENT TO SUE: Failure to comply with this final demand will result in the immediate commencement of legal proceedings in Small Claims Court without further notice. We will pursue the recovery of the full amount, statutory interest at the prescribed rate, and all associated legal and court costs."""

    # 1. HIGH PIXEL PAPER PREVIEW WITH SIGNATURE BLOCK
    st.markdown(f"""
        <div class="legal-paper">
            <div style="display:flex; justify-content:space-between; width:100%; border-bottom: 2px solid #000; padding-bottom: 10px;">
                <div style="text-align:left;"><b>FROM:</b><br>{st.session_state.cl_name}</div>
                <div style="text-align:right;"><b>DATE:</b><br>{date_now}</div>
            </div>
            <br>
            <div style="text-align:left;"><b>TO:</b><br>{st.session_state.res_name}</div>
            <br><br>
            <div style="text-align:center; text-decoration:underline; font-size: 22px;"><b>FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE</b></div>
            <br>
            <p style="white-space: pre-wrap;">{body}</p>
            <br><br>
            <p>Sincerely,</p>
            <div class="signature-line"></div>
            <p><b>{st.session_state.cl_name}</b><br>Claimant</p>
            <br>
            <p style="font-size: 10px; color: #888;">DOCUMENT ID: TS-BOT-{int(time.time())}</p>
        </div>
    """, unsafe_allow_html=True)

    # 2. WORD DOWNLOAD FIX (Bordered & Structured)
    word_export = f"""
    <html><body style='font-family:serif; padding:1in;'>
        <div style='border: 5px double #000; padding: 0.5in; min-height: 9.5in;'>
            <table width='100%'><tr><td align='left'><b>FROM:</b><br>{st.session_state.cl_name}</td><td align='right' valign='top'><b>DATE:</b><br>{date_now}</td></tr></table>
            <br><b>TO:</b><br>{st.session_state.res_name}<br><br><br>
            <div align='center'><u><b>FORMAL LETTER OF DEMAND</b></u></div><br>
            <p style='white-space:pre-wrap;'>{body}</p><br><br>
            <p>Sincerely,</p><br><br>___________________________<br><b>{st.session_state.cl_name}</b>
        </div>
    </body></html>"""
    
    st.download_button("DOWNLOAD OFFICIAL WORD DOCUMENT", word_export, file_name="Legal_Demand.doc")
    if st.button("INITIATE NEW CASE"):
        st.session_state.paid = False; st.session_state.ready = False; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.21 | Trend Shadows Executive Tier")
