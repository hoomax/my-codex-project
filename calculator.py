class Calculator:
    """Simple calculator supporting basic arithmetic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Basic command-line calculator")
    parser.add_argument('operation', choices=['add', 'sub', 'mul', 'div'], help='Operation')
    parser.add_argument('a', type=float, help='First operand')
    parser.add_argument('b', type=float, help='Second operand')

    args = parser.parse_args()
    calc = Calculator()
    ops = {
        'add': calc.add,
        'sub': calc.subtract,
        'mul': calc.multiply,
        'div': calc.divide,
    }
    result = ops[args.operation](args.a, args.b)
    print(result)


if __name__ == '__main__':
    main()
