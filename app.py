from flask import Flask
import json
from time import sleep


app = Flask(__name__)

@app.route('/')
def test():
    sleep(10)
   # response = {"foo:bar", "hello:test"}
    return """
    {
        'test':'foo',
        'foo':'bar',
        'name':'jenny'
    }
    """