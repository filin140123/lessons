import csv


def print_students():
    with open('students.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for s in csv_reader:
            if s:
                print(f'{s[0]} {s[1]}, {s[2]} years old')


print_students()
