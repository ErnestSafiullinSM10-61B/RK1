# используется для сортировки
from operator import itemgetter

class Lang:
    """Язык программирвания"""
    def __init__(self, id, lang, age, oper_id):
        self.id = id
        self.lang = lang
        self.age = age
        self.oper_id = oper_id
class Oper:
    """Оператор"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
# Оператор
opers = [
    Oper(11, 'Оператор присваивания'),
    Oper(22, 'Арифметические операторы'),
    Oper(33, 'Логические операторы'),
    Oper(44, 'Операторы сравнения'),
    Oper(55, 'Операторы выбора'),
]
# Главы
langs = [
    Lang(1, 'Python', 26, 11),
    Lang(2, 'C++', 25, 22),
    Lang(3, 'C#', 194, 33),
    Lang(4, 'C', 133, 44),
    Lang(5, 'Pascal', 154, 55),
]
def main():
    """Основная функция"""    # Соединение данных один-ко-многим
    one_to_many = [(c.oper_id, c.age, b.name)
        for b in opers
        for c in langs
        if c.oper_id == b.id]
    print('Задание 1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    print('nЗадание 2')
    res_12_unsorted = []
    # Перебираем все опраторы
    for b in opers:
        c_langs = list(filter(lambda i: i[2]==b.name, one_to_many))
        if len(c_langs) > 0:
            c_ages = [age for _,age,_ in c_langs]
            c_ages_sum = sum(c_ages)
            res_12_unsorted.append((b.name, c_ages_sum))            
            # Сортировка по суммарной странице
    
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
if __name__ == '__main__':
    main()