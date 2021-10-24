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
    one_to_many = [(o.name, m.fio, m.sal) 
        for o in orch
        for m in mus
        if m.orc_id == o.id
    ]

    many_to_many_temp = [(o.name, m_o.orch_id, m_o.mus_id) 
        for o in orch 
        for m_o in mus_orch
        if o.id == m_o.orch_id]
    
    many_to_many = [(m.fio, m.sal, orch_name) 
        for orch_name, orch_id, mus_id in many_to_many_temp
        for m in mus if m.id == mus_id]

    d_orch_mus = {}
    for elem in one_to_many:
        if elem[0][0] == 'А':
            d_orch_mus[elem[0]] = elem[1]
    
    print("Задание Г1:")
    print(d_orch_mus)

    m = 0
    res = []
    for o in orch:
        for elem in one_to_many:
            if o.name == elem[0]:
                if elem[2] > m:
                    m = elem[2]
                    

    print("Задание Г2")
    print("Задание Г3")

if __name__ == '__main__':
    main()