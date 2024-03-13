from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_audit_report(file_path, audit_details):
    c = canvas.Canvas(file_path, pagesize=letter)

    # Set font style
    c.setFont("Helvetica", 12)

    # Define page size
    width, height = letter

    # Define margin
    margin = 50

    # Define line height
    line_height = 14

    # Define header
    header_text = "Audit Report"
    header_font_size = 16
    header_x = width / 2 - c.stringWidth(header_text, "Helvetica-Bold", header_font_size) / 2
    header_y = height - margin / 2

    # Define title
    title_text = "Detailed Audit Information"
    title_font_size = 14
    title_x = width / 2 - c.stringWidth(title_text, "Helvetica-Bold", title_font_size) / 2
    title_y = header_y - margin

    # Define footer
    footer_text = "This report was generated on 11/30/2023"
    footer_font_size = 10
    footer_x = width - margin
    footer_y = margin / 2

    # Draw page border
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

    # Draw header
    c.setFont("Helvetica-Bold", header_font_size)
    c.drawCentredString(header_x, header_y, header_text)

    # Draw title
    c.setFont("Helvetica-Bold", title_font_size)
    c.drawCentredString(title_x, title_y, title_text)

    # Initialize y-coordinate
    y = title_y - margin / 2

    # Iterate over audit details
    for detail_name, detail_value in audit_details.items():
        # Check if the detail name is in bold
        if detail_name.startswith("**") and detail_name.endswith("**"):
            # Remove bold markers and set font to bold
            detail_name = detail_name[2:-2]
            c.setFont("Helvetica-Bold", 12)
        else:
            # Set font back to regular
            c.setFont("Helvetica", 12)

        # Write detail to PDF
        c.drawString(margin, y, f"{detail_name}: {detail_value}")

        # Update y-coordinate
        y -= line_height

        # Check if y-coordinate goes beyond the page, start a new page
        if y < margin:
            c.setFont("Helvetica", footer_font_size)
            c.drawRightString(footer_x, footer_y, footer_text)
            c.showPage()
            y = height - margin

    # Save the PDF
    c.save()


# Example audit details
audit_details = {
    "**Audit ID**": "12345",
    "**Audit Date**": "2023-11-30",
    "**Audit Type**": "Financial",
    "**Audit Status**": "Completed",
    "**Audit Reason**": "Regular audit",
    "**Auditor Name**": "John Doe",
    "**Department**": "Finance",
    "**Findings**": "Several findings identified.",
    "**Mandatory Actions**": "Implemented corrective actions.",
    "**Recommended Actions**": "Improvement suggestions provided.",
    "**Compliance Status**": "Compliant",
    "**Audit Notes**": "Additional notes about the audit.",
}

# Create the PDF report
create_audit_report("styled_audit_report.pdf", audit_details)