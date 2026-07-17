import streamlit as st
import time
from datetime import datetime

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.38)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: INDUSTRIAL LEGAL STANDARD | WORD EXPORT FIXED
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Elite", layout="wide")

# --- VERSION STAMP (Sidebar) ---
st.sidebar.markdown("### 🛠️ System Control")
st.sidebar.markdown(f"`VERSION: v1.38` (STABLE)")
st.sidebar.markdown(f"`BUILD DATE: {datetime.now().strftime('%Y-%m-%d')}`")
st.sidebar.markdown("---")

# --- MASTER CSS (Visibility & Industrial Finish) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    
    /* 1. DROPDOWN VISIBILITY - FORCED BLACK ON SILVER */
    div[data-testid="stSelectbox"] > div {
        background-color: #C0C0C0 !important; color: #000000 !important;
        border: 2px solid #FFFFFF !important;
        border-radius: 4px !important;
    }
    div[data-testid="stSelectbox"] * { color: #000000 !important; font-weight: 800 !important; }

    /* 2. LABELS & HEADINGS */
    h1 { color: #FFFFFF !important; font-family: 'serif'; font-weight: 900 !important; font-size: 3.5rem !important; text-align: center; }
    label, .stMarkdown p { color: #FFFFFF !important; font-weight: 700 !important; font-size: 1.1rem !important; }
    
    /* 3. INPUT FIELDS */
    .stTextArea textarea, .stTextInput input {
        background-color: #111111 !important; color: #FFFFFF !important; border: 1px solid #C0C0C0 !important;
        font-size: 16px !important;
    }

    /* 4. BUTTONS: Solid Industrial Silver */
    button, .stButton>button, .stDownloadButton>button {
        background-color: #C0C0C0 !important; color: #000000 !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        border: 2px solid #FFFFFF !important; height: 3.5em !important;
    }
    button:hover { background-color: #FFFFFF !important; box-shadow: 0 0 20px rgba(255, 255, 255, 0.5) !important; }

    /* 5. THE PRO LEGAL DOCUMENT (Premium Bond Stationery) */
    .legal-paper {
        background-color: #FFFFFF !important; color: #000000 !important;
        padding: 80px 100px !important; font-family: 'Times New Roman', serif !important;
        line-height: 1.6 !important; border: 1px solid #ddd !important;
        margin: 40px auto !important; max-width: 900px !important; text-align: left !important;
        box-shadow: 0 0 60px rgba(255, 255, 255, 0.1) !important;
    }
    .legal-paper * { color: #000000 !important; font-family: 'Times New Roman', serif !important; }
    .sig-line { margin-top: 60px; border-top: 2px solid #000; width: 300px; padding-top: 10px; }
    .doc-header { display: flex; justify-content: space-between; border-bottom: 2px solid #000; padding-bottom: 20px; margin-bottom: 30px; }

    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- THE 10-DOMAIN GLOBAL ENGINE ---
STATUTES = {
    "United States (US)": {
        "Security Deposit Recovery": "Civil Code Section 1950.5 and the Uniform Residential Landlord and Tenant Act (URLTA)",
        "Unpaid Freelance Invoice": "Uniform Commercial Code (UCC) Article 2 and state-specific Prompt Payment Acts",
        "Private Sale (Vehicle/Goods)": "UCC Article 2 governing the Sale of Goods and State Bill of Sale requirements",
        "Travel/Flight Refund": "14 CFR Part 259 and US Department of Transportation (DOT) consumer protection mandates",
        "Service Cancellation": "State Consumer Protection Statutes and the FTC Cooling-Off Rule",
        "Employment/Unpaid Wages": "Fair Labor Standards Act (FLSA)",
        "Insurance Claim Dispute": "State Insurance Fair Conduct Acts",
        "Property Damage Claim": "General Tort Law & Civil Liability Codes",
        "General Ceist & Desist": "Common Law Defamation & Harassment Statutes",
        "Custom / Other": "Relevant Consumer Protection and Civil Statutes"
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": "Housing Act 2004 (Tenancy Deposit Protection) and Landlord and Tenant Act 1985",
        "Unpaid Freelance Invoice": "Late Payment of Commercial Debts (Interest) Act 1998",
        "Private Sale (Vehicle/Goods)": "Sale of Goods Act 1979 and Common Law principles of Contract",
        "Travel/Flight Refund": "UK261 Flight Compensation Regulations and CAA guidelines",
        "Service Cancellation": "Consumer Rights Act 2015 regarding unfair terms",
        "Employment/Unpaid Wages": "Employment Rights Act 1996",
        "Insurance Claim Dispute": "Financial Ombudsman Service (FOS) Guidelines",
        "Property Damage Claim": "Occupiers' Liability Act 1957",
        "General Ceist & Desist": "Protection from Harassment Act 1997",
        "Custom / Other": "Relevant UK Common Law and Statutes"
    },
    "South Africa (ZA)": {
        "Security Deposit Recovery": "Rental Housing Act 50 of 1999 and the Rental Housing Amendment Act of 2014",
        "Unpaid Freelance Invoice": "Section 11 of the Prescription Act and Common Law Breach of Contract",
        "Private Sale (Vehicle/Goods)": "Common Law of Sale and the 'Voetstoots' clause protocols",
        "Electronics/Goods Sale": "Consumer Protection Act 68 of 2008 (Section 55 and 56)",
        "Travel/Flight Refund": "Consumer Protection Act (Section 47) and IATA International Conventions",
        "Service Cancellation": "Consumer Protection Act (Section 14)",
        "Employment/Unpaid Wages": "Basic Conditions of Employment Act",
        "Insurance Claim Dispute": "Short-Term Insurance Act / Ombudsman Protocol",
        "Property Damage Claim": "Apportionment of Damages Act 34 of 1956",
        "General Ceist & Desist": "Protection from Harassment Act 17 of 2011"
    },
    "Canada (CA)": {
        "Security Deposit Recovery": "Provincial Residential Tenancy Acts and local Housing Regulations",
        "Unpaid Freelance Invoice": "Provincial Sale of Goods Acts and Breach of Contract Common Law",
        "Private Sale (Vehicle/Goods)": "Consumer Protection Act (Provincial) and Standard Bill of Sale requirements",
        "Travel/Flight Refund": "Air Passenger Protection Regulations (APPR)",
        "Service Cancellation": "Provincial Consumer Protection Statutes",
        "Employment/Unpaid Wages": "Canada Labour Code",
        "Insurance Claim Dispute": "Provincial Insurance Acts",
        "Property Damage Claim": "Negligence Act",
        "General Ceist & Desist": "Libel and Slander Act",
        "Custom / Other": "Relevant Canadian Statutes and Regulations"
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
        "General Ceist & Desist": "IT Act 2000 / Defamation Laws"
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
        "General Ceist & Desist": "Personal Violence Protection Act"
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
        "General Ceist & Desist": "Harassment Act 1997"
    }
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)", "INR (₹)"]

# --- PERSISTENT STORAGE VAULT ---
if 'paid' not in st.session_state: st.session_state.paid = False
if 'ready' not in st.session_state: st.session_state.ready = False
if 'vault' not in st.session_state: st.session_state.vault = {}

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>CERTIFIED LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence Architecture")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name / Business", key="cl_v38")
            cl_addr = st.text_area("Claimant Physical Address", height=80, key="cla_v38")
            juris = st.selectbox("Select Jurisdiction", list(STATUTES.keys()), key="jur_v38")
        with c2:
            res_name = st.text_input("Respondent Name (Company or Person)", key="res_v38")
            res_addr = st.text_area("Respondent Physical Address", height=80, key="resa_v38")
            curr = st.selectbox("Select Currency", CURRENCIES, key="cur_v38")
            
        st.divider()
        category = st.selectbox("Case Category", list(STATUTES[juris].keys()), key="cat_v38")
        amount = st.text_input(f"Total Amount Owed ({curr.split(' ')[1]})", key="amt_v38")
        ref_no = st.text_input("Reference / Invoice / Lease Number", key="ref_v38")
        details = st.text_area("Dispute Narrative (Be thorough with dates and facts)", height=150, key="det_v38")
        
        if st.button("PROCESS OFFICIAL LEGAL DEMAND", key="btn_v38"):
            if cl_name and res_name and details and amount:
                # LOCK DATA INTO VAULT
                st.session_state.vault = {
                    "cl": cl_name, "cla": cl_addr, "res": res_name, "resa": res_addr,
                    "amt": amount, "det": details, "jur": juris, "cat": category,
                    "ref": ref_no, "cur": curr.split(' ')[1]
                }
                st.session_state.ready = True
                st.success("Logic Analysis Complete. Draft Ready.")
            else:
                st.error("Protocol Error: Please complete all required intelligence fields.")

    if st.session_state.ready:
        st.divider()
        st.markdown(f"**SUBJECT: FINAL NOTICE OF INTENT TO LITIGATE - {st.session_state.vault['cat'].upper()}**")
        st.markdown("""<div style="filter:blur(12px); background:#111; padding:20px; border:1px dashed #C0C0C0;">Notice is hereby given that your actions constitute a direct violation of the Governing Statutes for this jurisdiction...</div>""", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 💎 Unlock Document Package")
        v_code = st.text_input("Enter Voucher / Admin Code", type="password", key="vouch_v38")
        
        c_unlock, c_pay = st.columns(2)
        with c_unlock:
            if st.button("AUTHENTICATE VOUCHER", key="auth_v38"):
                if v_code == "TS-GIFT-2026":
                    st.session_state.paid = True
                    st.rerun()
                else:
                    st.error("Invalid Voucher Code")
        with c_pay:
            st.link_button("💎 PAY TO UNLOCK ($19.00)", "https://trend-shadows.lemonsqueezy.com/buy/1914602")

else:
    # --- PRODUCTION OUTPUT ---
    v = st.session_state.vault
    if not v:
        st.error("No case data found. Please return to the form.")
        if st.button("Back to Form"): st.session_state.paid = False; st.rerun()
    else:
        st.success("AUTHENTICATION SUCCESSFUL. DOCUMENT UNLOCKED.")
        law = STATUTES[v['jur']].get(v['cat'])
        date_now = datetime.now().strftime("%B %d, %Y")
        
        # --- THE PROFESSIONAL BODY (SUBSTANCE & BACKBONE) ---
        p1 = f"Regarding: {v['cat']} - {v['ref']}"
        p2 = f"This formal demand letter is issued in respect of the outstanding balance of {v['cur']}{v['amt']} currently owed to the Claimant. Despite previous attempts to resolve this matter amicably, the balance remains unpaid and is currently in arrears."
        p3 = f"STATEMENT OF FACTS:\n{v['det']}"
        p4 = f"LEGAL NOTICE:\nNotice is hereby given that your failure to remit payment or provide a statutory justification for withholding these funds constitutes a direct violation of {law}. Under the laws of {v['jur']}, specifically the statutes regarding {v['cat'].lower()}, your actions represent a breach of legal and fiduciary obligations."
        p5 = f"LEGAL DEMAND:\nDemand is hereby made for the immediate payment of {v['cur']}{v['amt']}. This payment must be received in full within fourteen (14) calendar days of the date of this notice."
        p6 = f"INTENT TO LITIGATE:\nFailure to comply with this final demand will result in the immediate commencement of legal proceedings in Small Claims Court without further notice. We will pursue the recovery of the debt, statutory interest at the prescribed rate, and all associated legal costs."

        # THE FINAL STATIONERY (Visual Preview)
        st.markdown(f"""
            <div class="legal-paper">
                <div class="doc-header">
                    <div style="color:#000;"><b>FROM:</b><br>{v['cl']}<br>{v['cla'].replace('\n','<br>')}</div>
                    <div style="text-align:right; color:#000;"><b>DATE:</b><br>{date_now}</div>
                </div>
                <div style="color:#000;"><b>TO:</b><br>{v['res']}<br>{v['resa'].replace('\n','<br>')}</div>
                <br><br>
                <div style="text-align:center; text-decoration:underline; font-size: 20px; color:#000;"><b>FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE</b></div>
                <br>
                <p style="color:#000;"><b>RE: {p1}</b></p>
                <p style="color:#000;">{p2}</p>
                <p style="white-space: pre-wrap; color:#000;"><b>{p3}</b></p>
                <p style="white-space: pre-wrap; color:#000;">{p4}</p>
                <p style="background-color: #f9f9f9; padding: 15px; border-left: 5px solid #000; color:#000;">{p5}</p>
                <p style="color:#000;">{p6}</p>
                <br><p style="color:#000;">Sincerely,</p>
                <div class="sig-line"></div>
                <p style="color:#000;"><b>{v['cl']}</b><br>Claimant</p>
                <br><p style="font-size: 10px; color: #888;">DOCUMENT ID: TS-EXEC-{int(time.time())}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # INDUSTRIAL-STRENGTH WORD EXPORT (HTML with Table and Borders)
        word_html = f"""
        <html>
        <head>
        <meta charset='utf-8'>
        <style>
            body {{ font-family: 'Times New Roman', Times, serif; padding: 1in; background-color: white; color: black; }}
            .border-box {{ border: 3px double #000; padding: 0.5in; min-height: 9.5in; }}
            .header-table {{ width: 100%; border-bottom: 2px solid #000; margin-bottom: 20px; }}
            .content {{ line-height: 1.5; font-size: 12pt; }}
            .subject {{ text-align: center; text-decoration: underline; font-weight: bold; margin: 20px 0; }}
            .sig-line {{ border-top: 1px solid #000; width: 250px; margin-top: 40px; }}
        </style>
        </head>
        <body>
            <div class="border-box">
                <table class="header-table">
                    <tr>
                        <td align="left" valign="top"><b>FROM:</b><br>{v['cl']}<br>{v['cla'].replace('\n','<br>')}</td>
                        <td align="right" valign="top"><b>DATE:</b><br>{date_now}</td>
                    </tr>
                </table>
                <div class="content">
                    <b>TO:</b><br>{v['res']}<br>{v['resa'].replace('\n','<br>')}
                    <div class="subject">FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE</div>
                    <b>RE: {p1}</b><br><br>
                    <p>{p2}</p>
                    <p><b>{p3.replace('\n','<br>')}</b></p>
                    <p>{p4.replace('\n','<br>')}</p>
                    <p style="background-color:#eee; padding:10px;">{p5}</p>
                    <p>{p6}</p>
                    <br><br>
                    <p>Sincerely,</p>
                    <div class="sig-line"></div>
                    <b>{v['cl']}</b><br>Claimant
                </div>
            </div>
        </body>
        </html>
        """
        
        full_raw_text = f"FROM: {v['cl']}\nDATE: {date_now}\nTO: {v['res']}\n\nRE: {p1}\n\n{p2}\n\n{p3}\n\n{p4}\n\n{p5}\n\n{p6}\n\nSincerely,\n{v['cl']}"
        
        st.download_button("📥 DOWNLOAD OFFICIAL WORD DOC (.DOC)", word_html, file_name="JusticeBot_Official_Demand.doc", key="dl_word_v38")
        st.download_button("📥 DOWNLOAD PLAIN TEXT (.TXT)", full_raw_text, file_name="JusticeBot_Formal_Demand.txt", key="dl_txt_v38")
        
        if st.button("INITIATE NEW CASE", key="new_v38"):
            st.session_state.paid = False; st.session_state.ready = False; st.session_state.vault = {}; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.38 | Trend Shadows Digital Agency")
