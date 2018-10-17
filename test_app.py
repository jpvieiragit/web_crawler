from app import app

import json

def test_single_api_call():
    data = {
        "keyword": "Data Science",
        "urls": [
            "https://medium.com/search/posts?q=python"
        ]
    }

    expected_response = {
        "events": [{
            "count": 5,
            "url": "https://medium.com/search/posts?q=python"
        }]
    }

    with app.test_client() as client:
        # Test client uses "query_string" instead of "params"
        response = client.post('/search', data=data)
        # Check that we got "200 OK" back.
        assert response.status_code == 200
        # response.data returns bytes, convert to a dict.
        assert json.loads(response.data) == expected_response