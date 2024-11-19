# Lambda-функция:
first = 'Мама мыла раму'  # Первая строка
second = 'Рамена мало было'  # Вторая строка

# Используем функцию map с лямбда-функцией для сравнения символов из двух строк на одинаковые позиции
# Результатом будет список True или False в зависимости от того, совпадает ли символ в этих строках на соответствующих позициях
result = list(map(lambda word1, word2: word1 == word2, first, second))

# Выводим результат: список из True и False
print(result)


# Замыкание:
# Функция, возвращающая замыкание
def get_advanced_writer(file_name):
    # Замкнутая функция для записи данных в файл
    def write_everything(*data_set):
        # Открываем файл для записи
        with open(file_name, 'w', encoding='utf-8') as file:
            # Проходим по всем переданным данным и записываем их в файл
            for item in data_set:
                file.write(f'{item}\n')

    # Возвращаем функцию записи
    return write_everything


# Создаем экземпляр функции для записи в файл 'example.txt'
write = get_advanced_writer('example.txt')
# Вызываем замыкание с набором данных для записи в файл
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
# Класс MysticBall, который использует метод __call__
class MysticBall:
    # Инициализация: принимаем список возможных ответов
    def __init__(self, *words):
        self.words = words

    # Метод __call__ позволяет экземпляру класса работать как функция
    def __call__(self):
        from random import choice
        # Возвращаем случайный элемент из списка слов
        return choice(self.words)


# Создаем экземпляр класса с возможными ответами
first_ball = MysticBall('Да', 'Нет', 'Наверное')
# Вызываем объект, который теперь ведет себя как функция
print(first_ball())  # Выведет случайный ответ из списка
print(first_ball())  # Выведет еще один случайный ответ
print(first_ball())  # И еще один случайный ответ
