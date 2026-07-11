import io

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def create_pdf(messages):

    buffer = io.BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=letter)

    width, height = letter

    y = height - 50

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(170, y, "ZIGGY AI CHAT")

    y -= 30

    pdf.setFont("Helvetica", 11)

    current_date = datetime.now().strftime("%d %B %Y")
    current_time = datetime.now().strftime("%I:%M %p")

    pdf.drawString(50, y, f"Generated on: {current_date}")

    y -= 18

    pdf.drawString(50, y, f"Time: {current_time}")

    y -= 25

    pdf.line(40, y, width - 40, y)

    y -= 25

    for msg in messages:

        sender = "User" if msg["role"] == "user" else "Ziggy AI"

        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(50, y, sender)

        y -= 18

        pdf.setFont("Helvetica", 11)

        lines = msg["content"].split("\n")

        for line in lines:

            pdf.drawString(70, y, line)

            y -= 16

        pdf.drawString(70, y, f"Time: {msg['time']}")

        y -= 20

        pdf.line(40, y, width - 40, y)

        y -= 20

        if y < 60:

            pdf.showPage()

            pdf.setFont("Helvetica", 11)

            y = height - 50

    pdf.save()

    buffer.seek(0)

    return buffer