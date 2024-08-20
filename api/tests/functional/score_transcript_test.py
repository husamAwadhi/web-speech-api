from webspeech import create_app


def test_no_params_request_handling():
    flask_app = create_app("config.TestingConfig")

    with flask_app.test_client() as client:
        response = client.post(
            "/score", json={}, headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 500


def test_score_response():
    flask_app = create_app("config.TestingConfig")

    with flask_app.test_client() as client:
        response = client.post(
            "/score",
            json={
                "id": 1,
                "duration": 12.1,
                "transcript": "discovering the wonders of nature is a universal joy",
            },
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 200
