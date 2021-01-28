import pytest
import requests
from datetime import datetime


@pytest.mark.bug_4
def test_api_enter_name():
    data = {"name": "Nadia Kriazheva"}
    response = requests.post('http://localhost:3001/', json=data)
    assert response.status_code == 200, "Expected: Status: 200 OK"
    response_json = response.json()
    customers = response_json["customers"]
    for customer in customers:
        if customer["name"] == "Caribian Airlnis":
            assert (customer["size"]) == "Medium", "Wrong company size, expected: Medium"


@pytest.mark.bug_7
def test_api_complex_data():
    data = {"name": [1, "a"]}
    response = requests.post('http://localhost:3001/', json=data)
    assert response.status_code == 400, "Expected: Status: 400 Bad Request"
    response_json = response.json()
    assert (response_json["message"]) == "Invalid Data", "expected: message: Invalid Data"


@pytest.mark.bug_9
def test_api_timestamp():
    data = {"name": "Nadia Kriazheva"}
    response = requests.post('http://localhost:3001/', json=data)
    assert response.status_code == 200, "Expected: Status: 200 OK"
    response_json = response.json()
    timestamp = response_json["timestamp"]
    try:
        # Expected: "timestamp": "2021-01-28T20:18:31.533Z"
        # Actual:   "timestamp": "Thu Jan 28 2021"
        datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError as error:
        assert False, "Invalid timestamp: " + str(error)
