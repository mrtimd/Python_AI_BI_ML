def sum_all(nums):
    return sum(nums)


def median(nums):
    if not nums:
        raise ValueError("No numbers provided.")

    s = sorted(nums)
    n = len(s)
    mid = n // 2

    if n % 2 == 1:
        return s[mid]

    return (s[mid - 1] + s[mid]) / 2