import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Executive Edition v1.13 - FINAL)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: LIVE ON CLOUD / COMMERCIAL REVENUE ACTIVE
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Trend Shadows", layout="wide")

# --- EXECUTIVE CSS (Industrial Silver & Obsidian) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; }
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important; border: 2px solid #FFFFFF !important;
        font-weight: 900 !important; text-transform: uppercase !important; height: 3.5em !important; width: 100% !important;
    }
    button:hover { background-color: #FFFFFF !important; box-shadow: 0 0 20px rgba(255,255,255,0.4) !important; }
    .stTextArea textarea, .stTextInput input { background-color: #111 !important; color: #FFFFFF !important; border: 1px solid #C0C0C0 !important; }
    label, p, .stMarkdown { color: #FFFFFF !important; font-weight: 700 !important; }
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important; padding: 50px 70px !important;
        font-family: 'Times New Roman', serif !important; line-height: 1.6 !important; border: 3px solid #000000 !important;
        margin: 20px auto !important; max-width: 800px !important; text-align: left !important;
    }
    .blur-zone { filter: blur(12px); background: rgba(20,20,20,0.9); padding: 30px; border: 1px dashed #C0C0C0; color: #fff !important; }
    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- STATUTE ENGINE ---
JURISDICTIONS = {
    "United States (US)": "US Civil Code Section 1950.5 and the Uniform Residential Landlord and Tenant Act (URLTA)",
    "United Kingdom (UK)": "Housing Act 2004 and the Consumer Rights Act 2015",
    "South Africa (ZA)": "Rental Housing Act 50 of 1999 and the Consumer Protection Act 68 of 2008"
}

if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot AI Pro")
st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>ELITE LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Name (You)")
            cl_addr = st.text_area("Your Address", height=80)
        with c2:
            res_name = st.text_input("Respondent Name (Company or Person)")
            res_addr = st.text_area("Opposing Party Address", height=80)
        st.divider()
        c3, c4 = st.columns(2)
        with c3:
            juris = st.selectbox("Jurisdiction", list(JURISDICTIONS.keys()))
            ref_no = st.text_input("Reference No (Invoice / Lease / ID)")
        with c4:
            amount = st.text_input("Total Amount Owed (Including Currency)")
        details = st.text_area("Dispute Narrative (Be thorough and precise)", height=150)

        if st.button("ARCHITECT LEGAL DEMAND"):
            if cl_name and res_name and details:
                st.session_state.cl_name, st.session_state.cl_addr = cl_name, cl_addr
                st.session_state.res_name, st.session_state.res_addr = res_name, res_addr
                st.session_state.amount, st.session_state.details = amount, details
                st.session_state.juris, st.session_state.ref_no = juris, ref_no
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Encrypted Below.")

    if st.session_state.ready:
        st.divider()
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE**")
        st.markdown("""<div class="blur-zone">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes for this jurisdiction. Our AI has identified specific breaches of contract and consumer law. Failure to remit funds will result in immediate filing in Small Claims Court... [LEGAL CITATIONS ENCRYPTED]</div>""", unsafe_allow_html=True)
        
        if st.button("💎 UNLOCK COMMERCIAL DOCUMENT PACKAGE"):
            # CONNECTING TO YOUR LEMONSQUEEZY CASH REGISTER
            checkout_url = "https://trend-shadows.lemonsqueezy.com/buy/1914602"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={checkout_url}">', unsafe_allow_html=True)
            st.info("Redirecting to Secure Executive Checkout...")
            time.sleep(2)

else:
    st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
    law = JURISDICTIONS[st.session_state.juris]
    date_now = datetime.now().strftime("%B %d, %Y")
    body = f"""Notice is hereby given that your failure to remit the balance of {st.session_state.amount} constitutes a direct violation of {law}. Specifically, the withholding of these funds regarding the matter of: {st.session_state.details} represents a breach of legal obligations. \n\nLEGAL DEMAND: Demand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days. Failure to comply will result in an immediate filing in Small Claims Court without further notice."""
    
    st.markdown(f"""<div class="legal-paper"><div style="display:flex; justify-content:space-between;"><div><b>FROM:</b><br>{st.session_state.cl_name}</div><div><b>DATE:</b><br>{date_now}</div></div><br><b>TO:</b><br>{st.session_state.res_name}<br><br><div style="text-align:center; text-decoration:underline;"><b>FORMAL LETTER OF DEMAND</b></div><br><b>REF:</b> {st.session_state.ref_no}<br><p>{body}</p></div>""", unsafe_allow_html=True)
    st.download_button("📥 DOWNLOAD PRINT-READY DOCUMENT", body, file_name="Legal_Demand.doc")
