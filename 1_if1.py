"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Введите ваш возраст!'))

    if 3 <= age < 7:
        return 'Ходит в детский сад'
    elif 7 <= age < 18:
        return 'Учиться в школе'
    elif 18 <= age < 23:
        return 'Учится в университете'
    else:
        return 'безработный'
        

if __name__ == "__main__":
   print(main())
