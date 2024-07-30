from flask import Flask
from urllib.parse import quote as url_quote

app = Flask(__name__)

# Set the debug mode to True
app.debug = True

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()