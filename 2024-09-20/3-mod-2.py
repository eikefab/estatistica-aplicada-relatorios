import pandas as p
import statistics
import scipy.stats as stats
import seaborn
import numpy
import matplotlib.pyplot as plt
import math

iris = p.read_csv("iris.csv")
species = p.unique(iris["Species"]).tolist()

columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

def calculate_distribution():
    _, axes = plt.subplots(nrows=1, ncols=4)


    for b, column in enumerate(columns):
        column_data = iris[column]

        bot, mid, top = numpy.percentile(column_data, [25, 50, 75])
        modes = statistics.multimode(column_data)
        mean = column_data.mean()
        derivation = numpy.std(column_data, ddof=1)

        shapiro = stats.shapiro(column_data).pvalue

        column_value = column_data.values
        inf, sup = mean - derivation * 3, mean + derivation * 3

        outliers = list(column_data[(column_value < inf) | (column_value > sup)])
        amplitude = (top - bot)

        print(f"Média: {mean:.2f}")
        print(f"Moda(s): {modes}")
        print(f"Mediana: {mid:.3f}")
        print(f"Desvio padrão: {derivation:.3f}")
        print(f"Amplitude: {amplitude:.3f}")
        print(f"Outliers: ({len(outliers)}) {outliers}")
        print("Simétrico" if shapiro >= 0.05 else "Assimétrico", f"({shapiro:.10f})\n")

        chart = axes[b]

        seaborn.histplot(
            data=column_data, 
            bins=7,
            ax=chart
        )

        chart.set_title(f"Iris - {column}")
        chart.set_ylabel("Observações")
        chart.set_xlabel(f"Média: {mean:.2f} - Mediana: {mid:.2f} - Moda: {modes} - Desvio {derivation:.2f} - {"Simétrico" if shapiro >= 0.05 else "Assimétrico"} ({shapiro:.2f})")
        chart.grid(True, axis="y")
        chart.set_yticks(numpy.arange(0, 51, 5))

    plt.tight_layout()
    plt.show()

calculate_distribution()