"""
Пример кода с ошибкой № 7

"""

print('Программа для визуализации работы индексов\n')
test_string = 'Тестовая строчка'
print(f'{test_string}\n')

ind_1 = input(
    'Введи первый индекс среза (или нажми Enter - это будет означать, что срез берется с начала строки): '
)
ind_2 = input(
    'Введи второй индекс среза (или нажми Enter - это будет означать, что срез берется до конца строки): '
)
step = input(
    'Введи шаг среза (или нажми Enter - это будет означать, что шаг по-умолчанию равен 1): '
)

# Проверяем, не пустая ли строка в ind_1, ind_2, step. Если нет, то переводим в число эти переменные.
if ind_1:
    ind_1 = int(ind_1)
if ind_2:
    ind_2 = int(ind_2)
if step:
    step = int(step)

# Напиши свой код тут, остальной код не трогай

print('\nТвой срез:')

# Создаем список для хранения параметров среза
slice_params = []
if ind_1 is not None:
    slice_params.append(ind_1)
if ind_2 is not None:
    slice_params.append(ind_2)
if step is not None:
    slice_params.append(step)

# Выполняем срез в зависимости от количества параметров
if len(slice_params) == 3:
    print(test_string[slice_params[0]:slice_params[1]:slice_params[2]])
elif len(slice_params) == 2:
    print(test_string[slice_params[0]:slice_params[1]])
elif len(slice_params) == 1:
    print(test_string[slice_params[0]:])
else:
    print(test_string[:])