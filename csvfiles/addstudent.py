import csv


def add_student(fname: str, lname: str, age):
    with open('students.csv', 'a', encoding='utf-8') as file:
        csv_appender = csv.writer(file)
        csv_appender.writerow([fname, lname, age])


add_student('John', 'Smith', 28)
