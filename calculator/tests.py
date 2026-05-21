#!/usr/bin/env python3

import unittest

from pkg.calculator import evaluate


class TestCalculator(unittest.TestCase):
    def test_addition(self) -> None:
        result = evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self) -> None:
        result = evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self) -> None:
        result = evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self) -> None:
        result = evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self) -> None:
        result = evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self) -> None:
        result = evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self) -> None:
        result = evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("$ 3 5")

    def test_not_enough_operands(self) -> None:
        with self.assertRaises(ValueError):
            evaluate("+ 3")


if __name__ == "__main__":
    unittest.main()
