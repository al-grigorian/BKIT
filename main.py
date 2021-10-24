from copy import deepcopy
import operator

class Mus:
    def __init__(self, id, fio, sal, orch_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.orc_id = orch_id

class Orch:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mus_Orch:
    def __init__(self, mus_id, orch_id):
        self.mus_id = mus_id
        self.orch_id = orch_id

orch = [
    Orch(1, "Московский симфонический оркестр"),
    Orch(2, "Симфонический оркестр Большого театра"),
    Orch(3, "Оркестр имени П.И.Чайковского"),
    Orch(4, "Государственный оркестр России"),
    Orch(5, "Академический оркестр Московской филармонии"),
]

mus = [
    Mus(1, "Иванов", 67000, 5),
    Mus(2, "Дмитриев", 55000, 1),
    Mus(3, "Васильев", 89000, 3),
    Mus(4, "Герасимов",64000, 4),
    Mus(5, "Зайцев", 95000, 4),
]

mus_orch = [
    Mus_Orch(1, 5),
    Mus_Orch(2, 1),
    Mus_Orch(3, 3),
    Mus_Orch(4, 4),
    Mus_Orch(5, 4),

    Mus_Orch(1, 4),
    Mus_Orch(2, 4),
    Mus_Orch(3, 4),
    Mus_Orch(4, 2),
    Mus_Orch(5, 3),
]

def main():
    # соединение данных один-ко-многим
    one_to_many = [(o.name, m.fio, m.sal) 
        for o in orch
        for m in mus
        if m.orc_id == o.id
    ]

    # соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, m_o.orch_id, m_o.mus_id) 
        for o in orch 
        for m_o in mus_orch
        if o.id == m_o.orch_id]
    
    many_to_many = [(m.fio, m.sal, orch_name) 
        for orch_name, orch_id, mus_id in many_to_many_temp
        for m in mus if m.id == mus_id]

    #------------------------Задание Г1-------------------------------------------
    res1 = {}
    for o in orch:
        for elem in one_to_many:
            if o.name == elem[0]:
                
        

    #-----------------------------------------------------------------------------


    #------------------------Задание Г2-------------------------------------------
    # словарь для оркестров, названия которых начинаются с буквы 'А'
    res2 = {}
    # зарплаты
    sal = []
    for o in orch:
        for elem in one_to_many:
            if o.name == elem[0]:
                # добавление значения зарплаты для каждого музыканта каждого оркестра
                sal.append(elem[2])
        # добавление списка зарплат для каждого оркестра
        res2[o.name] = deepcopy(sal)
        # очищение списка для зарплат нового оркестра
        sal.clear()

    # поиск максимальной зарплаты в каждом отделе
    for value in res2.values():
        if len(value) != 0:
            m = max(value)
            value.clear()
            value.append(m)
    print("Задание Г2:")
    print(res2)
    #-------------------------------------------------------------------
    

    #--------------------------Задание Г3-------------------------------






    #-------------------------------------------------------------------

    """
    for elem in one_to_many:
        if elem[0][0] == 'А':
            # добавление нового оркестра (ключ - название, значение - фа)
            d_orch_mus[elem[0]] = []
    """
    
    
    """
    m = 0
    res = []
    for o in orch:
        for elem in one_to_many:
            if elem[0]

                if elem[2] > m:
                    m = elem[2]
    """

if __name__ == '__main__':
    main()