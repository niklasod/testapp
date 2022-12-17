from flask import Flask
import json


app = Flask(__name__)

@app.route('/')
def test():
    return "{'name':'hello', 'foo':'bar'}"