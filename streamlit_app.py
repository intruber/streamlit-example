import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Configure MySQL connection
mysql_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database',
}

# Route for the search page
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        results = perform_search(keyword)
        return render_template('results.html', results=results)
    return render_template('search.html')

# Perform the search query
def perform_search(keyword):
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Modify the query to match your table structure
    query = "SELECT * FROM your_table WHERE column_name LIKE %s"
    keyword = f"%{keyword}%"

    cursor.execute(query, (keyword,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

if __name__ == '__main__':
    app.run()
