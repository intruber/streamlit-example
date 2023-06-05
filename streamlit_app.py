import mysql.connector

# Database connection details
host = 'db5013282227.hosting-data.io'
port = 3306
user = 'dbu1225225'
password = 'fepvyg-sAgdim-9fysgy'
database = 'your_database_name'  # Replace with your actual database name

# Search query parameters
food_name = 'Search food name here'  # Replace with the food name you want to search for

# Establish a database connection
connection = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Search query
query = "SELECT * FROM foods WHERE food_name = %s"

# Execute the query
cursor.execute(query, (food_name,))

# Fetch all matching rows
rows = cursor.fetchall()

# Process and display the search results
if rows:
    for row in rows:
        print(row)  # Modify this to process or display the results as desired
else:
    print("No matching rows found.")

# Close the cursor and database connection
cursor.close()
connection.close()
