from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Lenina str.", "5", "45")
from_address = Address("654321", "Kirov", "Prospect Mira str.", "7", "85")
track = "MK-123789"
cost = 500

address_mailing = Mailing(track, from_address, to_address, cost)

print(address_mailing)
