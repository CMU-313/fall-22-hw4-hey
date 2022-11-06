from flask import Flask, json
from app.handlers.routes import configure_routes
from flask import Flask, jsonify, request


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'


def test_predict_route_consistent():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    url = '/predict'
    famrel = 4
    Medu = 4
    Fedu = 4
    studytime = 4
    goout = 1
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":0}\n'
    
