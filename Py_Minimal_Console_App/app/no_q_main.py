from . import calculator
from . import file_stats


MODES = {
    "1": ("calculator", calculator.run),
    "2": ("file stats", file_stats.run),
}


def main():
    print("1) calculator")
    print("2) file stats")
    choice = input("> ").strip()

    mode = MODES.get(choice)
    if not mode:
        print("Invalid choice.")
        return

    _, fn = mode
    fn()


if __name__ == "__main__":
    main()