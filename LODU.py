import os, math


def example(): # Получение значений примера
    try:
        A = int(input('Введите значение A: '))
        sign_A_B = input('Введите знак между A и B: ')
        B = int(input('Введите значение B: '))
        sign_B_C = input('Введите знак между B и C: ')
        C = int(input('Введите значение C: '))

        # Проверка примера пользователя на корректность
        valid = input(f'''\nВаш пример: {A}y'' {sign_A_B} {B}y' {sign_B_C} {C}y = 0
[1] - Верно
[2] - Не верно
>>> ''')
        
        print(f'''\nОтлично! Заменим y на K, тогда\n{A}K² {sign_A_B} {B}K {sign_B_C} {C} = 0''')

        # Если пример правильный
        if valid == '1':
            # Вычесление дискриминанта
            print('\nОтлично! Теперь вычислим дискриминант!')
            if sign_A_B == '-':     print(f'''Формула дискриминанта B²-4*A*C, значит: -{B}² - 4*{A}*{C}''')
            elif sign_A_B == '+':   print(f'''Формула дискриминанта B²-4*A*C, значит: {B}² - 4*{A}*{C}''')
            D = B**2 - 4 * A * C
            print(f'''Дискриминант равен: {D}''')


            # Получение ответа
            if D == 0:
                print('\nЕсли дискриминант равен нулю, то:')
                if sign_A_B == '-':
                    K_1_2 = int(B/2*A)
                elif sign_A_B == '+':
                    K_1_2 = int(-B/2*A)
                print(f'K₁ = K₂ = {K_1_2}')
                print(f'''y = (C₁ + C₂x) e^({K_1_2}x)''')


            elif D > 0:
                print('\nЕсли дискриминант больше нуля, то:')
                if sign_A_B == '-':
                    K1 = (B + math.sqrt(D))/2*A
                    K2 = (B - math.sqrt(D))/2*A
                elif sign_A_B == '+':
                    K1 = int((-B + math.sqrt(D))/2*A)
                    K2 = int((-B - math.sqrt(D))/2*A)
                print(f'''K₁ = {round(K1, 2)}\nK₂ = {round(K2, 2)}''')
                print(f'''y = C₁ e^({round(K1, 2)}x) + C₂ e^({round(K2, 2)}x)''')


            elif D < 0:
                print('\nЕсли дискриминант меньше нуля, то:')
                if sign_A_B == '-':
                    alpha = int(B/2*A)
                elif sign_A_B == '+':
                    alpha = int(-B/2*A)
                beta = math.sqrt(D*-1)/2
                beta_new = round(beta, 2)
                print(f'''Альфа = {alpha}\nБета = {beta_new}i''')
                print(f'''y = e^({alpha}x) * (C₁ Cos {beta_new}ix + C₂ Sin {beta_new}ix)''')


        # Если пример не правильный
        else:
            print('\nХорошо, введите значения вашего примера заново!')
            example()


    except: example()


if __name__ == '__main__':
    os.system('cls')
    print('''\tКалькулятор ЛОДУ! Введите значения своего примера и получите полное подробное решение!\n''')
    print('''\t\ty''  -   7y'  +   7y = 0
\t\t↓    ↓    ↓   ↓    ↓
\t\tA   знак  B  знак  C\n\n''')
    example()