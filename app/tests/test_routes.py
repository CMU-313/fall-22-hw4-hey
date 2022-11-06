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

def test_invalid_parameters():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'
    student1 = {'famrel': -1, 'medu': 5, 'fedu': -1, 'studytime': 1000, 'goout':4}
    response1 = client.get(url, data=json.dumps(student1), content_type='application/json')
    print(response1.status_code)
    assert response1.status_code == 500

