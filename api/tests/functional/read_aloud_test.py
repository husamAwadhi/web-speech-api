from webspeech import create_app


def test_initial_reading_task():
    flask_app = create_app("config.TestingConfig")

    with flask_app.test_client() as client:
        response = client.post(
            "/reading-task", json={}, headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200
        assert b"paragraph" in response.data
        assert b"id" in response.data
        assert b"hasNext" in response.data
        assert b"hasPrevious" in response.data


def test_reading_task_with_id():
    flask_app = create_app("config.TestingConfig")

    with flask_app.test_client() as client:
        response = client.post(
            "/reading-task", json={"id": 2}, headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200
        assert b"id" in response.data
        assert response.json.get("id") == 2
