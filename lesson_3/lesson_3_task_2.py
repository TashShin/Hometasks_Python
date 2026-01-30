from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3310", "+793545867159"),
    Smartphone("Motorola", "Razer", "+79677510689"),
    Smartphone("Apple", "iPhone", "+79240340671"),
    Smartphone("Google", "Nexus", "+79430751069"),
    Smartphone("Samsung", "Galaxy", "+79543950710")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
