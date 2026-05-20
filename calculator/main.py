#!/usr/bin/env python3

import sys

from pkg.calculator import evaluate


def main():
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = evaluate(expression)
        if result is not None:
            # to_print = format_json_output(expression, result)
            # print(to_print)
            print(f"expression: {expression}")
            print(f"result: {result}")
        else:
            print("Error: Expression is empty or only contains white space.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
