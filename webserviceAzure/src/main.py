'''
Created on 11 Jul 2018

@author: SIVA5239
'''

from flask.app import Flask
app=Flask(__name__)

@app.route('/hello')
def helloWorld():
    return "hello world"

if __name__=='__main__':
    app.run()
    