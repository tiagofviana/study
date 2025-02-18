import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    balanced_accuracy_score,
    roc_auc_score,
    roc_curve,
)


def show_tree(tree: DecisionTreeClassifier, feature_names: list, class_names: list):
    plt.figure(figsize=(20, 10))
    plot_tree(
        decision_tree=tree,
        feature_names=feature_names,
        class_names=class_names,
        filled=True,
    )
    plt.show()


def analyze_dataframe(df: pd.DataFrame, lines: int = 12, show_describe: bool = True):
    print("\n\n", df.head(lines))
    print("...")

    print("\n\n", "Tipos das variáveis:\n", df.dtypes)

    if show_describe:
        for item in df.columns:
            print("\n-------------------------------------")
            print(f'Análise da variável "{ item }":')
            print(df[item].describe())
            print(f'Possui "NaN": { df[item].isna().any() }')
            print(df[item].value_counts(dropna=False).sort_index())


def describe_graph(
    df: pd.DataFrame, column_name: str, target: str, quantiles_number: int = 5
):
    df = df.copy()

    if df[column_name].nunique() > quantiles_number:
        # Intervalos de tamanhos iguais com base na classificação ou em quantis de amostra
        df[column_name] = pd.qcut(
            df[column_name], q=quantiles_number, duplicates="drop"
        )

    _, axis_left = plt.subplots(figsize=(16, 9))
    axis_left.set_ylabel(ylabel="Taxa de sobreviventes", color="purple")
    axis_left.tick_params(axis="y", labelcolor="purple")
    axis_left.set_zorder(2)

    # Criar eixo y da direita para a taxa de sobreviventes
    axis_right = axis_left.twinx()
    axis_right.set_ylabel(ylabel="Frequência", color="blue")
    axis_right.tick_params(axis="y", labelcolor="blue")

    sns.countplot(
        data=df,
        x=column_name,
        palette="viridis",
        hue=column_name,
        alpha=0.5,
        ax=axis_right,
    )

    # Relação entre variáveis categóricas (compara as média).
    sns.pointplot(data=df, y=target, x=column_name, ax=axis_left)

    plt.show()


def confusion_matrix_plot(
    model: DecisionTreeClassifier, X_train: pd.DataFrame, y_train: pd.DataFrame
):
    cm = confusion_matrix(y_train, model.predict(X_train))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="viridis",
        xticklabels=["Não Sobreviveu (real)", "Sobreviveu (real)"],
        yticklabels=["Não Sobreviveu (previsão)", "Sobreviveu (previsão)"],
    )
    plt.show()


def auc_curve_plot(
    model: DecisionTreeClassifier,
    y: pd.DataFrame,
    X: pd.DataFrame,
    identifier: str,
):
    pred = model.predict(X)

    y_prob = model.predict_proba(X)[:, -1]

    # Calculando acurácia e matriz de confusão
    cm = confusion_matrix(y, pred)
    ac = accuracy_score(y, pred)
    bac = balanced_accuracy_score(y, pred)

    print(f"\nBase de {identifier}:")
    print(f"A acurácia da árvore é: {ac:.1%}")
    print(f"A acurácia balanceada da árvore é: {bac:.1%}")
    auc_score = roc_auc_score(y, y_prob)
    print(f"AUC-ROC: {auc_score:.2%}")
    print(f"Gini de avaliação de modelo: {(2*auc_score-1):.2%}")

    # Relatório de classificação do Scikit
    print("\n", classification_report(y, pred))

    # Gerar a Curva ROC
    fpr, tpr, thresholds = roc_curve(y, y_prob)

    # Plotar a Curva ROC
    plt.figure(figsize=(16, 9))
    plt.plot(fpr, tpr, color="blue", label=f"Curva ROC (AUC = {auc_score:.2f})")
    plt.plot(
        [0, 1], [0, 1], color="red", linestyle="--"
    )  # Linha de referência (modelo aleatório)
    plt.xlabel("Taxa de Falsos Positivos (FPR)")
    plt.ylabel("Taxa de Verdadeiros Positivos (TPR)")
    plt.title(f"Curva ROC - base de {identifier}")
    plt.legend(loc="lower right")
    plt.grid()
    plt.show()


def tree_tunning(
    model: DecisionTreeClassifier,
    X_train: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
    X_test: pd.DataFrame,
) -> DecisionTreeClassifier:
    ccp = model.cost_complexity_pruning_path(
        X_train,
        y_train,
    )

    ginis = []
    for item in ccp["ccp_alphas"]:
        tree = DecisionTreeClassifier(
            criterion="gini",
            max_depth=30,
            random_state=42,
            ccp_alpha=item,
        )

        # Treinar o modelo
        tree.fit(X_train, y_train)
        # AUC - area under curve (Curva ROC)
        auc = roc_auc_score(y_test, tree.predict_proba(X_test)[:, -1])
        ginis.append((auc - 0.5) * 2)

    sns.lineplot(x=ccp["ccp_alphas"], y=ginis)
    plt.ylabel("GINI da árvore")
    plt.xlabel("CCP Alphas")
    plt.title("Avaliação da árvore por valor de CCP-Alpha")
    plt.show()

    df = pd.DataFrame({"ccp": ccp["ccp_alphas"], "GINI": ginis})

    GINI_max = df["GINI"].max()
    ccp_max = df.loc[df["GINI"] == GINI_max, "ccp"].values[0]

    print(f"O GINI máximo é de: {GINI_max:.2%}\nObtido com um ccp de: {ccp_max}")

    model = DecisionTreeClassifier(
        criterion="gini", max_depth=30, random_state=42, ccp_alpha=ccp_max
    )
    model.fit(X_train, y_train)
    return model
