import re

import pytest

from main import to_tree, TreeReferenceError, HangingNodesError


def test_to_tree_1(test_data_1):
    source, expected = test_data_1
    result = to_tree(source)
    assert result == expected


def test_to_tree_2(test_data_2):
    source, expected = test_data_2
    result = to_tree(source)
    assert result == expected


def test_to_tree_3(test_data_3):
    source, expected = test_data_3
    result = to_tree(source)
    assert result == expected


def test_to_tree_with_error_1(test_data_with_error_1):
    source, expected_error_message = test_data_with_error_1
    with pytest.raises(TreeReferenceError, match=expected_error_message):
        to_tree(source)


def test_to_tree_with_error_2(test_data_with_error_2):
    source, expected_error_message = test_data_with_error_2
    with pytest.raises(TreeReferenceError, match=expected_error_message):
        to_tree(source)


def test_to_tree_with_error_3(test_data_with_error_3):
    source, expected_error_message = test_data_with_error_3
    with pytest.raises(HangingNodesError, match=re.escape(expected_error_message)):
        to_tree(source)
