"""Den 1: ověření, že pytest běží. Smaž, až napíšeš první vlastní test."""


def add(a: int, b: int) -> int:
    return a + b


def test_add() -> None:
    assert add(2, 3) == 5
