from fpdf import FPDF
import base64

class MedicalPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'MedBot Consultation Summary', 0, 1, 'C')

def export_to_pdf(messages):
    pdf = MedicalPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    
    for msg in messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        pdf.multi_cell(0, 10, f"{role}: {msg['content']}")
        pdf.ln(2)
        
    # Return as base64 for download button
    return pdf.output(dest="S").encode("latin-1")