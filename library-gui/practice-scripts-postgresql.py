"""
1. connect to the database
2. create a cursor object
3. write a SQL query
4. commit changes
5. close the database connection
"""


import psycopg2

from dotenv import load_dotenv
load_dotenv()
import os

# database credentials
conn_creds = f"dbname={os.getenv('DBNAME')} user={os.getenv('USER')} password={os.getenv('PASSWORD')} host={os.getenv('HOST')} port={os.getenv('PORT')}"

def createTable():
    conn = psycopg2.connect(conn_creds)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(conn_creds)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))   # note traditional string formatting (%s, % (item...)) is prone to SQL injections
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(conn_creds)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows     # returned as a list

def delete(item):
    conn = psycopg2.connect(conn_creds)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect(conn_creds)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

createTable()
# insert("Apple", 12, 0.99)
# delete("Apple")
update(11, 0.99, "Apple")
print(view())
# delete("Wine Glass")
# update(8, 5.00, "Water Glass")
# print(view())