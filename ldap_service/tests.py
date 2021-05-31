import pytest

from app import create_app


def test_GET_get_lineupid_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/get-lineupid')
        assert response.status_code == 200
        assert b"Get Lineup ID" in response.data
        assert b"Please enter the account number" in response.data


def test_POST_get_lineupid_page():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.post('/get-lineupid')
        assert response.status_code == 200
        assert b"Get Lineup ID" in response.data
        assert b"Please enter the account number" in response.data
