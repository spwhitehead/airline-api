from fastapi.testclient import TestClient

from main import app
from schemas import Company, FlightData

client = TestClient(app)


def test_list_airline_name():
    response = client.get("/airline")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    expected_airlines = ["Delta", "Southwest", "Alaska"]
    assert response.json() == expected_airlines