from flask import Flask, jsonify, request

app= Flask(__name__)

if __name__=='__server__':
    app.run(debug=True)