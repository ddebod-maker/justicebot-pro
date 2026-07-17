import streamlit as st
import time
from datetime import datetime
try:
    from docx import Document
    from docx.shared import Pt, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    DOCX_SUPPORT = True
except ImportError:
    DOCX_SUPPORT = False

import io

# ============================================================
# PROJECT: JUSTICE BOT AI (Global Executive v1.42.1)
# PRODUCED BY: Trend Shadows Digital Agency
# STATUS: DUAL-MODE ENGINE | GLOBAL RESTORED | UI REPAIRED
# FIXED: 7 Countries & 10 Domains restored.
# FIXED: Separate logic for "Sale Agreements" vs "Demand Letters".
# FIXED: Context-aware fields (VIN/Reg for Vehicles).
# FIXED: Voucher box restored to main screen.
# FIXED: Raw HTML tags appearing in preview.
# FIXED: Added ID Numbers for Parties.
# FIXED: Professional Word (.docx) formatting with Elite styling.
# FIXED: ImportError Fallback for Streamlit Cloud (python-docx).
# ============================================================

st.set_page_config(page_title="JusticeBot Pro | Global Elite", layout="wide")

# --- VERSION STAMP ---
st.sidebar.markdown("### 🛠️ System Control")
st.sidebar.markdown("`VERSION: v1.43` (ELITE)")
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
    .legal-paper p, .legal-paper div, .legal-paper b, .legal-paper span { 
        color: #000000 !important; 
        font-family: 'Times New Roman', serif !important; 
    }
    .sig-line { margin-top: 60px; border-top: 2px solid #000; width: 300px; padding-top: 10px; }
    .doc-header { display: flex; justify-content: space-between; border-bottom: 2px solid #000; padding-bottom: 20px; margin-bottom: 30px; }

    .ts-logo { font-size: 32px; font-weight: 900; letter-spacing: 10px; color: #FFFFFF; text-align: right; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- THE 10-DOMAIN GLOBAL ENGINE (7 COUNTRIES RESTORED) ---
STATUTES = {
    "United States (US)": {
        "Security Deposit Recovery": {"type": "DEMAND", "law": "Civil Code Section 1950.5 and the URLTA"},
        "Unpaid Freelance Invoice": {"type": "DEMAND", "law": "UCC Article 2 and state Prompt Payment Acts"},
        "Private Vehicle Sale": {"type": "CONTRACT", "law": "State Bill of Sale & UCC Article 2"},
        "Electronics/Goods Sale": {"type": "CONTRACT", "law": "Magnuson-Moss Warranty Act and UCC"},
        "Travel/Flight Refund": {"type": "DEMAND", "law": "14 CFR Part 259 and DOT mandates"},
        "Service Cancellation": {"type": "DEMAND", "law": "State Consumer Statutes & FTC Cooling-Off Rule"},
        "Employment/Unpaid Wages": {"type": "DEMAND", "law": "Fair Labor Standards Act (FLSA)"},
        "Insurance Claim Dispute": {"type": "DEMAND", "law": "State Insurance Fair Conduct Acts"},
        "Property Damage Claim": {"type": "DEMAND", "law": "General Tort Law & Civil Liability Codes"},
        "General Cease & Desist": {"type": "DEMAND", "law": "Common Law Defamation Statutes"}
    },
    "United Kingdom (UK)": {
        "Security Deposit Recovery": {"type": "DEMAND", "law": "Housing Act 2004 and Landlord and Tenant Act 1985"},
        "Unpaid Freelance Invoice": {"type": "DEMAND", "law": "Late Payment of Commercial Debts Act 1998"},
        "Private Vehicle Sale": {"type": "CONTRACT", "law": "Sale of Goods Act 1979 & Common Law"},
        "Electronics/Goods Sale": {"type": "CONTRACT", "law": "Sale of Goods Act 1979"},
        "Travel/Flight Refund": {"type": "DEMAND", "law": "UK261 Flight Compensation Regulations"},
        "Service Cancellation": {"type": "DEMAND", "law": "Consumer Rights Act 2015"},
        "Employment/Unpaid Wages": {"type": "DEMAND", "law": "Employment Rights Act 1996"},
        "Insurance Claim Dispute": {"type": "DEMAND", "law": "FOS Guidelines"},
        "Property Damage Claim": {"type": "DEMAND", "law": "Occupiers' Liability Act 1957"},
        "General Cease & Desist": {"type": "DEMAND", "law": "Protection from Harassment Act 1997"}
    },
    "South Africa (ZA)": {
        "Security Deposit Recovery": {"type": "DEMAND", "law": "Rental Housing Act 50 of 1999"},
        "Unpaid Freelance Invoice": {"type": "DEMAND", "law": "Section 11 of the Prescription Act"},
        "Private Vehicle Sale": {"type": "CONTRACT", "law": "Common Law of Sale and Voetstoots Protocol"},
        "Electronics/Goods Sale": {"type": "CONTRACT", "law": "Consumer Protection Act 68 of 2008"},
        "Travel/Flight Refund": {"type": "DEMAND", "law": "CPA Section 47 and IATA Conventions"},
        "Service Cancellation": {"type": "DEMAND", "law": "CPA Section 14"},
        "Employment/Unpaid Wages": {"type": "DEMAND", "law": "Basic Conditions of Employment Act"},
        "Insurance Claim Dispute": {"type": "DEMAND", "law": "Short-Term Insurance Act"},
        "Property Damage Claim": {"type": "DEMAND", "law": "Apportionment of Damages Act"},
        "General Cease & Desist": {"type": "DEMAND", "law": "Protection from Harassment Act 2011"}
    },
    "Australia (AU)": {
        "Security Deposit Recovery": {"type": "DEMAND", "law": "Residential Tenancies Act 2010"},
        "Unpaid Freelance Invoice": {"type": "DEMAND", "law": "Australian Consumer Law (ACL)"},
        "Private Vehicle Sale": {"type": "CONTRACT", "law": "State Motor Vehicle Traders Act"},
        "Electronics/Goods Sale": {"type": "CONTRACT", "law": "ACL Consumer Guarantees"},
        "Travel/Flight Refund": {"type": "DEMAND", "law": "ACL Major Failure Protocols"},
        "Service Cancellation": {"type": "DEMAND", "law": "ACL Unfair Contract Terms"},
        "Employment/Unpaid Wages": {"type": "DEMAND", "law": "Fair Work Act 2009"},
        "Insurance Claim Dispute": {"type": "DEMAND", "law": "Insurance Contracts Act 1984"},
        "Property Damage Claim": {"type": "DEMAND", "law": "Civil Liability Act 2002"},
        "General Cease & Desist": {"type": "DEMAND", "law": "Personal Violence Protection Act"}
    },
    "Canada (CA)": {
        "Security Deposit Recovery": {"type": "DEMAND", "law": "Provincial Residential Tenancy Acts"},
        "Unpaid Freelance Invoice": {"type": "DEMAND", "law": "Provincial Sale of Goods Acts"},
        "Private Vehicle Sale": {"type": "CONTRACT", "law": "Provincial Consumer Protection Statutes"},
        "Electronics/Goods Sale": {"type": "CONTRACT", "law": "CPA Section 14"},
        "Travel/Flight Refund": {"type": "DEMAND", "law": "Air Passenger Protection Regulations (APPR)"},
        "Service Cancellation": {"type": "DEMAND", "law": "CPA Cancellation Protocols"},
        "Employment/Unpaid Wages": {"type": "DEMAND", "law": "Canada Labour Code"},
        "Insurance Claim Dispute": {"type": "DEMAND", "law": "Provincial Insurance Acts"},
        "Property Damage Claim": {"type": "DEMAND", "law": "Negligence Act"},
        "General Cease & Desist": {"type": "DEMAND", "law": "Libel and Slander Act"}
    },
    "New Zealand (NZ)": {
        "Security Deposit Recovery": {"type": "DEMAND", "law": "Residential Tenancies Act 1986"},
        "Unpaid Freelance Invoice": {"type": "DEMAND", "law": "Consumer Guarantees Act 1993"},
        "Private Vehicle Sale": {"type": "CONTRACT", "law": "Fair Trading Act 1986"},
        "Electronics/Goods Sale": {"type": "CONTRACT", "law": "CGA Section 6"},
        "Travel/Flight Refund": {"type": "DEMAND", "law": "Contract and Commercial Law Act 2017"},
        "Service Cancellation": {"type": "DEMAND", "law": "CGA Reasonable Care"},
        "Employment/Unpaid Wages": {"type": "DEMAND", "law": "Employment Relations Act 2000"},
        "Insurance Claim Dispute": {"type": "DEMAND", "law": "Insurance Law Reform Act"},
        "Property Damage Claim": {"type": "DEMAND", "law": "Limitation Act 2010"},
        "General Cease & Desist": {"type": "DEMAND", "law": "Harassment Act 1997"}
    },
    "India (IN)": {
        "Security Deposit Recovery": {"type": "DEMAND", "law": "Model Tenancy Act 2021"},
        "Unpaid Freelance Invoice": {"type": "DEMAND", "law": "Indian Contract Act 1872"},
        "Private Vehicle Sale": {"type": "CONTRACT", "law": "Motor Vehicles Act 1988"},
        "Electronics/Goods Sale": {"type": "CONTRACT", "law": "Consumer Protection Act 2019"},
        "Travel/Flight Refund": {"type": "DEMAND", "law": "DGCA Passenger Charter"},
        "Service Cancellation": {"type": "DEMAND", "law": "CPA Unfair Contracts"},
        "Employment/Unpaid Wages": {"type": "DEMAND", "law": "Payment of Wages Act 1936"},
        "Insurance Claim Dispute": {"type": "DEMAND", "law": "IRDAI Guidelines"},
        "Property Damage Claim": {"type": "DEMAND", "law": "Tort of Negligence"},
        "General Cease & Desist": {"type": "DEMAND", "law": "IT Act 2000"}
    }
}

CURRENCIES = ["USD ($)", "GBP (£)", "ZAR (R)", "AUD ($)", "NZD ($)", "CAD ($)", "INR (₹)"]

# --- PERSISTENT STORAGE VAULT ---
if 'paid_v42' not in st.session_state: st.session_state.paid_v42 = False
if 'ready_v42' not in st.session_state: st.session_state.ready_v42 = False
if 'vault_v42' not in st.session_state: st.session_state.vault_v42 = {}

st.markdown('<div class="ts-logo">TS</div>', unsafe_allow_html=True)
st.title("JusticeBot Pro Global")
st.markdown("<p style='text-align:center; color:#888; letter-spacing:5px;'>CERTIFIED LEGAL RECOVERY TERMINAL</p>", unsafe_allow_html=True)
st.divider()

if not st.session_state.paid_v42:
    with st.container():
        st.markdown("### 🏛️ Case Intelligence Architecture")
        c1, c2 = st.columns(2)
        with c1:
            cl_name = st.text_input("Claimant Full Name (You)", key="cl_in")
            cl_id = st.text_input("Claimant ID Number / Passport", key="cl_id_in")
            cl_addr = st.text_area("Claimant Physical Address", height=80, key="cla_in")
            juris = st.selectbox("Select Jurisdiction", list(STATUTES.keys()), key="ju_in")
        with c2:
            res_name = st.text_input("Respondent Name (Target)", key="re_in")
            res_id = st.text_input("Respondent ID Number (If known)", key="res_id_in")
            res_addr = st.text_area("Respondent Physical Address", height=80, key="resa_in")
            curr = st.selectbox("Select Currency", CURRENCIES, key="cu_in")
            
        st.divider()
        category = st.selectbox("Select Case Category", list(STATUTES[juris].keys()), key="ca_in")
        
        # DYNAMIC FIELD LOGIC (VIN/Reg for Vehicles)
        is_vehicle = "Vehicle" in category
        if is_vehicle:
            c3, c4 = st.columns(2)
            with c3: ref_no = st.text_input("Vehicle VIN / Serial Number", key="vin_in")
            with c4: reg_no = st.text_input("Vehicle Registration / Plate", key="reg_in")
            ref_combined = f"VIN: {ref_no} | REG: {reg_no}"
        else:
            ref_combined = st.text_input("Reference / Invoice / Lease Number", key="ref_in")
            
        amount = st.text_input(f"Total Amount Owed / Sale Price ({curr.split(' ')[1]})", key="am_in")
        details = st.text_area("Narrative (Be thorough with dates and facts)", height=150, key="de_in")
        
        if st.button("PROCESS OFFICIAL DOCUMENT", key="main_btn"):
            if cl_name and res_name and details and amount:
                st.session_state.vault_v42 = {
                    "cl": cl_name, "cl_id": cl_id, "cla": cl_addr, 
                    "res": res_name, "res_id": res_id, "resa": res_addr,
                    "amt": amount, "det": details, "jur": juris, "cat": category,
                    "ref": ref_combined, "cur": curr.split(' ')[1]
                }
                st.session_state.ready_v42 = True
                st.success("Analysis Complete. Draft Generated.")

    if st.session_state.get("ready_v42"):
        st.divider()
        v = st.session_state.vault_v42
        mode_type = STATUTES[v['jur']][v['cat']]['type']
        subject_header = "NOTICE OF INTENT TO LITIGATE" if mode_type == "DEMAND" else "SALE & PURCHASE AGREEMENT"
        
        st.markdown(f"**SUBJECT: {subject_header} - {v['cat'].upper()}**")
        st.markdown("""<div style="filter:blur(12px); background:#111; padding:20px; border:1px dashed #C0C0C0;">Notice is hereby given that your actions constitute a direct violation... [ENCRYPTED]</div>""", unsafe_allow_html=True)
        
        st.markdown("### 💎 Unlock Document Package")
        v_code = st.text_input("Enter Voucher Code (Admin Only)", type="password", key="vouch_in")
        
        col_v, col_p = st.columns(2)
        with col_v:
            if st.button("AUTHENTICATE VOUCHER", key="auth_btn"):
                if v_code == "TS-GIFT-2026":
                    st.session_state.paid_v42 = True
                    st.rerun()
                else: st.error("Invalid Code")
        with col_p:
            st.link_button("💎 PAY TO UNLOCK ($19.00)", "https://trend-shadows.lemonsqueezy.com/buy/1914602")

else:
    # --- PRODUCTION OUTPUT ---
    v = st.session_state.vault_v42
    st.success("✅ DOCUMENT UNLOCKED.")
    config = STATUTES[v['jur']].get(v['cat'])
    law = config['law']
    doc_mode = config['type']
    date_now = datetime.now().strftime("%B %d, %Y")
    
    if doc_mode == "DEMAND":
        doc_title = "FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE"
        res_id_str = f" (ID: {v.get('res_id', '')})" if v.get('res_id') else ""
        content_body = f"TO: {v['res']}{res_id_str}\n\nNotice is hereby given that your failure to remit the balance of {v['cur']}{v['amt']} regarding the {v['cat'].lower()} constitutes a direct violation of {law}.\n\nUnder the laws of {v['jur']}, the withholding of these funds is a breach of legal obligations.\n\nSTATEMENT OF FACTS:\n{v['det']}\n\nLEGAL DEMAND:\nDemand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days of the date of this notice.\n\nINTENT TO LITIGATE:\nFailure to comply with this final demand will result in the immediate commencement of legal proceedings in Small Claims Court without further notice."
    else:
        doc_title = "PRIVATE SALE & PURCHASE AGREEMENT"
        cl_id_str = f" (ID: {v.get('cl_id', '')})" if v.get('cl_id') else ""
        res_id_str = f" (ID: {v.get('res_id', '')})" if v.get('res_id') else ""
        content_body = f"This Agreement is made on {date_now} between {v['cl']}{cl_id_str} (Seller) and {v['res']}{res_id_str} (Buyer).\n\nASSET DESCRIPTION:\n{v['cat']} - {v['ref']}\n\nNARRATIVE & CONDITION:\n{v['det']}\n\nPURCHASE PRICE:\nThe agreed sale price is {v['cur']}{v['amt']}, payable in full before the transfer of ownership.\n\nLEGAL TERMS:\nThis sale is conducted under the {law}. The asset is sold in its current condition (As-Is/Voetstoots), and the Seller provides no warranties. The Buyer acknowledges they have inspected the asset and accept it in its current state."

    # --- DOCX GENERATION ENGINE ---
    def generate_pro_docx(v, title, body, date_str):
        if not DOCX_SUPPORT:
            return None
        doc = Document()
        
        # Global Style
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(11)
        
        # 1. BRANDING HEADER (Top Right)
        section = doc.sections[0]
        header = section.header
        htable = header.add_table(1, 2, width=Inches(6.5))
        htable.columns[0].width = Inches(4.5)
        htable.columns[1].width = Inches(2.0)
        
        # Left side of header (Empty or Address)
        # Right side: Logo
        h_cell = htable.cell(0, 1)
        hp = h_cell.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr = hp.add_run("TREND SHADOWS")
        hr.bold = True
        hr.font.size = Pt(10)
        hr.font.name = 'Arial'
        
        hp2 = h_cell.add_paragraph()
        hp2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr2 = hp2.add_run("JUSTICE BOT PRO")
        hr2.font.size = Pt(8)
        hr2.font.name = 'Arial'
        hr2.italic = True

        # 2. PARTY INFORMATION BLOCK
        # Use a table for clean alignment
        table = doc.add_table(rows=1, cols=2)
        table.autofit = False
        table.columns[0].width = Inches(3.25)
        table.columns[1].width = Inches(3.25)
        
        # FROM Cell
        c1 = table.cell(0, 0)
        cp1 = c1.paragraphs[0]
        cp1.add_run("FROM (CLAIMANT/SELLER):").bold = True
        cp1.add_run(f"\n{v.get('cl', '')}")
        if v.get('cl_id'): cp1.add_run(f"\nID: {v['cl_id']}")
        cp1.add_run(f"\n{v.get('cla', '')}")
        
        # TO Cell
        c2 = table.cell(0, 1)
        cp2 = c2.paragraphs[0]
        cp2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        cp2.add_run("TO (RESPONDENT/BUYER):").bold = True
        cp2.add_run(f"\n{v.get('res', '')}")
        if v.get('res_id'): cp2.add_run(f"\nID: {v['res_id']}")
        cp2.add_run(f"\n{v.get('resa', '')}")

        doc.add_paragraph("\n")
        
        # 3. DATE & REFERENCE
        dr = doc.add_paragraph()
        dr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        dr.add_run(f"DATE: {date_str}").bold = True
        
        doc.add_paragraph("\n")
        
        # 4. MAIN TITLE
        t = doc.add_paragraph()
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        tr = t.add_run(title)
        tr.bold = True
        tr.font.size = Pt(16)
        tr.font.name = 'Arial'
        
        # Decorative Line
        p_line = doc.add_paragraph()
        p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_line.add_run("_______________________________________________________")

        doc.add_paragraph("\n")
        
        # 5. CONTENT BODY
        for line in body.split('\n'):
            line = line.strip()
            if not line:
                doc.add_paragraph("")
                continue
            
            p = doc.add_paragraph()
            if ":" in line and len(line) < 45 and (line.isupper() or line.endswith(':')):
                # Section Heading
                run = p.add_run(line)
                run.bold = True
                run.underline = True
            else:
                # Standard Paragraph
                p.add_run(line)
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            
        doc.add_paragraph("\n\n")
        
        # 6. SIGNATURE BLOCK (Side-by-Side)
        sig_table = doc.add_table(rows=2, cols=2)
        sig_table.columns[0].width = Inches(3.25)
        sig_table.columns[1].width = Inches(3.25)
        
        # Seller Sig
        s1 = sig_table.cell(0, 0)
        s1.paragraphs[0].add_run("__________________________\nFOR THE SELLER / CLAIMANT")
        s1.add_paragraph(f"Name: {v.get('cl', '')}")
        
        # Buyer Sig
        s2 = sig_table.cell(0, 1)
        s2.paragraphs[0].add_run("__________________________\nFOR THE BUYER / RESPONDENT")
        s2.add_paragraph(f"Name: {v.get('res', '')}")
        
        # 7. FOOTER
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.text = "This document is a legally binding instrument generated via Trend Shadows JusticeBot Pro Global. (c) 2026."
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.style.font.size = Pt(8)
        fp.style.font.italic = True
        
        target = io.BytesIO()
        doc.save(target)
        return target.getvalue()

    # Stationer Rendering
    st.markdown(f"""
        <div class="legal-paper">
            <div class="doc-header">
                <div><b>FROM:</b><br>{v['cl']}{'<br>ID: '+v.get('cl_id','') if v.get('cl_id') else ''}<br>{v['cla'].replace('\n','<br>')}</div>
                <div style="text-align:right;"><b>DATE:</b><br>{date_now}</div>
            </div>
            <div><b>TO:</b><br>{v['res']}{'<br>ID: '+v.get('res_id','') if v.get('res_id') else ''}<br>{v['resa'].replace('\n','<br>')}</div>
            <br><br>
            <div style="text-align:center; text-decoration:underline; font-size: 22px;"><b>{doc_title}</b></div>
            <br>
            <p style="white-space: pre-wrap;">{content_body}</p>
            <br><p>Sincerely,</p>
            <div class="sig-line"></div>
            <p><b>{v['cl']}</b><br>Authorized Signature</p>
        </div>
    """, unsafe_allow_html=True)
    
    docx_bytes = generate_pro_docx(v, doc_title, content_body, date_now)
    
    if DOCX_SUPPORT and docx_bytes:
        st.download_button("📥 DOWNLOAD OFFICIAL WORD DOCUMENT (.DOCX)", docx_bytes, file_name=f"JusticeBot_{v['cat'].replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key="final_dl")
    else:
        st.warning("🚨 ATTENTION: Professional Word Engine is installing on server. This takes 60 seconds on first run. Please refresh in a moment for the ELITE format.")
        st.download_button("📥 DOWNLOAD TEMPORARY DOCUMENT (NOTEPAD)", content_body, file_name=f"JusticeBot_{v['cat'].replace(' ', '_')}.txt", key="final_dl_fallback")
    if st.button("INITIATE NEW CASE"):
        st.session_state.paid_v42 = False; st.session_state.ready_v42 = False; st.session_state.vault_v42 = {}; st.rerun()

st.divider()
st.caption("Shadow-Build Global Engine v1.42 | Trend Shadows Digital Agency")
