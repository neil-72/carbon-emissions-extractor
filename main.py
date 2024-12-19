import os
import sys
import logging
from dotenv import load_dotenv
from src.google_search import search_sustainability_reports
from src.pdf_parser import parse_pdf
from src.emissions_extractor import extract_emissions_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main(company_name):
    # Load environment variables
    load_dotenv()
    logger.info(f"Starting emissions data extraction for: {company_name}")
    
    # Search for sustainability reports
    logger.info("Initiating search for sustainability reports...")
    pdf_urls = search_sustainability_reports(company_name)
    
    # Parse PDFs and extract relevant sections
    logger.info("Starting PDF parsing...")
    parsed_data = []
    for i, url in enumerate(pdf_urls, 1):
        logger.info(f"Processing PDF {i} of {len(pdf_urls)}")
        parsed_content = parse_pdf(url)
        if parsed_content:
            parsed_data.append(parsed_content)
    
    # Extract and standardize emissions data
    if parsed_data:
        logger.info("Extracting emissions data using Claude...")
        emissions_data = extract_emissions_data(parsed_data)
        logger.info("\nExtracted Emissions Data:")
        print(emissions_data)
    else:
        logger.warning("No valid data found in the sustainability reports.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error('Usage: python main.py "Company Name"')
        sys.exit(1)
    
    company_name = sys.argv[1]
    main(company_name)