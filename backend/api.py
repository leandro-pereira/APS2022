import flask
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

@app.route('/forecast', methods=['GET'])
def home():
    queryParams = request.args
    print(queryParams.get('startDate'),"startDate")
    print(queryParams.get('endDate'),"endDate")
    print(queryParams.get('company'),"company")

    return jsonify([[34.05,"real","2022-02-02"],[39,"forecast","2022-02-02"],[32,"real","2022-02-03"],[32.2,"forecast","2022-02-03"]])

app.run()