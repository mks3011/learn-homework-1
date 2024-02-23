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


phones = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]


def count_sum(items_sold):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total_sold = 0
    for sold in items_sold:
        total_sold += sold
    average_sold = total_sold / len(items_sold)
    return total_sold, average_sold


all_phones_sold = 0
avg_phones_sold = 0

for one_phone in phones:
    sales = count_sum(one_phone['items_sold'])
    phone_sold, avg_phone_sold = sales
    all_phones_sold += phone_sold
    avg_phones_sold += avg_phone_sold

    print(f'Суммарное количество продаж модели {one_phone["product"]}: {phone_sold}')
    print(f'Среднее количество продаж модели {one_phone["product"]}: {avg_phone_sold}')

print(f"Суммарное количество продаж всех товаров: {all_phones_sold}")
print(f"Среднее количество продаж всех товаров: {avg_phones_sold}")
