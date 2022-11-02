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
    student1 = {'studytime': -1, 'failures': 1, 'G3': 10}
    student2 = {'studytime': 1, 'failures': -1, 'G3': 10}
    student3 = {'studytime': 1, 'failures': 1, 'G3': -10}

    response1 = client.get(url, data=json.dumps(student1), content_type='application/json')
    assert response1.status_code == "Invalid Parameters"

    response2 = client.get(url, data=json.dumps(student2), content_type='application/json')
    assert response2.status_code == "Invalid Parameters"

    response3 = client.get(url, data=json.dumps(student3), content_type='application/json')
    assert response3.status_code == "Invalid Parameters"
