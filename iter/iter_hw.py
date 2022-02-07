def get_week_day():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in week:
        yield day


x = get_week_day()
print(next(x))
print(next(x))
print(next(x))
