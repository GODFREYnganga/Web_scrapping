# Web_scrapping

## Usage

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/Web_scrapping.git

cd Web_scrapping
```

### 2. Install dependencies

	pip install -r requirements.txt

### 3. Run the scraper

	python scrape_wikipedia.py

### 4. Output

A .csv file will be created in the project directory containing the scraped table data.




## ⚙️ How It Works

### 1. Requesting the Page
Uses the `requests` library to fetch the HTML content of the specified Wikipedia page.

### 2. Parsing HTML
- Passes the HTML content to BeautifulSoup for parsing.
- Finds the target `<table>` element by its class or other attributes.

### 3. Extracting Table Data
- Iterates over table rows (`<tr>`) and cells (`<th>`, `<td>`).
- Constructs a list of lists representing the table.

### 4. Creating a DataFrame
- Converts the list representation into a Pandas DataFrame.
- Optionally cleans column names and data types.

### 5. Saving to CSV
- Calls `DataFrame.to_csv()` to export the data to `Australia_companies.csv`.
