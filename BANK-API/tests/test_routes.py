import os
import sys
import pytest


# To get the absolute path to the parent directory of the current file
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(project_dir)
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test case to test the /banks endpoint
def test_get_banks(client):
    response = client.get('/banks')
    assert response.status_code == 200
    assert 'ICICI Bank' in response.json

# Test case to test the /branches/<branch> endpoint
def test_get_branch_details(client):
    response = client.get('/branches/mumbai')
    assert response.status_code == 200
    assert response.json[0]['ifsc'] == 'ICIC0000001'
