import pdftotext

def read_pdf_file(pdf_file):
    pdf_pages = []
    try:
        with open(pdf_file, "rb") as f:
            pdf_pages = pdftotext.PDF(f)
    except:
        pass
    
    return pdf_pages