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
    Orch(3, "Большой_симфонический_оркестр_имени_П._И._Чайковского"),
    Orch(4, "Государственный академический камерный оркестр России"),
    Orch(5, "Академический симфонический оркестр Московской филармонии"),
]

mus = [
    Mus(1, "Иванов Дмитрий Владимирович", 67000, 5),
    Mus(2, "Дмитриев Владимир Иванович", 55000, 1),
    Mus(3, "Васильев Антон Дмитриевич", 89000, 3),
    Mus(4, "Герасимов Геннадий Васильевич",64000, 4),
    Mus(5, "Зайцев Михаил Анатольевич", 95000, 4),
