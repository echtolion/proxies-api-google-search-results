# proxies-api-google-search-results
CrewAi tool for using proxies api scraper

# Google Search Results Scraper

This script allows you to scrape Google search results using proxies and save them in JSON format.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python 3.x
- `pip` (Python package installer)
- Excel file containing keywords to search for (e.g., `keywords.xlsx`)
- Proxies API key
- `.env` file containing environment variables (see `.env.example` for reference)

## Installation

1. Clone or download the repository to your local machine.
2. Install required Python packages using the following command:

pip install -r requirements.txt


## Usage

1. Set up your environment variables:
- Create a `.env` file in the root directory of the project.
- Add the following variables to the `.env` file:
  ```
  PROXIES_API_KEY=your_proxies_api_key
  COUNTRY_CODE=US
  LANGUAGE_CODE=en
  PAGE_NUMBER=1
  KEYWORDS_PATH=path_to_keywords_excel_file.xlsx
  ```

2. Populate the `keywords.xlsx` file with the keywords you want to search for. Each keyword should be in a separate row.

3. Run the script:

python main.py (rename this if using it as a CrewAI tool)


4. The script will search Google for each keyword using proxies and save the search results in JSON format. The JSON files will be saved in a directory named `<excel_file_name>_keyword_research`.

## Additional Notes

- Adjust the delay between searches by modifying the `time.sleep()` function call in the `main()` function.
- Make sure your Proxies API key is valid and has enough credits for the number of searches you intend to perform.

