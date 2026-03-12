from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app

client = TestClient(app)

@patch("src.services.rag_service.generate_text")
def test_generate_story(mock_generate):

    mock_generate.return_value = "Test story output"

    response = client.post(
        "/api/generate",
        json={
            "prompt": "Describe a sunset over mountains.",
            "parameters": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
    )

    assert response.status_code == 200
    assert "story_segment" in response.json()