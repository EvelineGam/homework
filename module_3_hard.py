data_structure = [
[1, 2, 3],
{'a':4, 'b':5},
(6, {'cube':7, 'drum':8}),
'Hello',
((), [{(2,'Urban', ('Urban2', 35))}])
] #переменная с вводными данными

def calculate_structure_sum(data): #функция вычисления суммы значений структур в списке
        result = 0 #изначальный результат сложения равен 0
        for data_elem in data: #итерация по всем элементам списка
            if isinstance(data_elem,(list, set, tuple)): #проверка равенства типа элемента списка типам: кортеж, множество, список
                result += calculate_structure_sum(data_elem) # рекурсивная функция для вычисления суммы элементов кортежа/множества/списка
            elif isinstance(data_elem,dict): #проверка равенства типа элемента списка типу: словарь
                listdict = list(data_elem.items()) #приведение словаря к списку пар(ключ-значение)
                result += calculate_structure_sum(listdict) #рекурсивная функция для вычисления суммы элементов списка
            elif isinstance(data_elem,str): #проверка равенства типа элемента списка типу: строка
                result += len(data_elem) #к результату сложения добавляется значение длины строки
            else:
                result += data_elem #к результату сложения добавляется значение элемента          
        return result            
result = calculate_structure_sum(data_structure) # вычисляем результат с помощью функции сложения (указав в качестве параметра функции заданную раннее переменную)
print(result) #выводим результат
