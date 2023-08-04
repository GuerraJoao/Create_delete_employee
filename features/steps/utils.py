import requests
import json

SUCCESS_MESSAGE = 'Successfully! Record has been '


def create_employee(id, name):
    response = requests.post('https://dummy.restapiexample.com/api/v1/create', {'id': f'{id}', 'name': f'{name}'}, headers={"User-Agent": "XY"})
    assert response.status_code is 200
    return response


def fetch_employee(id):
    response = requests.get(f'https://dummy.restapiexample.com/api/v1/employee/{id}', headers={"User-Agent": "XY"})
    assert response.status_code is 200
    return response


def delete_employee(id):
    response = requests.get(f'https://dummy.restapiexample.com/api/v1/delete/{id}', headers={"User-Agent": "XY"})
    assert response.status_code is 200
    return response


def validate_response(response, request_type):
    """
    :param request_type: 'add', 'fetch', 'delete'
    """
    assert response.status_code is 200
    response.parsed_text = json.loads(response.text)
    if request_type == 'add':
        assert response.parsed_text['message'] == SUCCESS_MESSAGE + 'added.'
    elif request_type == 'fetch':
        assert response.parsed_text['message'] == SUCCESS_MESSAGE + 'fetched.'
    elif request_type == 'delete':
        assert response.parsed_text['message'] == SUCCESS_MESSAGE + 'deleted.'

    return response



