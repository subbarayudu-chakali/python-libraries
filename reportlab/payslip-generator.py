from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_payslip(file_path):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # Fake employee details
    name = "subbu"
    id = "E895202"
    job_title = "Software Developer"
    department = "IT"
    location = "Chennai"
    joining_date = "2023-01-01"
    bank_account_number = "198480223381"
    bank_name = "Bank of India"
    pan_number = "XYCDE1234F"
    uan_number = "12345678129"
    pf_number = "PF123456789"
    available_calendar_days = "30"
    paid_days = "30"
    leave_days = "0"

    # Company details
    company_name = "AI Insurance India Private Limited"
    payslip_month = "Payslip for the month of October 2023"
    financial_period = "Financial Period: 2023 - 2024"

    # Earnings
    basic_salary = 50000
    house_rent_allowance = 10000
    medical_allowance = 5000
    special_allowance = 10000
    bonus = 15000
    total_earnings = basic_salary + house_rent_allowance + medical_allowance + special_allowance + bonus

    # Deductions
    pf_contribution = 5000
    tds = 2000
    total_deductions = pf_contribution + tds

    # Net salary
    net_salary = total_earnings - total_deductions

    # Content for the PDF
    content = []
    custom_style = ParagraphStyle('BoldStyle', fontSize=14, leading=25, alignment=1, textColor='black', fontName="Helvetica-Bold")

    # Company name
    company_info = f"{company_name}"
    centered_header = Paragraph(company_info, custom_style)


    # Company logo
    logo_path = 'company-logo.png'
    logo_width = 2 * inch
    logo_height = 1 * inch
    logo = Image('company-name.png', logo_width,  logo_height)

    content = [logo, centered_header, Paragraph(f"{payslip_month}", ParagraphStyle('BoldStyle', alignment=1, textColor='black', fontSize=9, fontName='Helvetica-Bold')), Spacer(1, 5), Paragraph(f"{financial_period}", ParagraphStyle('BoldStyle', alignment=1, textColor='black', fontSize=9, fontName='Helvetica-Bold'))]

    # Payslip month

    # Header
    # payslip_info = f"Payslip for {employee_name} - {employee_id}"
    # content.append(Paragraph(payslip_info, styles['Normal']))

    table_style=(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                 ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                 ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                 ('FONTSIZE', (0, 0), (-1, 0), 12),
                 ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                 ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                 ('GRID', (0, 1), (-1, -1), 1, colors.grey), ]))

    # Employee details
    employee_info = [
        ["Employee Details"],
        ["Employee Name", name],
        ["Employee ID", id],
        ["Job Title", job_title],
        ["Department", department],
        ["Location", location],
        ["Joining Date", joining_date],
        ["Bank Account Number", bank_account_number],
        ["Bank Name", bank_name],
        ["PAN Number", pan_number],
        ["UAN Number", uan_number],
        ["PF Number", pf_number],
        ["Available Calendar Days", available_calendar_days],
        ["Paid Days", paid_days],
        ["Leave Days", leave_days]
    ]
    employee_table = Table(employee_info, colWidths=[150, 75])
    employee_table.setStyle(table_style)
    content.append(employee_table)

    # content.append(Paragraph(employee_info, styles['Normal']))
    # content.append(Spacer(1, 12))

    # Earnings table
    earnings_data = [
        ["Earnings", "Amount"],
        ["Basic Salary", basic_salary],
        ["House Rent Allowance", house_rent_allowance],
        ["Medical Allowance", medical_allowance],
        ["Special Allowance", special_allowance],
        ["Bonus", bonus],
        ["Total Earnings (A)", total_earnings],
    ]

    earnings_table = Table(earnings_data, colWidths=[150, 75])
    # Apply styles to the table
    earnings_table.setStyle(table_style)
    # content.append(earnings_table)
    # content.append(Spacer(1, 12))

    # Deductions table
    deductions_data = [
        ["Deductions", "Amount"],
        ["PF Contribution", pf_contribution],
        ["TDS", tds],
        ["Total Deductions (B)", total_deductions],
    ]

    deductions_table = Table(deductions_data, colWidths=[150, 75])
    # Apply styles to the table
    deductions_table.setStyle(table_style)
    # content.append(deductions_table)
    # content.append(Spacer(1, 12))

    # Earnings table
    total_earnings_data = [
        ["Earnings", "Amount", 'Deductions', 'Amount'],
        ["Basic Salary", basic_salary, "PF Contribution", pf_contribution],
        ["House Rent Allowance", house_rent_allowance, "TDS", tds],
        ["Medical Allowance", medical_allowance, ],
        ["Special Allowance", special_allowance],
        ["Bonus", bonus],
        ["Total Earnings (A)", total_earnings, "Total Deductions (B)", total_deductions],
    ]
    total_earnings_data_table = Table(total_earnings_data, colWidths=[150, 75, 150, 75])
    total_earnings_data_table.setStyle(table_style)
    # combined_table_data = [[earnings_table,deductions_table]]
    # combined_table = Table(combined_table_data)
    # content.append(combined_table)
    #total_earnings_data_table = Table(total_earnings_data, colWidths=[150, 75, 150, 75])
    content.append(total_earnings_data_table)
    # Net salary
    net_salary_text = f"<b>Net Salary (A-B):</b>" + str(net_salary)
    content.append(Paragraph(net_salary_text, styles['Normal']))
    doc.build(content)

# Replace 'payslip.pdf' with the desired PDF file name
generate_payslip('payslip1.pdf')