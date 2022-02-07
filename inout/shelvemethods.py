import shelve

with shelve.open("shelve_test") as cars:
    cars["opel"] = "Germany"
    cars["ford"] = "USA"
    cars["mazda"] = "Japan"
    cars["renault"] = "France"
    cars["vaz"] = "Russia"
    cars["zaz"] = "Ukraine"

    for key in cars:
        print(key + ": " + cars[key])

    while True:
        key = input("Enter a car name: ")
        if key == "quit":
            break
        if key in cars:
            print(f"{key.title()} was made in {cars[key]}")
        else:
            print(f"We don't have a {key}")
