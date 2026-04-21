def test_get_activities_returns_dict_with_expected_structure(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    chess_club = payload["Chess Club"]
    assert isinstance(chess_club["description"], str)
    assert isinstance(chess_club["schedule"], str)
    assert isinstance(chess_club["max_participants"], int)
    assert isinstance(chess_club["participants"], list)


def test_get_activities_preserves_participant_data(client):
    response = client.get("/activities")

    payload = response.json()
    assert "michael@mergington.edu" in payload["Chess Club"]["participants"]
