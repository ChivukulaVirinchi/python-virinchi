# Plot a dataset with a boolean categorical value.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

X, _, _, Y = np.loadtxt("break_even.txt", skiprows=1, unpack=True)

plt.plot(X, Y, "bo")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Reservations", fontsize=30)
plt.ylabel("Break-even", fontsize=30)

plt.show()
