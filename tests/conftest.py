import pytest


@pytest.fixture
def test_data_1():
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


@pytest.fixture
def test_data_2():
    source = [
        (None, "a"),
        ("b11", "b111"),
        ("a", "a1"),
        ("b", "b1"),
        ("b1", "b11"),
        ("a", "a2"),
        (None, "b"),
        ("a2", "a21"),
        ("a2", "a22"),
        ("b", "b2"),
        (None, "c"),
        ("c", "c1"),
    ]

    expected = {
        "a": {"a1": {}, "a2": {"a21": {}, "a22": {}}},
        "b": {"b1": {"b11": {"b111": {}}}, "b2": {}},
        "c": {"c1": {}},
    }

    return source, expected


@pytest.fixture
def test_data_3():
    source = [
        (None, "a"),
        (None, "b"),
        ("b", "c"),
        ("c", "d"),
        ("a", "e"),
    ]

    expected = {
        "a": {"e": {}},
        "b": {"c": {"d": {}}},
    }

    return source, expected


@pytest.fixture
def test_data_with_error_1():
    source = [
        (None, "a"),
        (None, "b"),
        ("a", "c"),
        ("b", "c"),
    ]

    expected_error_message = "Node 'c' is already referenced in the tree."

    return source, expected_error_message


@pytest.fixture
def test_data_with_error_2():
    source = [
        (None, "a"),
        (None, "b"),
        ("a", "c"),
        ("b", "d"),
        ("d", "e"),
        ("c", "e"),
    ]

    expected_error_message = "Node 'e' is already referenced in the tree."

    return source, expected_error_message


@pytest.fixture
def test_data_with_error_3():
    source = [
        (None, "a"),
        (None, "b"),
        ("c", "d"),
    ]

    expected_error_message = "Nodes that do not fit into the tree: [('c', 'd')]."

    return source, expected_error_message
