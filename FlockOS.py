import time
import json
import random
import webbrowser
import os
from datetime import datetime
from colorama import Fore, Back, Style, init, deinit

init()


def clear():
    
    if os.name == 'nt':
        _ = os.system('cls')  
    else:
        _ = os.system('clear')



def OSmenu():
    clear()
    
    menu = ("Меню:\n"
    "1) Калькулятор\n"
    "2) Сравнение чисел\n"
    "3) Выход из системы\n"
    "4) Авторы\n"
    "5) Игра Math Logic\n"
    "6) Магазин WildBerries\n"
    "7) Сбербанк\n"
    "8) Браузер Бинь Чилинь\n"
    "9) Время\n"
    "67) Обновления системы")
    
    print(menu)
    choice = int(input("Введите ваш выбор: "))
    return choice

credits = ["flock_me - создал всю OS. Следите за обновлениями тут: @FlockMedia", "fear28 = Роблоксер Джокер Пасхалочник"]
num = 0

filename = 'rbalance.json'
try:
    with open(filename, 'r') as file:
        data = json.load(file)
        Rbalance = data.get('Rbalance', 0)
        activations = data.get('activations', {})
except FileNotFoundError:
    Rbalance = 0
    activations = {}

itemies = [
    "iPhone 28 Messenger MAX Ultra ne Kitai",
    "Кроссовки Nike Original Cum 28 Version",
    "Чехол «Venom» на смартфон vivo",
    "Подушка-игрушка «Кошка Luna»",
    "18+ Фаллоиммитатор (Дилдо) в стиле «fear28»",
    "Игрушка «PopIt! 250 кнопок»",
    "Промокод: WBMonster",
    "Футболка Поло «LaCostya»",
    "Телевизор «Samsung Galaxy Porno 8k ultra228 HD»",
    "IPorn28 Gay Sex Piski Piski",
    "Trusi «Cal In Pussy»"
]

print((Back.WHITE + Fore.RED), "Привет!")
time.sleep(1)
print((Back.WHITE + Fore.RED), "Добро пожаловать во Flock OS")
time.sleep(2)
print("Загрузка занимает немного времени, пожалуйста, подождите")
time.sleep(3)
print((Fore.BLACK), "Пожалуйста, нажмите Enter, чтобы начать: ")
input()

choice = OSmenu()

if choice == 1:
    clear()
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат сложения:", a + b)
    print("Результат вычитания:", a - b)
    print("Результат умножения:", a * b)
    try:
        print("Результат деления:", a / b)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")
    print("Если вы нашли баг, то пишите в ТГ: @flock_me")
    print("Скоро мы перекинем вас в главное меню. Ожидайте")
    time.sleep(10)
    OSmenu()

elif choice == 2:
    clear()
    a = int(input("Введите первое число для сравнения: "))
    b = int(input("Введите второе число для сравнения: "))
    if a > b:
        print(a, "больше чем", b)
    elif a < b:
        print(a, "меньше чем", b)
    else:
        print(a, "равно", b)
    print("Скоро мы перекинем вас в главное меню. Ожидайте!")
    time.sleep(5)
    OSmenu()

elif choice == 3:
    clear()
    print("Завершение работы")
    time.sleep(2)
    print("До свидания!")
    time.sleep(2)
    exit()

elif choice == 4:
    clear()
    print(credits)
    time.sleep(10)
    OSmenu()

elif choice == 5:
    print("Игра скоро появится... Но не факт")
    time.sleep(3)
    OSmenu()

elif choice == 67:
    clear()
    print(
        "Это функция обновления. Через некоторое время мы отправим вас в наш Телеграм-канал, где публикуются все обновления."
    )
    print("Текущая версия: FOS 0.5")
    time.sleep(5)
    print("Если у вас не открылась ссылка, зайдите вручную: @FlockMedia")
    time.sleep(4)
    webbrowser.open("https://t.me/FlockMedia")
    time.sleep(5)
    OSmenu()

elif choice == 6:
    clear()
    print(Fore.MAGENTA + Style.BRIGHT, "WildBerries")
    print(Fore.BLACK, "Меню:\n1) Список товаров\n2) Заказ товаров\n3) Выход")
    cho = int(input("Введите ваше действие: "))
    if cho == 1:
        for idx, item in enumerate(itemies):
            print(f"{idx + 1}) {item}")
    elif cho == 2:
        vebe = int(input("Введите номер товара: "))
        if 1 <= vebe <= len(itemies):
            print(f"Вы заказали товар: {itemies[vebe - 1]}")
        else:
            print("Нет такого товара.")
    elif cho == 3:
        OSmenu()

elif choice == 9:
    clear()
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        clear()
        print(f"Текущее время: {current_time}")

elif choice == 7:
    clear()
    print(Fore.GREEN + Style.BRIGHT, "Сбербанк")
    print(Fore.BLACK, f"Баланс: {Rbalance}")
    print("1) Кликер баланса\n2) Использование промокода\n3)Выход в главное меню")
    rchoise = int(input("Введите пункт: "))
    if rchoise == 1:
        deinit()
        while True:
            input("Нажмите Enter, чтобы увеличить баланс на 1...")
            Rbalance += 1
            print(f"Твой баланс: {Rbalance}")
            with open(filename, 'w') as file:
                json.dump({'Rbalance': Rbalance, 'activations': activations}, file)
    elif rchoise == 2:
        promocodes = {
            "1": {"reward": 100, "limit": 1},
            "blya": {"reward": 200, "limit": 5},
            "sasal?": {"reward": 1488, "limit": 1},
            "WBMonster": {"reward": 500, "limit": 1},
            "using_unity": {"reward": 300, "limit": 1},
            "Welcome!": {"reward": 500, "limit": 3},
            "Pey Gorno": {"reward": 1000, "limit": 1},
        }
        while True:
            promo_choice = input("Введите промокод: ").strip().lower()
            if promo_choice in promocodes:
                reward = promocodes[promo_choice]['reward']
                limit = promocodes[promo_choice].get('limit')
                current_uses = activations.get(promo_choice, 0)
            
                if limit is not None and current_uses >= limit:
                    print("Лимит активирований промокода исчерпан.")
                else:
                    Rbalance += reward
                    print(f"Ваш баланс увеличился на {reward}. Текущий баланс: {Rbalance}")
                    activations[promo_choice] = current_uses + 1
                    with open(filename, 'w') as file:
                        json.dump({'Rbalance': Rbalance, 'activations': activations}, file)
            else:
                print("Такой промокод не существует.")
    elif rchoise == 3:
         OSmenu()
         
    else:
        print((Back.BLUE + Fore.WHITE), ":(   Ошибка 0002! Если вы столкнулись с критическим багом и хотите его решить, то напишите разработчику в тг: @flock_me ! Мы информируем вас о случившейся ошибке, после чего вы сможете перезапустить Flock OS заново!")
        time.sleep(13)
        exit()

else:
    print((Back.BLUE + Fore.WHITE), ":(   Ошибка 0001! Если вы столкнулись с критическим багом и хотите его решить, то напишите разработчику в тг: @flock_me ! Мы информируем вас о случившейся ошибке, после чего вы сможете перезапустить Flock OS заново!")
    time.sleep(13)
    exit()