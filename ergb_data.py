import sqlite3
import datetime
import ergb_graph
# stores currency data into database
def store_data(data):
    print(f"adding data to {data[0]} table")
    print(f"time: {data[1]} , value :{data[2]}")
    cursor.execute(f"INSERT INTO {data[0]} (time, value) VALUES (?, ?)", (data[1], data[2]))
    conn.commit()
# grabs the data of specified currency
def get_data(currency):
    print(f"grabbing today's exchange rate for {currency}");
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    cursor.execute(f"SELECT strftime('%H:%M:%S', time), value FROM {currency} WHERE date(time) = date('now')")
    value = cursor.fetchall()
    return value

# initializes database, creates tables if not created
def initdb():
    # Connect to the database
    print("creating database")
    conn = sqlite3.connect('currency.db')
    cursor = conn.cursor()
    # initializing tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS usd (
                    time DATE,
                    value INTEGER
                )''')    
    cursor.execute('''CREATE TABLE IF NOT EXISTS euro (
                time DATE,
                value INTEGER
            )''')    
    cursor.execute('''CREATE TABLE IF NOT EXISTS imami_coin (
                time DATE,
                value INTEGER
            )''')    
    # Save the changes
    conn.commit()
    return conn

conn = initdb()
cursor = conn.cursor()
test_currency = "usd"
newdata = [test_currency,datetime.datetime.now(),10000]
store_data(newdata)

rows = get_data(test_currency)
# Initialize empty tuples
time = ()
value = ()

# Iterate through rows and append data to corresponding tuples
for row in rows:
    time += (row[0],)
    value += (row[1],)
    
    

ergb_graph.display_graph(test_currency, time,value)
# Close the connection
conn.close()