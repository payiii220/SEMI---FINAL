from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('Marianne Faye Moreno, '
            'BSIT III-A, '
            'System Integration and Architecture 1, '
            'SEMI-FINAL EXAM')