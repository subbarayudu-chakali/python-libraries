from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import black, red, blue, green, yellow
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart

# create a simple pdf with headline as Driving License
c = canvas.Canvas("driving-license.pdf", pagesize=letter)
c.setLineWidth(.3)
c.setFont('Helvetica', 22)
c.drawString(inch, inch, "Driving License")
c.showPage()
c.save()


def generate_payslip(employee_name, employee_id, salary, deductions, net_pay, pdf_path):
    # create a pdf document
    pdf = canvas.Canvas(pdf_path, pagesize=letter)

    # set font
    pdf.setFont("Helvetica", 12)

    # add content to the pdf document
    pdf.drawString(100, 730, f"Employee Name: {employee_name}")
    pdf.drawString(100, 710, f"Employee ID: {employee_id}")
    pdf.drawString(100, 680, "Salary: ${:,.2f}".format(salary))
    pdf.drawString(100, 660, "Deductions: ${:,.2f}".format(deductions))
    pdf.drawString(100, 630, "Net Pay: ${:,.2f}".format(net_pay))

    # save the pdf
    pdf.save()

# Example usage:
employee_name = "subbarayudu chakali"
employee_id = "EMP895202"
salary = 50000.00
deductions = 5000.00
net_pay = salary - deductions
pdf_path = "payslip_October.pdf"

generate_payslip(employee_name, employee_id, salary, deductions, net_pay, pdf_path)
