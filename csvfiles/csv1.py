import csv

with open("cars.csv", encoding="utf-8") as file:
    r = csv.reader(file)
    next(r)
    for car in r:
        print(f"{car[1]} {car[2]} costs {int(float(car[4]))}$")

with open("cars.csv", encoding="utf-8") as file:
    r = csv.DictReader(file)
    for car in r:
        print(f"{car['Make']} {car['Model']} costs {int(float(car['Price']))}$")
