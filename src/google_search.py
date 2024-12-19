from googlesearch import search
import time

def search_sustainability_reports(company_name, years=[2024, 2023, 2022]):
    """Search for sustainability reports using Google Search."""
    pdf_urls = []
    
    for year in years:
        query = f"{company_name} sustainability report {year} filetype:pdf"
        try:
            # Get top 3 results for each year
            search_results = search(query, num_results=3)
            
            for url in search_results:
                if url.lower().endswith('.pdf'):
                    pdf_urls.append(url)
            
            # Add delay to avoid hitting rate limits
            time.sleep(2)
            
        except Exception as e:
            print(f"Error searching for {year} report: {e}")
    
    return pdf_urls