import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(123)
df = pd.DataFrame({"dados": np.random.normal(size=100)})


def calcular_erro_padrao_media(data, n_boot=1000):
    n = len(data)
    medias_boot = np.zeros(n_boot)
    for i in range(n_boot):
        bootstrap_sample = np.random.choice(data, size=n, replace=True)
        medias_boot[i] = np.mean(bootstrap_sample)
    return medias_boot


amostra_bootstrap = calcular_erro_padrao_media(df["dados"])

plt.hist(amostra_bootstrap)
plt.title("Histograma das médias bootstrap")
plt.xlabel("Médias Bootstrap")
plt.ylabel("Frequência")
plt.show()

desvio_padrao = np.std(amostra_bootstrap)
print(f"Desvio padrão das médias bootstrap: {desvio_padrao}")
