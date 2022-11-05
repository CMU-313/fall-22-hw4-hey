from flask import Flask, json

from app.handlers.routes import configure_routes


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
    student = {'studytime' : 3, 'failures' : 0, 'G3' : 17}
    response = client.get(url, data=json.dumps(student), content_type='application/json')
    assert response.status_code == 200
    prediction = response.get_data()

    response = client.get(url, data=json.dumps(student), content_type='application/json')
    assert response.status_code == 200
    assert response.get_data() == prediction    

def test_predict_route_accurate():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    countSuccess = 0
    for i in range(1,11):
        student = {'studytime': abs(min(4, i-2)), 'failures': max(0,min(7,i)-5), 'G3': 10+i}
        response = client.get(url, data=json.dumps(
            student), content_type='application/json')

        if (response.status == 200): countSuccess += 1
    assert countSuccess >= 9
    
