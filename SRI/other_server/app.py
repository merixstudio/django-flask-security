from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(
    __name__, 
    static_url_path='/static',
)
CORS(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/media/<path:path>')
def send_media(path):
    return send_from_directory('media', path)

if __name__ == '__main__':
    app.run()
