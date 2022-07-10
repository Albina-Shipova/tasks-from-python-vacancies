def task(array: str) -> int:
    """
    Find index of first '0'
    """
    for i, number in enumerate(array):
        if int(number) == 0:
            return i


print(task("111111111110000000000000000"))
