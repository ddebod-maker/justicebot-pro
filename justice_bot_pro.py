import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.15)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: GLOBAL SCALE ACTIVE - 7 JURISDICTIONS | 10 DOMAINS
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Digital Asset", layout="wide")

# --- MASTER CSS (v1.15 - Global Industrial Silver) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; }
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important; border: 2px solid #FFFFFF !important;
        font-weight: 900 !important; text-transform: uppercase !important; height: 3.5em !important; width: 100% !important;
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
STATUTES = {
    "United States (US)": {
        "Security Deposit Recovery": "US Civil Code Section 1950.5",
        "Unpaid Freelance Invoice": "Uniform Commercial Code (UCC) Article 2",
        "Private Vehicle Sale": "Standard Bill of Sale & Lemon Law Statutes",
        "Electronics/Goods Sale": "UCC Warranties & Personal Property Transfer",
        "Travel/Flight Refund": "US Dept of Transportation (DOT) Refund Mandates",
        "Service Cancellation": "State Consumer Protection Statutes",
        "Employment/Unpaid Wages": "Fair Labor Standards Act (FLSA)",
        "Insurance Claim Dispute": "State Insurance Fair Conduct Acts",
        "Property Damage Claim": "General Tort Law & Civil Liability Codes",
        "General Cease & Desist": "Common Law Defamation & Harassment Statutes"
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": "Housing Act 2004",
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
        "Electronics/Goods Sale": "Consumer Protection Act 68 of 2008 (Section 55)",
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
        "Security Deposit Recovery": "Residential Tenancies Acts (Provincial)",
        "Unpaid Freelance Invoice": "Sale of Goods Act (Ontario/BC)",
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
        "Electronics/Goods Sale": "Consumer Protection Act 2019 (Section 2(7))",
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
st.markdown("<p style='letter-spacing:5px; color:#888; font-weight:400; text-align:center;'>INTERNATIONAL LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name")
            jurisdiction = st.selectbox("Jurisdiction", list(STATUTES.keys()))
        with c2:
            res_name = st.text_input("Respondent Name (Company or Person)")
            currency = st.selectbox("Preferred Currency", CURRENCIES)
            
        st.divider()
        category = st.selectbox("Case Category", list(STATUTES[jurisdiction].keys()))
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
        st.info("PROTOCOL: Legal draft generated for " + st.session_state.jurisdiction)
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.category.upper()}**")
        st.markdown("""<div class="blur-zone">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes. Our AI has identified specific breaches of legal duty. Failure to remit funds within 14 days will result in immediate filing... [STATUTORY CITATIONS ENCRYPTED]</div>""", unsafe_allow_html=True)
        if st.button("UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            checkout_url = "https://trend-shadows.lemonsqueezy.com/buy/1914602"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={checkout_url}">', unsafe_allow_html=True)

else:
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    law = STATUTES[st.session_state.jurisdiction].get(st.session_state.category)
    date_now = datetime.now().strftime("%B %d, %Y")
    
    final_body = f"""Notice is hereby given that your failure to remit the balance of {st.session_state.currency}{st.session_state.amount} regarding the {st.session_state.category.lower()} constitutes a direct violation of {law}.\n\nUnder the laws of {st.session_state.jurisdiction}, the withholding of these funds or failure to resolve this matter is a breach of legal obligations.\n\nDISPUTE DETAILS:\n{st.session_state.details}\n\nLEGAL DEMAND:\nDemand is hereby made for the immediate payment of the full balance. This must be received in full within fourteen (14) calendar days of the date of this notice.\n\nNOTICE OF INTENT TO SUE:\nFailure to comply will result in the immediate commencement of legal proceedings in Small Claims Court without further notice. We will pursue the recovery of the full amount, interest, and legal costs."""

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

st.divider()
st.caption("Shadow-Build Global Engine v1.15 | Trend Shadows Digital Agency")
