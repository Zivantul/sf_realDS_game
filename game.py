import numpy as np

def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(5))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v1(number):
    '''Просто угадываем на random ни как не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполагаемое число
        if number == predict: 
            break
    return(count) # выход из цикла, если угадали

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Сначала берем середину диапазона, смотрим в какую сторону идти 
        дальше (больше или меньше загаданного числа). Повторяем данный подход, пока не найдем'''
    count = 0
    min_int = 0 #нижняя граница диапазона
    max_int = 100 #верхняя граница диапазона
    cur_min_int = min_int #текущая для шага нижняя граница диапазона
    cur_max_int = max_int #текущая для шага верхняя граница диапазона
    cur_gap = 0 # текущая разница между заданным числом и предсказанием
    predict = 0 # переменная для предсказания
    sh = 0 #признак начала точной настройки
    
    while number != predict:
        if sh == 0:
            predict = (cur_max_int-cur_min_int)//2+cur_min_int # середина текущего диапазон
        
        cur_gap = number - predict
        if cur_gap < 0:
            cur_gap *= -1
        
        count+=1
        
        if cur_gap > 5:
            if number > predict: 
                cur_min_int = predict
            elif number < predict: 
                cur_max_int = predict
            else:
                break
        else:
            sh=1
            if number > predict: 
                predict +=1
            elif number < predict: 
                predict -=1
            else:
                break
    return(count) # выход из цикла, если угадали

# Проверяем
print ("Алгоритм 1")
score_game(game_core_v1)
print ("Алгоритм 2")
score_game(game_core_v2)
print ("Алгоритм 3")
score_game(game_core_v3)