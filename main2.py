# Задача 2. Случайные соревнования
# Мы хотим протестировать работу электронной таблицы для участников
# некоторых соревнований. Есть два списка, то есть две команды, по 20
# участников в каждом. В них хранятся очки каждого участника — вещественные
# числа с двумя знаками после точки, например 4.03.
# Член одной команды соревнуется с участником другой команды под таким же
# номером. То есть первый соревнуется с первым, второй — со вторым и так
# далее.
# Напишите программу, которая генерирует два списка участников (по 20
# элементов) из случайных вещественных чисел (от 5 до 10). Для этого найдите
# подходящую функцию из модуля random. Затем сгенерируйте третий список, в
# котором окажутся только победители из каждой пары.

import random
team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

team_3=[team_1[i] if team_1[i] >= team_2[i] else team_2[i] for i in range(len(team_1)) ]
print(team_1,team_2,sep='\n')
print(team_3)