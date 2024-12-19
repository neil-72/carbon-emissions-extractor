import os
import sys
from dotenv import load_dotenv
from src.google_search import search_sustainability_reports
from src.pdf_parser import parse_pdf
from src.emissions_extractor import extract_emissions_data

def main(company_name):
    # Load environment variables
    load_dotenv()
    
    # Search for sustainability reports
    print(f"Searching for sustainability reports for {company_name}...")
    pdf_urls = search_sustainability_reports(company_name)
    
    # Parse PDFs and extract relevant sections
    print("Parsing PDFs...")
    parsed_data = []
    for url in pdf_urls:
        parsed_content = parse_pdf(url)
        if parsed_content:
            parsed_data.append(parsed_content)
    
    # Extract and standardize emissions data
    if parsed_data:
        print("Extracting emissions data...")
        emissions_data = extract_emissions_data(parsed_data)
        print("\nExtracted Emissions Data:")
        print(emissions_data)
    else:
        print("No valid data found in the sustainability reports.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python main.py "Company Name"')
        sys.exit(1)
    
    company_name = sys.argv[1]
    main(company_name)