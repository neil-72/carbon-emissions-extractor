import anthropic
import os

def extract_emissions_data(parsed_data):
    """Extract and standardize emissions data using Claude API."""
    client = anthropic.Anthropic(
        api_key=os.getenv('CLAUDE_API_KEY')
    )
    
    # Prepare prompt for Claude
    prompt = """
    Please analyze the following text from sustainability reports and extract:
    1. Scope 1 (direct) emissions
    2. Scope 2 (indirect) emissions - both market-based and location-based if available
    
    Please standardize all units to tCO2e (tonnes of CO2 equivalent) and structure the output as JSON.
    If you find multiple years, include all years found.
    
    Text to analyze:
    {text}
    """
    
    try:
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            temperature=0,
            system="You are an expert in analyzing sustainability reports and extracting emissions data. Always convert units to tCO2e and maintain high precision.",
            messages=[
                {
                    "role": "user",
                    "content": prompt.format(text=parsed_data)
                }
            ]
        )
        return message.content
    except Exception as e:
        print(f"Error using Claude API: {e}")
        return None
