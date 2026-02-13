from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79012345678"),
    Smartphone("Apple", "iPhone 15 Pro Max", "+79253456789"),
    Smartphone("Xiaomi", "Redmi Note 13 Pro", "+79164567890"),
    Smartphone("Google", "Pixel 8 Pro", "+79035678901"),
    Smartphone("Motorola", "Edge 40 Pro", "+79266789012")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
