import requests
import os
from parsestudio.parse import PDFParser
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableStructureOptions, EasyOcrOptions, TableFormerMode
from docling.backend.docling_parse_backend import DoclingParseDocumentBackend
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
    """Parse PDF using ParseStudio with optimized settings."""
    pdf_path = download_pdf(url)
    if not pdf_path:
        return None
    
    try:
        # Configure pipeline options for better extraction
        pipeline_options = PdfPipelineOptions(
            do_ocr=True,  # Enable OCR for scanned text
            do_table_structure=True,  # Better for finding emissions data in tables
            table_structure_options=TableStructureOptions(
                do_cell_matching=False,
                mode=TableFormerMode.ACCURATE
            ),
            ocr_options=EasyOcrOptions(
                force_full_page_ocr=True,
                use_gpu=False
            ),
            images_scale=1.0,
            generate_picture_images=True
        )
        
        # Initialize parser with optimized settings
        parser = PDFParser(
            parser="docling",
            parser_kwargs={
                "pipeline_options": pipeline_options,
                "backend": DoclingParseDocumentBackend
            }
        )
        
        # Get both text and tables since emissions data often appears in tables
        output = parser.run([pdf_path], modalities=["text", "tables"])[0]
        
        # Combine text and table data
        full_text = output.text
        if hasattr(output, 'tables'):
            for table in output.tables:
                full_text += "\n\n" + table.markdown
        
        return full_text
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None
    finally:
        try:
            os.remove(pdf_path)
        except:
            pass