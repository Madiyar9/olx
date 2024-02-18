Title: Web Scraping OLX Kazakhstan Sport and Leisure Section

Description:
This Python script utilizes Selenium and BeautifulSoup to scrape data from the OLX Kazakhstan website's "Sport and Leisure" section. Specifically, it targets advertisements marked as "TOP". It extracts the titles and links of these advertisements and prints them to the console.

Requirements:

Python 3.x
selenium library
beautifulsoup4 library
webdriver_manager library
Chrome web browser
Installation:

Ensure you have Python installed on your system. If not, download and install it from Python's official website.
Install the required Python libraries using pip:
Copy code
pip install selenium beautifulsoup4 webdriver_manager
Make sure you have Google Chrome installed on your system. If not, download and install it from the official website.
Ensure you have a stable internet connection.
Usage:

Clone or download the provided Python script to your local machine.
Open a terminal or command prompt.
Navigate to the directory where the script is located.
Run the script using the following command:
Copy code
python script_name.py
Replace script_name.py with the name of the downloaded script file.
Options:

By default, the script runs in headless mode, meaning it does not open a visible browser window. If you want to see the browser window while the script is running, comment out the line chrome_options.add_argument("--headless").
You can modify the url variable to target a different OLX Kazakhstan page within the "Sport and Leisure" section.
Disclaimer:
This script is provided for educational purposes only. Scraping data from websites may be against the terms of service of the website being scraped. Use at your own risk.
