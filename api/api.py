import flask, os
from flask import request, jsonify
from selenium_controller import SearchInsta


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def query_bot():
    username = request.args['username']
    search = SearchInsta(username)
    response = search.selenium_get_username()
    return jsonify(response)

app.run()