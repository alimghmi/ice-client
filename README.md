# ICE Data Scraper with Docker

Scrape, transform, and insert ICE (Intercontinental Exchange) settlement prices into an MSSQL database, with Docker support for easy deployment and scaling.


## 📌 Features:

- **Efficient Scraping:** Targets the Markit ICE Settlement Prices from ICE's official page.
- **Data Transformation:** Tailored data transformation for easy database insertion.
- **MSSQL Support:** Built-in support to insert data into a Microsoft SQL Server database.
- **Dockerized:** Simplified deployment and setup using Docker.
- **Robust Error Handling:** Multi-retry mechanisms and comprehensive logging.


## Getting Started:

### Environment Setup

1. Clone the repository:
   ``` bash 
    git clone git@github.com:alimghmi/ice-client.git
    cd ice-client
   ```
2. Create an `.env` file in the project root and configure the following:
   ```
    URL="https://www.ice.com/public-web/cds-settlement-prices/icc/single-names"
    LOG_LEVEL="INFO"
    OUTPUT_TABLE=<name_of_the_output_table>
    INSERTER_MAX_RETRIES=2
    REQUEST_MAX_RETRIES=3
    REQUEST_BACKOFF_FACTOR=2
    MSSQL_SERVER=<mssql_server>
    MSSQL_DATABASE=<mssql_database>
    MSSQL_USERNAME=<mssql_username>
    MSSQL_PASSWORD=<mssql_password>
   ```
    Replace the placeholders (`<...>`) with the appropriate values.

### Running with Python

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the `main.py` script:
   ```bash
   python main.py
   ```

### Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t ice-data-scraper .
   ```
2. Run the Docker container:
   ```bash
   docker run --env-file .env ice-data-scraper
   ```

## Contribution

Feel free to fork the repository, make changes, and open a pull request. All contributions are welcomed!
