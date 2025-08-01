from fastapi.testclient import TestClient
import pytest
from ..main import app

# Create a test client for the app
client = TestClient(app)



# ---
# Test suite for creating and reading different resources
# ---

def test_create_order():
    response = client.post("/orders/", json=sample_order)
    assert response.status_code == 200  # or 201
    assert response.json() is not None

