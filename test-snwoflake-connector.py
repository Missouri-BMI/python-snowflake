import snowflake.connector
from dotenv import dotenv_values

# Load environment variables
args = dotenv_values(".env")

# Define connection parameters
conn = snowflake.connector.connect(
        account=args['SNOWFLAKE_ACCOUNT'],  # e.g., 'xy12345.us-east-2.aws'
        user=args['SNOWFLAKE_USER'],
        warehouse=args['SNOWFLAKE_WAREHOUSE'],
        database=args['SNOWFLAKE_DATABASE'],
        schema=args['SNOWFLAKE_SCHEMA'],
        role=args['SNOWFLAKE_ROLE'],
        authenticator='externalbrowser',  # Enables browser-based SSO authentication
)

# Execute a query
cur = conn.cursor()
cur.execute("select current_version()")

# Fetch results
results = cur.fetchall()
print(results)

# Close the connection
cur.close()
conn.close()