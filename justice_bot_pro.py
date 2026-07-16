import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Executive Edition v1.12)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: COMMERCIAL STANDARD - PAYMENT INTEGRATED
# ============================================================

st.set_page_config(
    page_title="JusticeBot Pro | Trend Shadows",
    layout="wide"
)

# --- NUCLEAR CSS OVERHAUL (v1.12 - High Contrast & No Emojis) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important;
        color: #000000 !important;
        border: 2px solid #FFFFFF !important;
        font-weight: 900 !important;
        font-family: 'Inter', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        height: 3.5em !important;
        width: 100% !important;
        opacity: 1.0 !important;
        visibility: visible !important;
    }
    button p, .stButton>button p, .stDownloadButton>button p {
        color: #000000 !important;
        font-weight: 900 !important;
    }
    button:hover { background-color: #FFFFFF !important; color: #000000 !important; }
    .stTextArea textarea, .stTextInput input {
        background-color: #111 !important; color: #FFFFFF !important; border: 1px solid #C0C0C0 !important;
    }
    label, p, .stMarkdown, .stSelectbox label {
        color: #FFFFFF !important; font-weight: 700 !important; opacity: 1.0 !important;
    }
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important;
        padding: 50px 70px !important; font-family: 'Times New Roman', serif !important;
        line-height: 1.6 !important; border: 3px solid #000000 !important;
        margin: 20px auto !important; max-width: 850px !important; text-align: left !important;
    }
    .legal-paper b, .legal-paper p, .legal-paper div, .legal-paper span, .legal-paper pre {
        color: #000000 !important; font-family: 'Times New Roman', serif !important;
    }
    .blur-zone {
        filter: blur(12px); background: rgba(20, 20, 20, 0.9);
        padding: 30px; border: 1px dashed #C0C0C0; color: #FFFFFF !important;
    }
    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- LEGAL STATUTE ENGINE ---
JURISDICTIONS = {
    "United States (US)": {
        "Security Deposit Recovery": "US Civil Code Section 1950.5 and the Uniform Residential Landlord and Tenant Act (URLTA)",
        "Unpaid Freelance Invoice": "Uniform Commercial Code (UCC) and State Breach of Contract Statutes",
        "Faulty Product Refund": "Magnuson-Moss Warranty Act and UCC Article 2",
        "Other Legal Matter": "Consumer Protection Act and relevant Civil Statutes"
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": "Housing Act 2004 (Tenancy Deposit Protection) and Landlord and Tenant Act 1985",
        "Unpaid Freelance Invoice": "Late Payment of Commercial Debts (Interest) Act 1998",
        "Faulty Product Refund": "Consumer Rights Act 2015",
        "Other Legal Matter": "Common Law and relevant Statutory Instruments"
    },
    "South Africa (ZA)": {
        "Security Deposit Recovery": "Rental Housing Act 50 of 1999 and the Rental Housing Amendment Act 2014",
        "Unpaid Freelance Invoice": "Section 11 of the Prescription Act and Common Law Breach of Contract",
        "Faulty Product Refund": "Consumer Protection Act 68 of 2008 (Section 55 and 56)",
        "Other Legal Matter": "Constitutionally aligned Consumer Protection Statutes"
    }
}

if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot AI Pro")
st.markdown("<p style='letter-spacing:5px; color:#888; font-weight:400;'>ELITE LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name (You)")
            cl_addr = st.text_area("Claimant Physical Address", height=80)
        with c2:
            res_name = st.text_input("Respondent Name (Company or Person)")
            res_addr = st.text_area("Respondent Physical Address", height=80)
        st.divider()
        c3, c4 = st.columns(2)
        with c3:
            jurisdiction = st.selectbox("Legal Jurisdiction", list(JURISDICTIONS.keys()))
            category = st.selectbox("Case Category", list(JURISDICTIONS[jurisdiction].keys()))
        with c4:
            ref_no = st.text_input("Ref Number (Invoice / Lease / ID)")
            amount = st.text_input("Total Amount Owed (Including Currency)")
        details = st.text_area("Sequence of Events (Describe the dispute)", height=150)
        if st.button("ARCHITECT LEGAL DEMAND"):
            if cl_name and res_name and details and amount:
                st.session_state.cl_name, st.session_state.cl_addr = cl_name, cl_addr
                st.session_state.res_name, st.session_state.res_addr = res_name, res_addr
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.ref_no, st.session_state.category = ref_no, category
                st.session_state.jurisdiction = jurisdiction
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Encrypted Below.")
            else: st.error("Protocol Error: All intelligence fields must be completed.")

    if st.session_state.ready:
        st.divider()
        st.markdown("### 📄 Encrypted Draft Preview")
        st.write(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.category.upper()}**")
        st.markdown("""<div class="blur-zone">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes... [LEGAL CITATIONS ENCRYPTED]</div>""", unsafe_allow_html=True)
        if st.button("UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            # LEMON SQUEEZY PAYMENT REDIRECT
            payment_url = "PASTE_YOUR_LINK_HERE"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={payment_url}">', unsafe_allow_html=True)
            time.sleep(2)
            # st.session_state.paid = True # Comment this out after testing

else:
    # --- OUTPUT PHASE (PAID) ---
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    statute_jargon = JURISDICTIONS[st.session_state.jurisdiction].get(st.session_state.category, "Governing Civil Codes")
    date_now = datetime.now().strftime("%B %d, %Y")
    final_body_content = f"""Notice is hereby given that your failure to remit the balance of {st.session_state.amount} constitutes a direct violation of {statute_jargon}.\n\nUnder the laws of {st.session_state.jurisdiction}, your withholding of these funds is a breach of legal obligations."""
    st.markdown(f"""<div class="legal-paper"><b>FROM:</b><br>{st.session_state.cl_name}<br>{st.session_state.cl_addr}<br><br><b>TO:</b><br>{st.session_state.res_name}<br>{st.session_state.res_addr}<br><br><p>{final_body_content}</p></div>""", unsafe_allow_html=True)
    st.download_button("DOWNLOAD OFFICIAL WORD DOCUMENT", final_body_content, file_name="JusticeBot_Formal_Demand.doc")
