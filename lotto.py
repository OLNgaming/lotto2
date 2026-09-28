import random

print("Eurojackpot")

try:
    anzahl_scheine = int(input("Wie viele Scheine möchtest du? "))
    if anzahl_scheine < 1:
        raise ValueError
except ValueError:
    print("Bitte gib eine ganze Zahl größer als 0 ein.")
else:
    for schein in range(1, anzahl_scheine + 1):
        zahlen = sorted(random.sample(range(1, 51), 5))
        eurozahlen = sorted(random.sample(range(1, 13), 2))

        print(f"Schein {schein}: {zahlen} | Eurozahlen: {eurozahlen}")
