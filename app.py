import psycopg2
from flask import Flask

conn = psycopg2.connect(database="test", user = "sid", password = "", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def get_notes():
  cur.execute('select * from notes')
  result = cur.fetchall()
  return(str(result))
  conn.close()

if __name__ == "__main__": 
        app.run()
