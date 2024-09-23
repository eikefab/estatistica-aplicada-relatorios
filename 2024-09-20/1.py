import pandas as p

iris = p.read_csv("iris.csv")
species = p.unique(iris["Species"]).tolist()

def show_petal_length_avg():
    for specie in species:
        data = iris[iris["Species"] == specie]

        print(f"Comprimento médio de {specie} -> {data["PetalLengthCm"].mean():.2f}cm")

show_petal_length_avg()