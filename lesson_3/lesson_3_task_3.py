from address import Address
from mailing import Mailing

to_address = Address("420021", "Казань", "Миславского", "9", "1")
from_address = Address("690001", "Владивосток", "Светланская", "109", "40")
cost = "5500"
track = "9316703180"

my_mailing = Mailing(to_address, from_address, cost, track)

print(my_mailing)
