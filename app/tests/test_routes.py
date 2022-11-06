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


def test_invalid_parameters():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'
    student1 = {'famrel': -1, 'medu': 5, 'fedu': -1, 'studytime': 1000, 'goout':4}
    response1 = client.get(url, data=json.dumps(student1), content_type='application/json')
    print(response1.status_code)
    assert response1.status_code == 500


def test_predict_route_consistent():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    url = '/predict'
    # sucessful response
    famrel = 4
    Medu = 4
    Fedu = 4
    studytime = 4
    goout = 1
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":0}\n'
 
    responseS1 = client.get(url, query_string=student)
    assert responseS1.status_code == 200
    responseS2 = client.get(url, query_string=student)
    assert responseS2.status_code == 200
    assert responseS1.get_data() == responseS2.get_data()

    # error response
    famrel = 0
    Medu = 0
    Fedu = 0
    studytime = 0
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}'
    responseF1 = client.get(url, query_string=student)
    assert responseF1.status_code == 500
    responseF2 = client.get(url, query_string=student)
    assert responseF2.status_code == 500


def test_predict_route_expected_behavior():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    
    url = '/predict'
    famrel = 2
    Medu = 4
    Fedu = 3
    studytime = 2
    goout = 1
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":1}\n'
    
    url = '/predict'
    famrel = 3
    Medu = 1
    Fedu = 2
    studytime = 4
    goout = 1
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":1}\n'
    
    url = '/predict'
    famrel = 3
    Medu = 2
    Fedu = 1
    studytime = 4
    goout = 1
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":1}\n'
    
    url = '/predict'
    famrel = 3
    Medu = 2
    Fedu = 2
    studytime = 4
    goout = 1
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":1}\n'
    
    url = '/predict'
    famrel = 3
    Medu = 2
    Fedu = 2
    studytime = 4
    goout = 5
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":0}\n'
    
    url = '/predict'
    famrel = 3
    Medu = 2
    Fedu = 2
    studytime = 1
    goout = 4
    student = f'famrel={famrel}&Medu={Medu}&Fedu={Fedu}&studytime={studytime}&goout={goout}'
    response = client.get(url, query_string=student)
    assert response.status_code == 200
    assert response.get_data() == b'{"prediction":0}\n'


