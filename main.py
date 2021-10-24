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


    print("Задание Г1:")
    print(one_to_many)
    print("Задание Г2")
    print("Задание Г3")

if __name__ == '__main__':
    main()