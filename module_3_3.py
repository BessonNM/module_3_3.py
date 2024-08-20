print('1.Функция с параметрами по умолчанию:')


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print()
print('2.Распаковка параметров:')


def print_params(a, b, c):
    print(a, b, c)


values_list = [1, 'строка', True]
values_dict = {'a': 2, 'b': 'строка2', 'c': False}
print_params(*values_list)
print_params(**values_dict)

print()
print('3.Распаковка + отдельные параметры:')


def print_params(*args):
    print(*args)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
