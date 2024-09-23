import pandas as p

iris = p.read_csv("iris.csv")
species = p.unique(iris["Species"]).tolist()

for specie in species:
    data = iris[iris["Species"] == specie]
    data = data.copy().drop(["Species", "Id"], axis=1)

    print(specie)
    print(data.corr())
    print("\n")