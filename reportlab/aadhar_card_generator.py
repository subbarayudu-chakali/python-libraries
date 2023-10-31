from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_aadhar_card(file_path, name, dob, gender, address, aadhar_number, mobile_number, photo_path) :
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # # Add a logo
    # logo = Image("logo.png")
    # logo.drawHeight = 0.5 * inch
    # logo.drawWidth = 0.5 * inch
    # logo.hAlign = "LEFT"
    # logo.vAlign = "TOP"

    # Add the name
    name_paragraph = Paragraph(name, styles["Normal"])

    # Add the DOB
    dob_paragraph = Paragraph(dob, styles["Normal"])

    # Add the gender
    gender_paragraph = Paragraph(gender, styles["Normal"])

    # Add the address
    address_paragraph = Paragraph(address, styles["Normal"])

    # Add the Aadhar number
    aadhar_number_paragraph = Paragraph(aadhar_number, styles["Normal"])

    # Add the mobile number
    mobile_number_paragraph = Paragraph(mobile_number, styles["Normal"])
    # Add the photo
    photo = Image(photo_path)
    photo.drawHeight = 1.5 * inch
    photo.drawWidth = 1.5 * inch
    photo.hAlign = "CENTER"
    photo.vAlign = "TOP"

    # Add the content
    content = [name_paragraph, dob_paragraph, gender_paragraph, address_paragraph, aadhar_number_paragraph, mobile_number_paragraph, photo]
    doc.build(content)
generate_aadhar_card("aadhar_card.pdf", "John Doe", "01/01/2000", "Male", "123 Main St", "8479", "1234567890", "company-name.png")