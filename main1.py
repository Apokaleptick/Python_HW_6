# Задание 1. Гласные буквы
# Команде лингвистов понравилось качество ваших программ, поэтому они
# решили заказать функцию для анализатора текста, которая создавала бы
# список гласных букв в нём и считала бы их количество.
# Напишите программу, которая запрашивает у пользователя текст и генерирует
# список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину

alph = 'ауоыиэяюёе'
text = input('Введите текст: ')
letters = [i for i in text if i in alph]
print(letters)