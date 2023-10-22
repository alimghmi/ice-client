# ICE Data Scraper

This project is designed to scrape the ICE (Intercontinental Exchange) webpage, specifically the Markit ICE Settlement Prices. The scraped data is then transformed and inserted into a Microsoft SQL Server database.


## Environment Setup

To set up the environment for this project, you need to have the following configurations in an `.env` file:

```plaintext
URL="https://www.ice.com/public-web/cds-settlement-prices/icc/single-names"
LOG_LEVEL="INFO"
OUTPUT_TABLE=<name_of_the_output_table>
INSERTER_MAX_RETRIES=2
REQUEST_MAX_RETRIES=3
REQUEST_BACKOFF_FACTOR=2
MSSQL_SERVER=<your_mssql_server>
MSSQL_DATABASE=<your_mssql_database>
MSSQL_USERNAME=<your_mssql_username>
MSSQL_PASSWORD=<your_mssql_password>
```

Replace the placeholders (<...>) with the appropriate values.

## How to Run
1. Ensure you have all the required libraries installed.
2. Set up your .env file with the appropriate values.
3. Run the main.py script:

```bash
python main.py
```

The script will then:

- Initialize the scraping engine
- Fetch the data from the ICE webpage
- Transform the fetched data
- Prepare the database inserter
- Insert the transformed data into the specified output table in the MS SQL Server database
- Log the process as it progresses

