# Web_scrapping
Usage

Clone the repository

git clone https://github.com/yourusername/Web_scrapping.git
cd Web_scrapping

Install dependencies

pip install -r requirements.txt

Run the scraper

python scrape_wikipedia.py

Output

A .csv file will be created in the project directory containing the scraped table data.

⚙️ How It Works

Requesting the Page

Uses the requests library to fetch the HTML content of the specified Wikipedia page.

Parsing HTML

Passes the HTML content to BeautifulSoup for parsing.

Finds the target <table> element by its class or other attributes.

Extracting Table Data

Iterates over table rows (<tr>) and cells (<th>, <td>).

Constructs a list of lists representing the table.

Creating a DataFrame

Converts the list representation into a Pandas DataFrame.

Optionally cleans column names and data types.

Saving to CSV

Calls DataFrame.to_csv() to export the data to output.csv.

