from pprint import pprint


file_name = "recipies.txt"
def cook_book_dict(file_name):
    with open(file_name, encoding="utf-8") as file_obj:
        cook_book = {}
        for line in file_obj:
            dish_name = line.strip()
            # print(dish_name) 
            ingredients_all = []
            name_key = ['ingredient_name', 'quantity', 'measure']
            for item in range(int(file_obj.readline())):
                ingredient = file_obj.readline()
                ingredients = ingredient.strip().split('|')
                dict_product = {}
                dict_product[name_key[0]] = ingredients[0]
                dict_product[name_key[1]] = ingredients[1]
                dict_product[name_key[2]] = ingredients[2].strip()
                ingredients_all.append(dict_product)
            cook_book[dish_name] = ingredients
        
            
            cook_book[dish_name] = ingredients_all
            # pprint(cook_book)
            file_obj.readline()

          
     
    return cook_book
pprint(cook_book_dict(file_name))

cook_book = {'Запеченный картофель': [{'ingredient_name': 'Картофель ',
                           'measure': 'кг',
                           'quantity': ' 1 '},
                          {'ingredient_name': 'Чеснок ',
                           'measure': 'зубч',
                           'quantity': ' 3 '},
                          {'ingredient_name': 'Сыр гауда ',
                           'measure': 'г',
                           'quantity': ' 100 '}],
 'Омлет': [{'ingredient_name': 'Яйцо ', 'measure': 'шт', 'quantity': ' 2 '},    
           {'ingredient_name': 'Молоко ', 'measure': 'мл', 'quantity': ' 100 '},
           {'ingredient_name': 'Помидор ', 'measure': 'шт', 'quantity': ' 2 '}],
 'Утка по-пекински': [{'ingredient_name': 'Утка ',
                       'measure': 'шт',
                       'quantity': ' 1 '},
                      {'ingredient_name': 'Вода ',
                       'measure': 'л',
                       'quantity': ' 2 '},
                      {'ingredient_name': 'Мед ',
                       'measure': 'ст.л',
                       'quantity': ' 3 '},
                      {'ingredient_name': 'Соевый соус ',
                       'measure': 'мл',
                       'quantity': ' 60 '}],
 'Фахитос': [{'ingredient_name': 'Говядина ',
              'measure': 'г',
              'quantity': ' 500 '},
             {'ingredient_name': 'Перец сладкий ',
              'measure': 'шт',
              'quantity': ' 1 '},
             {'ingredient_name': 'Лаваш ', 'measure': 'шт', 'quantity': ' 2 '}, 
             {'ingredient_name': 'Винный уксус ',
              'measure': 'ст.л',
              'quantity': ' 1 '},
             {'ingredient_name': 'Помидор ',
              'measure': 'шт',
              'quantity': ' 2 '}]}


 # задача 2

def get_shop_list_by_dishes(dishes, person_count):

    
    for dish in dishes:
        
        
        if dish in cook_book.keys():
            cook_dict = {}
            for ingredients in cook_book[dish]:

                ingredients['quantity'] = ingredients['quantity'] * person_count
                cook_dict[ingredients['ingredient_name']] = {'quantity': ingredients['quantity'],
                                                              'measure': ingredients['measure']}

        else:
            print(f'{dish} блюда нет в списке')
    return cook_dict



pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
