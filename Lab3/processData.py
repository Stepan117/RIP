import json
from Lab3.printResult import printResult1
from Lab3.unique import Unique1
from Lab3.field import field1
from Lab3.genRandom import genRandom1
from Lab3.cmTimer import cmTimer1

path = 'D:\Учеба\Лабы РИП\Lab3/data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@printResult1
def f1(arg):
    return sorted(Unique1(field1(arg, 'job-name')))


@printResult1
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@printResult1
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@printResult1
def f4(arg):
    gen_salary = list(genRandom1(len(arg), 100000, 200000))
    work_and_salary = list(zip(arg, gen_salary))
    return list(map(lambda x: x[0] + ', зарплата ' + str(x[1]) + ' руб', work_and_salary))


if __name__ == '__main__':
    with cmTimer1():
        f4(f3(f2(f1(data))))
