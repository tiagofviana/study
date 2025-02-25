import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    balanced_accuracy_score,
    roc_auc_score,
    roc_curve,
)


def avaliation(
    rfc: RandomForestClassifier,
    y: pd.DataFrame,
    X: pd.DataFrame,
    identifier: str,
):

    pred = rfc.predict(X)

    y_prob = rfc.predict_proba(X)[:, -1]

    cm = confusion_matrix(y, pred)
    ac = accuracy_score(y, pred)
    bac = balanced_accuracy_score(y, pred)

    print(f"\nBase de {identifier}:")
    print(f"A acurácia da árvore é: {ac:.1%}")
    print(f"A acurácia balanceada da árvore é: {bac:.1%}")

    # Calculando AUC
    auc_score = roc_auc_score(y, y_prob)
    print(f"AUC-ROC: {auc_score:.2%}")
    print(f"GINI: {(2*auc_score-1):.2%}")

    # Visualização gráfica
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="viridis",
        xticklabels=["Não Sobreviveu", "Sobreviveu"],
        yticklabels=["Não Sobreviveu", "Sobreviveu"],
    )

    # Relatório de classificação do Scikit
    print("\n", classification_report(y, pred))

    # Gerar a Curva ROC
    fpr, tpr, thresholds = roc_curve(y, y_prob)

    # Plotar a Curva ROC
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color="blue", label=f"Curva ROC (AUC = {auc_score:.2f})")
    plt.plot(
        [0, 1], [0, 1], color="red", linestyle="--"
    )  # Linha de referência (modelo aleatório)
    plt.xlabel("Taxa de Falsos Positivos (FPR)")
    plt.ylabel("Taxa de Verdadeiros Positivos (TPR)")
    plt.title(f"Curva ROC - base de { identifier }")
    plt.legend(loc="lower right")
    plt.grid()
    plt.show()


titanic_df = sns.load_dataset("titanic")
titanic_df.drop(
    inplace=True,
    columns=["class", "who", "adult_male", "deck", "embark_town", "alive", "alone"],
)

titanic_df.rename(
    inplace=True,
    columns={
        "pclass": "class",
        "sibsp": "siblings_spouses",
        "parch": "parent_children",
    },
)


titanic_dummies = pd.get_dummies(titanic_df)

y = titanic_dummies["survived"]
X = titanic_dummies.drop(columns=["survived"])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2360873
)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)


rf = RandomForestClassifier(n_estimators=50, random_state=42)
rf.fit(X_train, y_train)


rf_model = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(
    estimator=rf_model,
    param_grid={
        "n_estimators": [100],
        "max_features": range(1, 11),
    },
    scoring="roc_auc",
    cv=4,
    n_jobs=-1,
)

grid_search.fit(X_train, y_train.values.ravel())

print(grid_search)
print(grid_search.best_params_)
print(grid_search.best_score_)

best_model = grid_search.best_estimator_

print(type(best_model))

avaliation(rfc=best_model, X=X_train, y=y_train, identifier="Treino")
avaliation(rfc=best_model, X=X_test, y=y_test, identifier="Teste")
