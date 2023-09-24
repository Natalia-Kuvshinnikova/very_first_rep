"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
#

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    # Зададим правую и левую границу диапазона угадываемых чисел
    left_border=0
    right_border=100
    predict_number =np.random.randint(0,101)
    while True:
        # Угадываемым числом будет середина заданного диапазона
         count+=1
         if predict_number>number:
             right_border=predict_number
             predict_number = (left_border + right_border) // 2
         elif predict_number<number: 
             left_border=predict_number
             predict_number = (left_border + right_border) // 2
         else:
             break # Число отгадано       

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
