from flask import Flask
import json
from time import sleep
import threading

app = Flask(__name__)

@app.route('/')
def test():
    #x = threading.Thread(target=thread_function)
    #x.start()
   # x.join()
   # response = {"foo:bar", "hello:test"}
   response = {
    "test":"foo"
   }
   return response
#    return """
#    {
#        'test':'foo',
#        'foo':'bar',
#        'name':'jenny',
#        'additional':'true',
#        'canyouseethis':'yes
#    }
#    """

def thread_function():
    sleep(1)