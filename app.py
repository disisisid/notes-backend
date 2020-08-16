import psycopg2
from flask import Flask
from flask import request
import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

# conn = psycopg2.connect(database="test", user = "sid", password = "", host = "127.0.0.1", port = "5432")
conn = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)

print("Opened database successfully")
cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def get_notes():
  cur.execute('select * from notes');
  result = cur.fetchall()
  # conn.close()
  return(str(result))

@app.route('/create', methods=['POST'])
def take_note():
  if request.method == 'POST':
    cur.execute("insert into notes(note, timestamp) values(request.json['note'], current_timestamp)");
    print('inserted');
    # conn.close()
    return({})

if __name__ == "__main__": 
        app.run()
