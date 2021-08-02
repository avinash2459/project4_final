from flask import Flask, make_response, request, jsonify

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.ProdConfig')


@app.route("/hello", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)
