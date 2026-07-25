"""Tests for the math_utils module."""

from src.math_utils import add_numbers


def test_add_numbers() -> None:
    """Test addition of positive numbers."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0