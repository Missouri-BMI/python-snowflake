 This README file contains links to the Snowflake documentation for the Python connector.
 The links provide information on how to install the Python connector, how to connect to Snowflake using the connector,
 how to use the connector with Pandas, and how to use the connector with SQLAlchemy.

## Setting Up the Development Environment

To set up a virtual environment and install the required dependencies, follow these steps:
1. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the test scripts**:
    ```bash
    python test-snwoflake-connector.py
    python test-sqlalchemy.py
    ```

5. **Start a Jupyter session**:
    ```bash
    ./run-jup
    ```
    This will create a Jupyter session and open `test-notebook.ipynb`.

 Links:
 - Installation: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-install
 - Connection: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-connect
 - Pandas Integration: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-pandas
 - SQLAlchemy Integration: https://docs.snowflake.com/en/developer-guide/python-connector/sqlalchemy
