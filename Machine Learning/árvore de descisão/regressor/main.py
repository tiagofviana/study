import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from . import utils


df = utils.get_dataframe()
# utils.analyze_data(pd.DataFrame({"x": df["x"], "y": df["y"]}))

model = DecisionTreeRegressor(max_depth=2, ccp_alpha=0)
model.fit(df[["x"]], df["y"])
# utils.show_tree(tree=model, feature_names=["x"])


df["predicts"] = model.predict(df[["x"]])
df["residues"] = df["y"] - df["predicts"]

# utils.analyze_model_plot(df)


# R quadrado
r_squared = r2_score(df["y"], df["predicts"])
print("R quadrado (1): ", r_squared)

r_squared = model.score(df[["x"]], df["y"])
print("R quadrado (2): ", r_squared)

# utils.residues_plot(df)

# TUNNING
print("Iniciando o tunning...")
model = DecisionTreeRegressor(max_depth=30, ccp_alpha=0)
model.fit(df[["x"]], df["y"])

X_train, X_test, y_train, y_test = train_test_split(
    df[["x"]],
    df[["y"]],
    test_size=0.3,
    random_state=42,
)

path = model.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

param_grid = {"ccp_alpha": ccp_alphas[::10]}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,  # 5-fold cross-validation
    scoring="neg_mean_squared_error",
)

grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
print("Melhores parâmetros: ", best_params)

best_model = DecisionTreeRegressor(**best_params, max_depth=30)
best_model.fit(X_train, y_train)

y_pred = best_model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print("R-quadrado na base de testes:", r2)


plt.scatter(y_test, y_pred)
plt.xlabel("Valores Reais")
plt.ylabel("Valores Previstos")
plt.title("Comparação entre Valores Reais e Previstos")
plt.show()
