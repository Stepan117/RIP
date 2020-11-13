import random


def genRandom1(num_count: int, begin: int, end: int) -> iter:
    """Генерирует num_count случайных чисел от begin до end, включая их."""
    for i in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    print(str(list(genRandom1(5, 1, 3)))[1:-1])
