from main import to_tree


def test_to_tree(test_data):
    source, expected = test_data
    result = to_tree(source)
    assert result == expected
