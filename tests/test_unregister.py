from src.app import activities


def test_unregister_success(client):
    existing_email = activities["Chess Club"]["participants"][0]

    response = client.delete(f"/activities/Chess Club/signup?email={existing_email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {existing_email} from Chess Club"
    assert existing_email not in activities["Chess Club"]["participants"]


def test_unregister_returns_400_when_student_not_registered(client):
    response = client.delete("/activities/Chess Club/signup?email=absent@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete("/activities/Unknown Club/signup?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_requires_email_query_param(client):
    response = client.delete("/activities/Chess Club/signup")

    assert response.status_code == 422
