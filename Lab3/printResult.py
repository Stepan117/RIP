def printResult1(func):
    def decorated_func(*args):  # args - для 7-го пункта
        print(func.__name__)
        return_value = func(*args)
        if isinstance(return_value, list):
            for value in return_value:
                print(str(value))
        elif isinstance(return_value, dict):
            for key in return_value.keys():
                print(str(key) + ' = ' + str(return_value[key]))
        else:
            print(return_value)
        return return_value

    return decorated_func


@printResult1
def test_1():
    return 1


@printResult1
def test_2():
    return 'iu5'


@printResult1
def test_3():
    return {'a': 1, 'b': 2}


@printResult1
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('______________')
    test_1()
    test_2()
    test_3()
    test_4()
