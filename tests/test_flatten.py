from src.flatten import flatten_dict, normalize_payload


def test_flatten_dict() -> None:
    payload = {"user": {"name": "Alice", "age": 30}, "active": True}
    flat = flatten_dict(payload)

    assert flat["user.name"] == "Alice"
    assert flat["user.age"] == 30
    assert flat["active"] is True


def test_normalize_payload_list() -> None:
    payload = [{"id": 1, "meta": {"score": 10}}, {"id": 2, "meta": {"score": 20}}]
    rows = normalize_payload(payload)

    assert len(rows) == 2
    assert rows[0]["meta.score"] == 10
