import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Executive Edition v1.12)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: PROFESSIONAL COMMERCIAL STANDARD - PAYMENT INTEGRATED
# ============================================================

st.set_page_config(
    page_title="JusticeBot Pro | Trend Shadows",
    layout="wide"
)

# --- MASTER CSS OVERHAUL (v1.12 - High Contrast & No Emojis) ---
st.markdown("""
    <style>
    /* Global Body Background */
    .stApp { 
        background-color: #000000 !important; 
    }

    /* FORCE BUTTON VISIBILITY: SOLID SILVER BACKGROUND, SOLID BLACK TEXT */
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

    button:hover {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    /* Input Field visibility: Dark obsidian box, Pure White text */
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #C0C0C0 !important;
        font-size: 16px !important;
    }

    /* Label Visibility: Pure White */
    label, p, .stMarkdown, .stSelectbox label {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        opacity: 1.0 !important;
    }

    /* High-End White Paper (Black Text for Printing) */
    .legal-paper {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        padding: 50px 70px !important;
        font-family: 'Times New Roman', serif !important;
        line-height: 1.6 !important;
        border: 3px solid #000000 !important;
        margin: 20px auto !important;
        max-width: 850px !important;
        text-align: left !important;
    }
    
    .legal-paper b, .legal-paper p, .legal-paper div, .legal-paper span, .legal-paper pre {
        color: #000000 !important;
        font-family: 'Times New Roman', serif !important;
    }

    /* Paywall Blur */
    .blur-zone {
        filter: blur(12px);
        background: rgba(20, 20, 20, 0.9);
        padding: 30px;
        border: 1px dashed #C0C0C0;
        color: #FFFFFF !important;
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

# --- APP STATE ---
if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

# --- BRANDING ---
st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot AI Pro")
st.markdown("<p style='letter-spacing:5px; color:#888; font-weight:400;'>ELITE LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

# --- INPUT PHASE ---
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
        
        # PRIMARY ACTION BUTTON
        if st.button("ARCHITECT LEGAL DEMAND"):
            if cl_name and res_name and details and amount:
                st.session_state.cl_name = cl_name
                st.session_state.cl_addr = cl_addr
                st.session_state.res_name = res_name
                st.session_state.res_addr = res_addr
                st.session_state.amount = amount
                st.session_state.details = details
                st.session_state.ref_no = ref_no
                st.session_state.category = category
                st.session_state.jurisdiction = jurisdiction
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Encrypted Below.")
            else:
                st.error("Protocol Error: All intelligence fields must be completed.")

    if st.session_state.ready:
        st.divider()
        st.markdown("### 📄 Encrypted Draft Preview")
        st.info("PROTOCOL: Legal draft encrypted. High-level verification required for full access.")
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.category.upper()}**")
        
        st.markdown("""<div class="blur-zone">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes for this jurisdiction. Our AI has identified specific breaches of contract and consumer law. Failure to remit funds will result in immediate filing in Small Claims Court... [LEGAL CITATIONS ENCRYPTED]</div>""", unsafe_allow_html=True)
        
        if st.button("UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            # LEMON SQUEEZY PAYMENT REDIRECT (Executive Request)
            payment_url = "https://trendshadows.lemonsqueezy.com/checkout/buy/justicebot-unlock"
            st.markdown(f"""<meta http-equiv="refresh" content="0; url={payment_url}">
                <div style="text-align:center; padding:20px;">
                    <p>Redirecting to Secure Executive Checkout...</p>
                    <a href="{payment_url}" style="color:#C0C0C0;">Click here if not redirected automatically</a>
                </div>""", unsafe_allow_html=True)
            time.sleep(2)
            # Simulated unlock for testing
            st.session_state.paid = True
            st.rerun()

else:
    # --- OUTPUT PHASE (PAID) ---
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    
    statute_jargon = JURISDICTIONS[st.session_state.jurisdiction].get(st.session_state.category, "Governing Civil Codes")
    date_now = datetime.now().strftime("%B %d, %Y")
    
    final_body_content = f"""Notice is hereby given that your failure to remit the balance of {st.session_state.amount} constitutes a direct violation of {statute_jargon}.

Regarding the specific matter of: {st.session_state.details}

Under the laws of {st.session_state.jurisdiction}, specifically the statutes regarding {st.session_state.category.lower()}, your withholding of these funds is a breach of your legal obligations.

LEGAL DEMAND:
Demand is hereby made for the immediate payment of the full balance of {st.session_state.amount}. This payment must be received in full within fourteen (14) calendar days of the date of this notice.

INTENT TO LITIGATE:
Failure to comply with this final demand will result in the immediate commencement of legal proceedings in Small Claims Court without further notice. We will pursue the recovery of the full amount, statutory interest at the prescribed rate, and all associated legal and court costs.

Consider this the FINAL NOTICE before formal filing in the {st.session_state.jurisdiction} court system."""

    full_doc_text = f"""FROM: {st.session_state.cl_name}
{st.session_state.cl_addr}

DATE: {date_now}

TO: {st.session_state.res_name}
{st.session_state.res_addr}

RE: FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE
REFERENCE NO: {st.session_state.ref_no}
TOTAL SUM OUTSTANDING: {st.session_state.amount}

{final_body_content}

Sincerely,

___________________________
{st.session_state.cl_name}
DRAFTED BY: JUSTICEBOT AI EXECUTIVE"""

    # 1. THE HIGH-PIXEL PAPER PREVIEW
    st.markdown(f"""
        <div class="legal-paper">
            <div style="display:flex; justify-content:space-between; width:100%;">
                <div style="text-align:left;"><b>FROM:</b><br>{st.session_state.cl_name}<br>{st.session_state.cl_addr}</div>
                <div style="text-align:right;"><b>DATE:</b><br>{date_now}</div>
            </div>
            <br>
            <div style="text-align:left;"><b>TO:</b><br>{st.session_state.res_name}<br>{st.session_state.res_addr}</div>
            <br><br>
            <div style="text-align:center; text-decoration:underline; font-size: 20px;"><b>FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE</b></div>
            <br>
            <div style="display:flex; justify-content:space-between; width:100%;">
                <div style="text-align:left;"><b>REF:</b> {st.session_state.ref_no}</div>
                <div style="text-align:right;"><b>AMOUNT:</b> {st.session_state.amount}</div>
            </div>
            <br>
            <p style="white-space: pre-wrap;">{final_body_content}</p>
            <br>
            <p>Sincerely,</p>
            <br>
            <p>___________________________<br><b>{st.session_state.cl_name}</b></p>
        </div>
    """, unsafe_allow_html=True)

    # 2. DOWNLOAD BUTTONS
    word_export = f"<html><body style='font-family:serif; padding:1in;'><div style='border: 3px solid #000; padding: 0.5in; min-height: 9.5in;'><table width='100%'><tr><td align='left'><b>FROM:</b><br>{st.session_state.cl_name}<br>{st.session_state.cl_addr}</td><td align='right' valign='top'><b>DATE:</b><br>{date_now}</td></tr></table><br><b>TO:</b><br>{st.session_state.res_name}<br>{st.session_state.res_addr}<br><br><br><div align='center'><u><b>FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE</b></u></div><br><table width='100%'><tr><td><b>REF:</b> {st.session_state.ref_no}</td><td align='right'><b>AMOUNT:</b> {st.session_state.amount}</td></tr></table><br><p style='white-space:pre-wrap;'>{final_body_content}</p><br><br><p>Sincerely,</p><br><p>___________________________<br>{st.session_state.cl_name}</p></div></body></html>"
    
    st.download_button("DOWNLOAD OFFICIAL WORD DOCUMENT", word_export, file_name="JusticeBot_Formal_Demand.doc")
    st.download_button("DOWNLOAD PLAIN TEXT FILE", full_doc_text, file_name="JusticeBot_Formal_Demand.txt")

    if st.button("INITIATE NEW CASE"):
        st.session_state.paid = False; st.session_state.ready = False; st.rerun()

st.divider()
st.caption("Shadow-Build Engine v1.12 | Trend Shadows Digital Agency")
