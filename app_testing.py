from app import app


def test_home_page():
    app.config["TESTING"] = True

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Placement Tracker" in response.data