from flask import Flask, jsonify, request
app= Flask(__name__)

@app.route('/')
def root():
    return "root"

@app.route('/user/<user_id>')
def get_user(user_id):
    user={'id':user_id,'nombre':'heber'}
    query=request.args.get('query')
    if query:
        user['query']=query
    return jsonify(user),200

if __name__=="__main__":
    app.run(debug=True)