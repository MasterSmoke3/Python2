"""
Пример кода с ошибкой № 4

"""

input_int = input("Введите целое число: ")

if input_int.isdigit():
    print(f'Твое число в степени два равно {int(input_int)**2}')
else:
    print('Ну я же просил ввести целое число! Ну камон!')


input_str = input("А теперь напиши еще раз это число и добавь к нему букву: ")  # например, 10а или 24ц

if input_str.isdigit():
    input_int = int(input_str)
    print(f'{input_int} - это не число')
else:
    print('Ну я же просил ввести число! Ну камон!')