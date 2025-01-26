# Flipkart Web Scraper

## Project Overview
This project is a Python-based web scraper designed to extract details of laptops under ₹50,000 from the Flipkart website. It uses **Selenium** for browser automation and **BeautifulSoup** for parsing the webpage's HTML. The extracted data includes:
- **Product Name**
- **Price**
- **Description**

The scraped data is saved as a CSV file for further analysis.

---

## Tech Stack
- **Python**
- **Selenium**: Automates browser interactions.
- **BeautifulSoup**: Parses HTML content.
- **Pandas**: Organizes and stores scraped data in CSV format.

---

## Features
1. **Automated Search**:
   - Opens the Flipkart website and automatically closes the login popup (if present).
   - Searches for laptops under ₹50,000 based on user input.

2. **Data Extraction**:
   - Extracts the following details from search results:
     - Product Name
     - Price
     - Description (key specifications)
   
3. **Pagination Support**:
   - Navigates through multiple pages of search results automatically.

4. **CSV Export**:
   - Saves the scraped data into a CSV file named `flipkart_laptops_under_50000.csv`.

---

## How It Works
1. **Setup**:
   - Initialize a Selenium WebDriver instance.
   - Open the Flipkart homepage.
   - Close the login modal, if it appears.

2. **Search**:
   - Locate the search bar using XPath.
   - Enter the search query (e.g., "laptop under 50000") and press Enter.

3. **Scraping Data**:
   - Parse the loaded webpage using BeautifulSoup.
   - Extract product details using HTML class names for:
     - Product Name: `"_4rR01T"`
     - Price: `"_30jeq3 _1_WHN1"`
     - Description: `"_1xgFaf"`

4. **Pagination**:
   - Automatically click the "Next" button to scrape data from subsequent pages.

5. **Save Data**:
   - Store the extracted details in a Pandas DataFrame.
   - Export the data as a CSV file.

---

## Prerequisites
- **Python 3.7+**
- **Google Chrome** (installed)
- **ChromeDriver** (compatible with your Chrome version)
- Required Python libraries:
  - `selenium`
  - `beautifulsoup4`
  - `pandas`
  - `lxml`

Install dependencies using:
```bash
pip install selenium beautifulsoup4 pandas lxml
