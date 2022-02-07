import shelve

with shelve.open("shelve_test") as cars:
    cars["opel"] = "Germany"
    cars["ford"] = "USA"
    cars["mazda"] = "Japan"
    cars["renault"] = "France"
    print(cars['ford'], cars['renault'])

with shelve.open("shelve_test") as cars:
    cars["vaz 2114"] = "Russia"
