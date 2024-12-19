# Carbon Emissions Data Extractor

This tool automatically extracts and standardizes Scope 1 and Scope 2 emissions data from company sustainability reports using Google Search, ParseStudio, and the Claude API.

## Features

- Automated Google search for company sustainability reports
- PDF parsing using ParseStudio
- Emissions data extraction and standardization using Claude API
- Support for multiple years of data (2022-2024)
- Standardized output format for Scope 1 and Scope 2 (market-based and location-based) emissions

## Installation

```bash
# Clone the repository
git clone https://github.com/neil-72/carbon-emissions-extractor.git
cd carbon-emissions-extractor

# Install dependencies
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory
2. Add your API keys:
```
CLAUDE_API_KEY=your_claude_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
```

## Usage

```bash
python main.py "Company Name"
```

## Output Format

The tool outputs standardized emissions data in the following format:

```json
{
    "company_name": "Example Corp",
    "emissions_data": {
        "2024": {
            "scope_1": {"value": 1000, "unit": "tCO2e"},
            "scope_2_market": {"value": 800, "unit": "tCO2e"},
            "scope_2_location": {"value": 900, "unit": "tCO2e"}
        },
        "2023": {
            // Similar structure
        }
    }
}
```