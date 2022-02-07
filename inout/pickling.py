import pickle

honda = ("civic", "grey", "2009", ((1, "James"), (2, "Jane"), (3, "Steve")))

with open("honda.pickle", "wb") as p:
    pickle.dump(honda, p)

with open("honda.pickle", "rb") as r:
    data = pickle.load(r)
print(data)
