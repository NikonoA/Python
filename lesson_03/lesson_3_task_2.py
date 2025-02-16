from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "11", "88005553535"),
    Smartphone("Iphone", "16", "88888888888"),
    Smartphone("Samsung", "9", "99999999999"),
    Smartphone("Nokia", "1100", "55555555555"),
    Smartphone("Phone", "0", "00000000000")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} . {smartphone.number}")
