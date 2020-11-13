import time
from contextlib import contextmanager


class cmTimer1:
    """Контекстный менеджер, который считает время работы блока кода и выводит его на экран,
    основанный на классе"""
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(cmTimer1.__name__, time.time() - self.start_time)


@contextmanager
def cmTimer2():
    """Контекстный менеджер, который считает время работы блока кода и выводит его на экран,
        основанный на библиотечной функции"""
    start_time = time.time()
    yield
    print(cmTimer2.__name__, time.time() - start_time)


if __name__ == '__main__':
    with cmTimer1():
        time.sleep(5.5)

    with cmTimer2():
        time.sleep(5.5)