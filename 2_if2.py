"""

Домашнее задание №1

Условный оператор: Сравнение строк

* 
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    line1 = input()
    line2 = input()
    
    if len(line1) == len(line2):
        return '0'
    elif len(line1) != len(line2) and line2 == 'learn': 
        return '3'
    elif len(line1) > len(line2):
        return '2'
    
    else:
      return 'Нет подходящего условия'

if __name__ == "__main__":
    print(main())
