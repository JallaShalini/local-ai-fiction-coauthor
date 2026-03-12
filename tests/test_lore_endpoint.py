from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_add_lore():
    payload = {
        "content": "Aethelgard is a kingdom surrounded by magical forests.",
        "metadata": {
            "type": "world_lore"
        }
    }

    response = client.post("/api/lore", json=payload)

    assert response.status_code == 201