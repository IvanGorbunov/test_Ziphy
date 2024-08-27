def _get_node(tree: dict, parent: str):
    """Get the node with the given name from the tree"""
    if parent in tree:
        return tree[parent]
    for child in tree.values():
        result = _get_node(child, parent)
        if result is not None:
            return result
    return None


def _add_node(tree: dict, parent: str, child: str):
    """Add a child node to the parent node in the tree"""
    if parent is None:
        tree[child] = {}
    else:
        parent_node = _get_node(tree, parent)
        if parent_node is not None:
            parent_node[child] = {}
        else:
            raise ValueError(f"Parent node '{parent}' not found in the tree.")


def to_tree(pairs: list) -> dict:
    """Convert a list of pairs to a dictionary representation of the tree"""
    tree = {}
    remaining_pairs = pairs.copy()

    while remaining_pairs:
        for pair in remaining_pairs[:]:
            parent, child = pair
            try:
                _add_node(tree, parent, child)
                remaining_pairs.remove(pair)
            except ValueError:
                continue

    return tree


if __name__ == "__main__":
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

    assert to_tree(source) == expected
