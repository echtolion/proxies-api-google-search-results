import os
import time
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def search_google_via_proxy(query, auth_key, country_code='US', language_code='en', page_number=1):
    """
    Search Google using proxies and retrieve search results.
    
    Args:
        query (str): The search query.
        auth_key (str): The authentication key for the Proxies API.
        country_code (str): Country code for search results localization (default is 'US').
        language_code (str): Language code for search results localization (default is 'en').
        page_number (int): Page number of search results (default is 1).
    
    Returns:
        str: HTML content of the search results page, or None if request failed.
    """
    base_url = "http://api.proxiesapi.com/google"
    params = {
        'auth_key': auth_key,
        'search': query,
        'cc_code': country_code,
        'lc_code': language_code,
        'page': page_number
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return None

def save_search_results(keyword, search_results, directory):
    """
    Save search results to a file.
    
    Args:
        keyword (str): The search keyword.
        search_results (str): HTML content of the search results.
        directory (str): Directory to save the search results.
    """
    keyword_directory = os.path.join(directory, keyword)
    os.makedirs(keyword_directory, exist_ok=True)

    with open(os.path.join(keyword_directory, f"{keyword}_search_results.html"), 'w', encoding='utf-8') as file:
        file.write(search_results)

def main():
    # Load environment variables
    auth_key = os.getenv("PROXIES_API_KEY")
    country_code = os.getenv("COUNTRY_CODE", "US")
    language_code = os.getenv("LANGUAGE_CODE", "en")
    page_number = os.getenv("PAGE_NUMBER", 1)

    # Load keywords from Excel file
    excel_file_path = os.getenv("KEYWORDS_PATH")
    excel_file_name = os.path.splitext(os.path.basename(excel_file_path))[0]
    df = pd.read_excel(excel_file_path, header=None, skiprows=2)
    keywords = df.iloc[:, 0].tolist()  # Start reading from the first column (A) from row 3

    # Create directory for saving search results
    save_directory = os.path.join(os.getcwd(), f"{excel_file_name}_keyword_research")
    os.makedirs(save_directory, exist_ok=True)

    for keyword in keywords:
        # Search Google using proxy
        search_results = search_google_via_proxy(keyword, auth_key, country_code, language_code, page_number)
        
        # Save search results if available
        if search_results:
            save_search_results(keyword, search_results, save_directory)
            print(f"Search results for '{keyword}' saved.")
        else:
            print(f"Failed to fetch search results for '{keyword}'.")

        # Add a delay before the next search
        time.sleep(10)  # Adjust as needed

if __name__ == "__main__":
    main()
