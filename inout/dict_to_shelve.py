import shelve
import pandas as pd

university = shelve.open("university_file")
university['schedules'] = {
        "Monday": ["discrete math", "discrete math", "computer science", "computer science"],
        "Tuesday": ["python 102", "python 102", "computer science", "computer science"],
        "Wednesday": ["html/css", "html/css", "physical science", "physical science"],
        "Thursday": ["django", "django", "python 102", "python 102"],
        "Friday": ["english", "english", "computer science", "physical science"],
    }
university['tutors'] = {
        "math": ["Jack White", "Jim Persons"],
        "python": ["Jury Alexander", "Jane Smith"],
        "django": ["David Jackson", "Lloyd Ginwell"],
    }

# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['math'])

print("Wednesday Schedule:")
for index, course in enumerate(university['schedules']['Wednesday'], 1):
    print(f"{index}. {course.title()}")

print("-" * 20)

print("Math tutors:")
for index, tutor in enumerate(university['tutors']['math'], 1):
    print(f"{index}. {tutor}")

print("-" * 20)

data = pd.DataFrame(university['schedules'])
print(data.to_string())

university.close()
