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
    Mus_Orch(5, 4)
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
    res1 = []
    for o in orch:
        if o.name[0] == 'А':
            # cписок музыкантов оркестра
            orch_mus = list(filter(lambda i: i[0] == o.name, one_to_many))
            if len(orch_mus) > 0:
                # имена музыкантов оркестра
                names_mus = [name for _,name,_ in orch_mus]
                res1.append((o.name, names_mus))
    print("Задание Г1: ")
    print(res1)
    #-----------------------------------------------------------------------------


    #------------------------Задание Г2---------------------------------
    # список оркестров, названия которых начинаются с буквы 'А'
    res2_unsorted = []
    # зарплаты
    sal = []
    for o in orch:
        # cписок музыкантов оркестра
        orch_mus = list(filter(lambda i: i[0] == o.name, one_to_many))
        if len(orch_mus) > 0:
            # зарплаты музыкантов оркестра
            sal = [sal for _,_,sal in orch_mus]
            # максимальная зарплата
            max_sal = max(sal)
            res2_unsorted.append((o.name, max_sal))
    res2_sorted = sorted(res2_unsorted, key=operator.itemgetter(1), reverse=True)
    print("Задание Г2: ")
    print(res2_sorted)
    #---------------------------------------------------------------------

    #--------------------------Задание Г3-------------------------------
    res3_unsorted = []
    for o in orch:
        # cписок музыкантов оркестра
        orch_mus = list(filter(lambda i: i[2] == o.name, many_to_many))
        if len(orch_mus) > 0:
            fio_mus_unsorted = [fio for fio,_,_ in orch_mus]
            # отсортированный список фамилий музыкантов
            fio_mus_sorted = sorted(fio_mus_unsorted, key=operator.itemgetter(0))
            res3_unsorted.append((o.name, fio_mus_sorted))
    res3_sorted = sorted(res3_unsorted, key=operator.itemgetter(0), reverse=True)
    print("Задание Г3: ")
    print(res3_sorted)
    #-------------------------------------------------------------------

if __name__ == '__main__':
    main()
