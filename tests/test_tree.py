from main import to_tree


def test_to_tree_1(test_data_1):
    source, expected = test_data_1
    result = to_tree(source)
    assert result == expected


def test_to_tree_2(test_data_2):
    source, expected = test_data_2
    result = to_tree(source)
    assert result == expected
