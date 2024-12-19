import requests
import os
from parsestudio.parse import PDFParser
import tempfile

def download_pdf(url):
    """Download PDF from URL to temporary file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(response.content)
            return tmp_file.name
    except Exception as e:
        print(f"Error downloading PDF: {e}")
        return None

def parse_pdf(url):
    """Parse PDF using ParseStudio."""
    pdf_path = download_pdf(url)
    if not pdf_path:
        return None
    
    try:
        parser = PDFParser(parser="docling")
        output = parser.run([pdf_path], modalities=["text"])[0]
        return output.text
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None
    finally:
        # Clean up temporary file
        try:
            os.remove(pdf_path)
        except:
            pass