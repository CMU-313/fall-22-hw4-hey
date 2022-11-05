import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        famrel = request.args.get('famrel')
        Medu = request.args.get('Medu')
        Fedu = request.args.get('Fedu')
        studytime = request.args.get('studytime')
        goout = request.args.get('goout')
        data = [[famrel], [Medu], [Fedu], [studytime], [goout]]
        query_df = pd.DataFrame({'goout': pd.Series(goout), 'famrel': pd.Series(
            famrel), 'Medu': pd.Series(Medu), 'Fedu': pd.Series(Fedu), 'studytime': pd.Series(studytime)})
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction))
