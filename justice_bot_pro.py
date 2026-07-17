from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import io
import os
from datetime import datetime

# --- THE ELITE GENERATION ENGINE (v1.43) ---
def generate_pro_docx(v, title, body, date_str):
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
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False
    table.columns[0].width = Inches(3.25)
    table.columns[1].width = Inches(3.25)
    
    c1 = table.cell(0, 0)
    cp1 = c1.paragraphs[0]
    cp1.add_run("FROM (CLAIMANT/SELLER):").bold = True
    cp1.add_run(f"\n{v.get('cl', '')}")
    if v.get('cl_id'): cp1.add_run(f"\nID: {v['cl_id']}")
    cp1.add_run(f"\n{v.get('cla', '')}")
    
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
            run = p.add_run(line)
            run.bold = True
            run.underline = True
        else:
            p.add_run(line)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
    doc.add_paragraph("\n\n")
    
    # 6. SIGNATURE BLOCK
    sig_table = doc.add_table(rows=2, cols=2)
    sig_table.columns[0].width = Inches(3.25)
    sig_table.columns[1].width = Inches(3.25)
    
    s1 = sig_table.cell(0, 0)
    s1.paragraphs[0].add_run("__________________________\nFOR THE SELLER / CLAIMANT")
    s1.add_paragraph(f"Name: {v.get('cl', '')}")
    
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
    
    return doc

# --- TEST SETUP ---
date_now = datetime.now().strftime("%B %d, %Y")

# CASE 1: VEHICLE SALE (ZA)
v1 = {
    "cl": "Daniel De Bod", "cl_id": "7110255180085", "cla": "123 Silver Industrial Way, Cape Town",
    "res": "John Peterson", "res_id": "8506125000081", "resa": "456 Executive Plaza, Johannesburg",
    "amt": "125,000.00", "det": "Private sale of a 2018 Volkswagen Golf. The vehicle is sold 'voetstoots' (as-is condition). Both parties have inspected the vehicle. Full payment is due via EFT before ownership transfer.",
    "jur": "South Africa (ZA)", "cat": "Private Vehicle Sale", "ref": "VIN: VIN-VW88912 | REG: CEA5533", "cur": "R"
}
title1 = "PRIVATE SALE & PURCHASE AGREEMENT"
body1 = f"This Agreement is made on {date_now} between {v1['cl']} (ID: {v1['cl_id']}) (Seller) and {v1['res']} (ID: {v1['res_id']}) (Buyer).\n\nASSET DESCRIPTION:\n{v1['cat']} - {v1['ref']}\n\nNARRATIVE & CONDITION:\n{v1['det']}\n\nPURCHASE PRICE:\nThe agreed sale price is {v1['cur']}{v1['amt']}, payable in full before the transfer of ownership.\n\nLEGAL TERMS:\nThis sale is conducted under the Common Law of Sale and Voetstoots Protocol. The asset is sold in its current condition (As-Is/Voetstoots), and the Seller provides no warranties. The Buyer acknowledges they have inspected the asset and accept it in its current state."

# CASE 2: LETTER OF DEMAND (UK)
v2 = {
    "cl": "Trend Shadows Agency", "cl_id": "REG-2024-TS", "cla": "Industrial Hub, Suite 10, London",
    "res": "Global Logistics Ltd", "res_id": "CORP-9988-UK", "resa": "789 Stalled Street, Manchester",
    "amt": "5,000.00", "det": "Non-payment for digital agency services delivered between June 1st and June 30th 2026. Despite three reminders, the balance remains outstanding.",
    "jur": "United Kingdom (UK)", "cat": "Unpaid Freelance Invoice", "ref": "INV-SHADOW-001", "cur": "£"
}
title2 = "FORMAL LETTER OF DEMAND - PRE-LITIGATION NOTICE"
body2 = f"TO: {v2['res']} (ID: {v2['res_id']})\n\nNotice is hereby given that your failure to remit the balance of {v2['cur']}{v2['amt']} regarding the {v2['cat'].lower()} constitutes a direct violation of the Late Payment of Commercial Debts Act 1998.\n\nUnder the laws of {v2['jur']}, the withholding of these funds is a breach of legal obligations.\n\nSTATEMENT OF FACTS:\n{v2['det']}\n\nLEGAL DEMAND:\nDemand is hereby made for the immediate payment of the full balance. This must be received in full within 14 calendar days of the date of this notice.\n\nINTENT TO LITIGATE:\nFailure to comply with this final demand will result in the immediate commencement of legal proceedings in Small Claims Court without further notice."

# EXECUTE
doc1 = generate_pro_docx(v1, title1, body1, date_now)
doc1.save("TEST_CASE_1_SALE_AGREEMENT.docx")

doc2 = generate_pro_docx(v2, title2, body2, date_now)
doc2.save("TEST_CASE_2_DEMAND_LETTER.docx")

print("SUCCESS: Both Elite documents generated.")
