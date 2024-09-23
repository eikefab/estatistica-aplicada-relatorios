import pandas as p
import scipy.stats as stats
import seaborn
import matplotlib.pyplot as plt

iris = p.read_csv("iris.csv")
species = p.unique(iris["Species"]).tolist()

def show_petal_sepal_corr():
    _, axes = plt.subplots(nrows=1, ncols=3)

    for i, specie in enumerate(species):
        data = iris[iris["Species"] == specie]

        sepal_len = data["SepalLengthCm"]
        petal_len = data["PetalLengthCm"]

        corr = stats.pearsonr(x=sepal_len, y=petal_len).statistic

        print(f"Índice de correlação em {specie} para comprimento da sépala e o da pétala: {corr:.3f}")

        chart = axes[i]

        seaborn.scatterplot(data=iris, x=sepal_len, y=petal_len, ax=chart)
        chart.set_title(f"{specie}")

    plt.tight_layout()
    plt.show()

show_petal_sepal_corr()