import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

n = 1000
media = 173
sd = 7.3

populations = np.random.normal(loc=media, scale=sd, size=(n,1000)).flatten()


media_amostral = np.mean(populations)

inf = np.quantile(populations, 0.025)
sup = np.quantile(populations, 0.975)

sns.histplot(populations, kde=True, color='blue')
plt.axvline(inf, color = 'red', label = 'Limite Inferior')
plt.axvline(sup, color = 'red', label = 'Limite Superior')
plt.axvline(media_amostral, color='green', linestyle='--', label = 'média')
plt.legend()
plt.show()
