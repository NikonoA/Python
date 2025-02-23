class Mailing:
    def __init__(self, track, to_address, from_addres, cost):
        self.t = track
        self.cost = cost
        self.to = to_address
        self.fro = from_addres

    def __str__(self):
        return f"Отправление номер {self.t} из {self.fro} в {self.to}. Стоимость {self.cost} рублей"
