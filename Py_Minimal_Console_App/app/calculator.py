def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


OPS = {
    "1": ("add", add),
    "2": ("sub", sub),
    "3": ("mul", mul),
    "4": ("div", div),
}


def run():
    print("Calculator")
    print("1) add  2) sub  3) mul  4) div")

    op_choice = input("> ").strip()
    op = OPS.get(op_choice)
    if not op:
        print("Invalid choice.")
        return

    try:
        a = float(input("a: ").strip())
        b = float(input("b: ").strip())
        name, fn = op
        result = fn(a, b)
        print(f"{name} result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid number.")