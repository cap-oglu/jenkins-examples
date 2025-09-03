"""
Simple Calculator Application for Jenkins CI/CD Example
"""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract second number from first."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide first number by second."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        return base ** exponent


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()

    print("Jenkins CI/CD Example - Calculator App")
    print("=====================================")

    # Demonstrate calculator operations
    print(f"Addition: 10 + 5 = {calc.add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {calc.subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {calc.multiply(10, 5)}")
    print(f"Division: 10 / 5 = {calc.divide(10, 5)}")
    print(f"Power: 2 ^ 3 = {calc.power(2, 3)}")


if __name__ == "__main__":
    main()
