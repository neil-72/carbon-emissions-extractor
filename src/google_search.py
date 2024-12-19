from googleapiclient.discovery import build
import os

def search_sustainability_reports(company_name, years=[2024, 2023, 2022]):
    """Search for sustainability reports using Google Custom Search API."""
    api_key = os.getenv('GOOGLE_API_KEY')
    search_engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')
    
    service = build('customsearch', 'v1', developerKey=api_key)
    pdf_urls = []
    
    for year in years:
        query = f"{company_name} sustainability report {year} filetype:pdf"
        try:
            result = service.cse().list(
                q=query,
                cx=search_engine_id,
                num=3  # Limit to top 3 results per year
            ).execute()
            
            if 'items' in result:
                for item in result['items']:
                    if item['link'].endswith('.pdf'):
                        pdf_urls.append(item['link'])
        except Exception as e:
            print(f"Error searching for {year} report: {e}")
    
    return pdf_urls