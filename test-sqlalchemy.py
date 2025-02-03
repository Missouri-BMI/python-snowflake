from sqlalchemy import create_engine 
from snowflake.sqlalchemy import URL 
from sqlalchemy.sql import text
from dotenv import dotenv_values

# Load environment variables
args = dotenv_values(".env")

# Define Snowflake connection parameters
url = URL(
        account=args['SNOWFLAKE_ACCOUNT'],  # e.g., 'xy12345.us-east-2.aws'
        user=args['SNOWFLAKE_USER'],
        warehouse=args['SNOWFLAKE_WAREHOUSE'],
        database=args['SNOWFLAKE_DATABASE'],
        schema=args['SNOWFLAKE_SCHEMA'],
        role=args['SNOWFLAKE_ROLE'],
        authenticator='externalbrowser',  # Enables browser-based SSO authentication
    )
engine = create_engine(url)

# Establish connection
try:
    connection = engine.connect()
    
    query = text('select current_version()')
    results = connection.execute(query).fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()
