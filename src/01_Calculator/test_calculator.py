import pytest
from calculator import calculate, prefix_evaluate, to_prefix


@pytest.mark.parametrize(
    ("equation", "result"),
    [
        ("", None),
        ("+ 2 3", 5),
        ("* 2 3", 6),
        ("+ - 2 3 5", 4),
        ("/ * 2 3 5", 1.2),
    ],
)
def test_prefix_evaluate(equation: str, result: int):
    equation_result = prefix_evaluate(equation)
    assert equation_result == result, f"Must be {result}, get {equation_result}"


@pytest.mark.parametrize(
    ("infix_equation", "prefix_equation"),
    [
        ("1 + 2", ["+", "1", "2"]),
        ("1 * 2", ["*", "1", "2"]),
        ("1 + ( 2 - 3 ) * 2", ["+", "1", "*", "-", "2", "3", "2"]),
    ],
)
def test_to_prefix(infix_equation: str, prefix_equation: str):
    assert to_prefix(infix_equation) == prefix_equation


@pytest.mark.parametrize("equation", ["1 + 2", "1 * 2", "1 + ( 2 - 3 ) * 2"])
def test_calculate(equation: str):
    assert calculate(equation) == eval(equation)
