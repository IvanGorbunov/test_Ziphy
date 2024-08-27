import pytest


@pytest.fixture
def test_data():
    source = [
        (None, "a"),
        (None, "b"),
        (None, "c"),
        ("a", "a1"),
        ("a", "a2"),
        ("a2", "a21"),
        ("a2", "a22"),
        ("b", "b1"),
        ("b1", "b11"),
        ("b11", "b111"),
        ("b", "b2"),
        ("c", "c1"),
    ]

    expected = {
        "a": {"a1": {}, "a2": {"a21": {}, "a22": {}}},
        "b": {"b1": {"b11": {"b111": {}}}, "b2": {}},
        "c": {"c1": {}},
    }

    return source, expected
