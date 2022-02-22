import csv

with open('students.csv', 'w', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['First name', 'Last name', 'Age'])
    csv_writer.writerow(['Jack', 'White', 24])
    csv_writer.writerow(['Jane', 'Black', 25])
