from flask import Flask

app = Flask(__name__)

@app.route('/encrypt')
def _encrypt():
    return 'to be implemented'

@app.route('/decrypt')
def _decrypt():
    return 'to be implemented'

@app.route('/sign')
def _sign():
    return 'to be implemented'

@app.route('/verify')
def _verify():
    return 'to be implemented'