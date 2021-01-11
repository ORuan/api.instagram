import flask
from flask import request, jsonify
import os
from selenium_controller import SearchInsta


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def query_bot():
    #response = os.system(f'echo $(python3 selenium_controller.py {username})')
    username = request.args['username']
    search = SearchInsta(username)
    response = search.selenium_get_username()
    print(response)
    return jsonify(response)


app.run()