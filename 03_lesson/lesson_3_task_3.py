from address import Address
from mailing import Mailing

from_address = Address("123456", "Moskow", "Tverskaya", "10", "25")
to_address = Address("654321", "St.Peterburg", "Pr. Nevskiy", "20", "15")

mailing = Mailing(to_address, from_address, 350, "RU123456789CN")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
