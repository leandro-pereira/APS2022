# Python 3.10.4
# lib version
# Flask==2.1.2
# Flask-Cors==3.0.10
# matplotlib==3.5.2
# pandas==1.4.2
# numpy==1.21.6
# yfinance==0.1.70
# pycaret==2.2.1
import flask
from flask import request, jsonify
from flask_cors import CORS
from matplotlib.pyplot import axis

import pandas as pd
import numpy as np
import yfinance as yf
from pycaret.utils import enable_colab

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

@app.route('/forecast', methods=['GET'])
def home():
    queryParams = request.args
    startDate = queryParams.get('startDate')
    endDate = queryParams.get('endDate')
    company = queryParams.get('company')
    print(startDate, "startDate")
    print(endDate, "endDate")
    print(company, "company")
    df = yf.Ticker('{company}.sa'.format(company = company))
    print('${company}.sa'.format(company = company))
    # RADL3 raia drogasil
    # ITSA4 ITAU
    # NUBR33 nubank
    # BBDC4 bradesco
    # use format YYYY-MM-DD
    history = df.history(start=startDate, end=endDate)
    # retirando os campos
    history = history.drop(['Dividends', 'Stock Splits', 'Volume', 'High', 'Low'], axis=1)
    print('asdf {0}'.format(history.to_xarray()))

    return jsonify([[34.05,"real","2022-02-02"],[39,"forecast","2022-02-02"],[32,"real","2022-02-03"],[32.2,"forecast","2022-02-03"]])

app.run()