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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phones = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    
    def count_sum(itms_sld):
        ttl_sld = 0
        for sold in itms_sld:
            ttl_sld += sold
            avg_sld = ttl_sld / len(itms_sld)
        return(ttl_sld, avg_sld)
    
    
    all_items_sum = 0
    avg_items_sum = 0

    for one_phone in phones:
        phone_ttl = count_sum(one_phone['items_sold'])
        t, a = phone_ttl
        all_items_sum += t
        avg_items_sum += a
    
        print(f'Cуммарное количество продаж модели {one_phone["product"]}: {t}')
        print(f'Среднее количество продаж модели {one_phone["product"]}: {int(a)}')
    print(f"Суммарное количество продаж всех товаров: {all_items_sum}")    
    print(f"Среднее количество продаж всех товаров: {int(avg_items_sum)}")

            
        
if __name__ == "__main__":
    main()
