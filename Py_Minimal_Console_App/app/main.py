from . import calculator
from . import file_stats


MODES = {
    "1": ("calculator", calculator.run),
    "2": ("file stats", file_stats.run),
}


def main():
    while True:
        print("1) calculator")
        print("2) file stats")
        print("q) quit")
        choice = input("> ").strip().lower()

        if choice == "q":
            break

        mode = MODES.get(choice)
        if not mode:
            print("Invalid choice.")
            continue

        _, fn = mode
        fn()
        print()  # blank line between runs


if __name__ == "__main__":
    main()