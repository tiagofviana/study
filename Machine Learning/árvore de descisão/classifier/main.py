import pandas as pd
from seaborn import load_dataset
from sklearn.metrics import (
    classification_report,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from . import utils


titanic_df = load_dataset("titanic")

# Data Wrangling

# Verifica se class e pclass são redudantes
# titanic_df["class"] = titanic_df["class"].astype(pd.StringDtype()).replace({
#     "First": "1",
#     "Second": "2",
#     "Third": "3"
# }).astype(int)
# print((df["class"] == df["pclass"]).all(skipna=False))

# Remove as colunas redundantes ou não relevantes
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

# Preenche os valores NaN com a média
titanic_df["age"] = titanic_df["age"].fillna(titanic_df["age"].mean())

# for item in titanic_df.columns:
#     utils.describe_graph(df=titanic_df, target="survived", column_name=item)


# Converte variaveis categoricas em valor numerico
titanic_dummies = pd.get_dummies(titanic_df)
# arquivos pkl mantem todas as propriedades do objeto
# titanic_dummies.to_pickle('titanic.pkl')

target = titanic_dummies["survived"]
data = titanic_dummies.drop(columns=["survived"])

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.01, random_state=42
)


model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=30,  # Overfiting
    random_state=42,
    ccp_alpha=0,
)
model.fit(X=X_train, y=y_train)

model = utils.tree_tunning(
    model=model,
    X_train=X_train,
    y_train=y_train,
    X_test=X_test,
    y_test=y_test,
)

# utils.show_tree(
#     tree=model,
#     feature_names=X_train.columns.tolist(),
#     class_names=["Not Survived", "Survived"],
# )

# Dados para classificar
result = model.predict(X_test)
print("Resultado dos dados não classificados: ", result)


# Comparação a classificação com o valores observados
result_classified_data = model.predict(X_train)

# Tabela cruzada
print(
    "\n---------------------------------\n",
    "Quantidade de acertos: \n",
    pd.crosstab(columns=result_classified_data, index=y_train, margins=True),
    "\n---------------------------------\n",
)
print(
    "Taxa de sobrviventes: \n",
    pd.crosstab(result_classified_data, y_train, normalize="index"),
    "\n---------------------------------\n",
)
print(
    "Taxa de NÃO sobrviventes: \n",
    pd.crosstab(result_classified_data, y_train, normalize="columns"),
    "\n---------------------------------\n",
)

# Matriz de confusão
# utils.confusion_matrix_plot(model=model, X_train=X_train, y_train=y_train)

# Relatório de classificação do Scikit
print("\n Scikit Report: ", classification_report(y_train, model.predict(X_train)))

# AUC ROC
utils.auc_curve_plot(
    model=model,
    identifier="Treino",
    y=y_train,
    X=X_train,
)

utils.auc_curve_plot(
    model=model,
    identifier="Teste",
    y=y_test,
    X=X_test,
)
