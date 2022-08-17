from flask import Flask, render_template
from datetime import datetime
from meteostat import Point, Daily
import socket

#Get IP & Hostname
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

start = datetime.today()
end = datetime.today()

telaviv = Point(32.0853, 34.7818, 5)

cel = Daily(telaviv, start, end)
cel = str(cel.fetch())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', hostname=hostname, IPAddr=IPAddr, cel=cel)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
