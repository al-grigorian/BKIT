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

class MusOrch:
    def __init__(self, mus_id, orch_id):
        self.mus_id = mus_id
        self.orch_id = orch_id

orch = [
    Orch(5, "Московский симфонический оркестр"),
    Orch(7, "Симфонический оркестр Большого театра"),
    Orch(2, 
]

mus = [
    Mus(2, "Иванов Дмитрий Владимирович", 67000, ),
    Mus(4, "Дмитриев Владимир Иванович", 55000, )
    ]