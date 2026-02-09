from .stats import sum_all, median


ACTIONS = {
    "1": ("sum", sum_all),
    "2": ("median", median),
}


def _read_numbers(path):
    nums = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            nums.append(float(line))
    return nums


def run():
    print("File Stats")
    print("Enter path to a text file with one number per line.")

    path = input("> ").strip()

    print("1) sum  2) median")
    action_choice = input("> ").strip()

    action = ACTIONS.get(action_choice)
    if not action:
        print("Invalid choice.")
        return

    try:
        nums = _read_numbers(path)
        name, fn = action
        result = fn(nums)
        print(f"{name} result: {result}")
    except FileNotFoundError:
        print("File not found.")
    except ValueError as e:
        print(f"Bad data: {e}")