# Entry point of the Flask Application
# Define routes that will handle incoming HTTP requests from frontend
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Saving Money'

