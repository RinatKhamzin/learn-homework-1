"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

all_product = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main(all_product):

  phone_list = len(all_product)
  how_sold_all = 0

  for i in range(phone_list):
    how_sold = 0
    
    for j in range(len(all_product[i]['items_sold'])):
      how_sold = how_sold + int(all_product[i]['items_sold'][j])
    how_sold_all = how_sold_all + how_sold  
    print(f'Всего продано {how_sold} штук {all_product[i]['product']}')
    print(f'Cреднее количество продаж {how_sold/len(all_product[i]['items_sold'])}')

  print(f'Всего продано {how_sold_all} телефонов')
  print(f'среднее количество продаж всех товаров {how_sold_all/phone_list}')  
    
if __name__ == "__main__":
    main(all_product)
