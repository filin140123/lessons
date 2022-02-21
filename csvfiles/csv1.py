import csv

with open("cars.csv", encoding="utf-8") as file:
    r = csv.reader(file)
    for car in r:
        print(f"{car[1]} {car[2]} costs {int(float(car[4]))}$")
