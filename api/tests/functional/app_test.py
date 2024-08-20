from webspeech import create_app


def test_initial_reading_task():
    flask_app = create_app("config.TestingConfig")

    with flask_app.test_client() as client:
        response = client.post(
            "/", json={}, headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 404
