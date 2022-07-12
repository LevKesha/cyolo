from flask import Flask, render_template
import socket

#Get IP & Hostname
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

app = Flask('app')

@app.route('/')
def index():
    return render_template('index.html', hostname=hostname, IPAddr=IPAddr)

if __name__ == '__main__':
    app.run()
