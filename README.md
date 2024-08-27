# Тестовая задача "Дерево из списка"

Написать функцию, строящую дерево по списку пар `id` (`id` родителя, `id` потомка),
где `None` - `id` корневого узла.

Пример работы:

```python
source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
```

### 1. Запуск:

```bash
python ./main.py
```

### 2. Запуск тестов:

```bash
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install poetry
poetry install
poetry run pytest --cov=main --cov-report=html tests/
```