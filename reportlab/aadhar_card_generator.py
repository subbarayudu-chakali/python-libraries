from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def create_pdf():
    # Create a PDF document
    pdf_path = "output.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Define the image path and rectangle coordinates
    image_path = "company-name.png"
    rect_x, rect_y = 10, 580
    rect_width, rect_height = 300, 200

    # Draw the rectangle
    c.rect(rect_x, rect_y, rect_width, rect_height, stroke=1, fill=0 )

    # Draw the image inside the rectangle
    c.drawImage(image_path, rect_x, rect_y, width=rect_width, height=rect_height)

    # Add text on top of the image
    text = "Hello, this is text on top of the image!"
    text_x, text_y = rect_x + 20, rect_y + rect_height - 40
    c.setFont("Helvetica", 12)
    c.drawString(text_x, text_y, text)

    # Save the PDF
    c.save()


# Call the function to create the PDF
create_pdf()