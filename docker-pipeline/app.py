from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    # flask_env = os.getenv('FLASK_ENV', 'not set')
    return f'Hello, Docker!'

