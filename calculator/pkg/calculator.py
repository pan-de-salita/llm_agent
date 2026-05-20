#!/usr/bin/env python3

from __future__ import annotations

from typing import NamedTuple

Node = NamedTuple(
    "Node", [("left", ["Node", float]), ("operator", str), ("right", ["Node", float])]
)

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def evaluate(expr: str) -> float | None:
    try:
        tokens: list[str] = expr.strip().split()
        node: Node | float = __parse(tokens)
        if isinstance(node, float):
            return node
        return __compute(node)
    except Exception as e:
        print(f"Evaluation failed: {e}")
        return None


def __parse(
    tokens: list[str],
) -> Node | float:
    _, ast = __parse_term(tokens, 0)
    return ast


def __parse_term(
    tokens: list[str], step: int, node: Node | None = None
) -> tuple[int, Node]:
    step, node = __parse_factor(tokens, step, node) if node is None else (step, node)
    if step < len(tokens):
        operator = tokens[step]
        if operator in ["+", "-"]:
            step, right = __parse_factor(tokens, step + 1)
            step, node = __parse_term(
                tokens, step, Node(left=node, operator=operator, right=right)
            )
    return step, node


def __parse_factor(
    tokens: list[str], step: int, node: Node | None = None
) -> tuple[int, Node]:
    step, node = __parse_literal(tokens, step) if node is None else (step, node)
    if step < len(tokens):
        operator = tokens[step]
        if operator in ["*", "/"]:
            step, right = __parse_literal(tokens, step + 1)
            step, node = __parse_factor(
                tokens, step, Node(left=node, operator=operator, right=right)
            )
    return step, node


def __parse_literal(tokens: list[str], step: int) -> tuple[int, float]:
    return step + 1, float(tokens[step])


def __compute(node: Node) -> float:
    left: float = __compute(node.left) if isinstance(node.left, Node) else node.left
    right: float = __compute(node.right) if isinstance(node.right, Node) else node.right
    return OPERATIONS[node.operator](left, right)
