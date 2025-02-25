import os, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    balanced_accuracy_score,
    roc_auc_score,
    roc_curve,
)


FILENAME = "t.json"


def get_dataframe() -> pd.DataFrame:
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return pd.DataFrame(json.load(file))

    with open(f"./{FILENAME}", "x") as file:
        data = generate_data()
        json.dump(data, file, indent=4)
        return pd.DataFrame(data)


def generate_data() -> dict:
    np.random.seed(2360873)
    numbers = np.linspace(0, 1, 1200)
    # Equação do 2 grau
    results = (
        0
        + 10 * numbers
        + -10 * numbers**2
        + np.random.normal(loc=0, scale=0.3, size=len(numbers)) ** 3
    )
    return {
        "x": numbers.tolist(),
        "y": results.tolist(),
    }


def analyze_data(data: pd.DataFrame):
    plt.figure(figsize=(16, 9))  # Adjust figure size as needed
    sns.scatterplot(x="x", y="y", data=data, color="skyblue", label="Observado")

    # Estética do gráfico
    plt.title("Relação Quadrática com Ruído")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(
        loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False
    )  # Adjust legend position
    plt.show()


def show_tree(tree: DecisionTreeRegressor, feature_names: list):
    plt.figure(figsize=(16, 9))
    plot_tree(
        decision_tree=tree,
        feature_names=feature_names,
        filled=True,
    )
    plt.show()


def analyze_model_plot(df: pd.DataFrame):

    plt.figure(figsize=(16, 9))
    sns.scatterplot(x="x", y="y", data=df, color="skyblue", label="Observado")
    plt.plot(
        df["x"],
        df["predicts"],
        color="red",
        label="Predito",
    )

    plt.title("Relação Quadrática com Ruído e Previsão da Árvore")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


def residues_plot(df: pd.DataFrame):
    figure, ax = plt.subplots(1, 2)

    sns.scatterplot(x="x", y="y", data=df, color="skyblue", label="Observado", ax=ax[0])

    ax[0].plot(
        df["x"], df["predicts"], color="red", label="Predito"
    )  # adicionando a linha de previsão
    ax[0].set_title("Relação Quadrática com Ruído e Previsão da Árvore")
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("y")
    ax[0].legend()
    # ax[0].show()

    sns.scatterplot(
        x="x", y="residues", data=df, color="skyblue", label="Observado", ax=ax[1]
    )
    plt.show()
