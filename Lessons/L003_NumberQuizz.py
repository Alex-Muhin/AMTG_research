import random
def is_valid(n):
    return n.isdigit() and int(n) in range(1, 101)

def game():
    num = random.randint(1,100)
    count = 7
    while count > 0:
        while True:
            user_num = input('Введите число от 0 до 100 включительно: ')
            if is_valid(user_num) == False:
                print('А может быть все-таки введем целое число от 1 до 100?')
                user_num = input()
            else:
                user_num = int(user_num)
                break
        count -= 1
        if user_num > num:
            print('Ваше число больше загаданного, попробуйте еще разок.', 'Число оставшихся попыток: ', count)

        elif user_num < num:
            print('Ваше число меньше загаданного, попробуйте еще разок.', 'Число оставшихся попыток: ', count)

        elif user_num == num:
            print('Вы угадали, поздравляем!!')
            print('Число попыток: ', 7 - count)
            return 1

    print('Ваши попытки закончились.', 'Спасибо, что играли в числовую угадайку. Еще увидимся...', sep='\n')

    return 0
#========================================== module start =============================================
if __name__ == '__main__':
    exit(0)
#========================================== module start =============================================
def Lesson003_NumberQuizz():

    print('Добро пожаловать в игру "Угадай-ка число!"', 'У вас есть 7 попыток', sep='\n')

    while True:
        game()
        if not input('Если вы хотите продолжить игру, введите "Y", если нет, то нажмите любую клавишу') == "Y":
            break

    print('До новых встреч')