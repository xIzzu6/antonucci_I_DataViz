import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Gold", "Silver", "Bronze"])
y = np.array([0, 100, 150, 200, 250, 300, 350, 400])

x = ["Gold", "Silver", "Bronze"]
y = [315, 202, 106]

plt.ylabel("Medals")
plt.xlabel("Types of Medals")
plt.title("Comparing Medals By Gold, Silver, Bronze")

plt.bar(x,y, color = "purple")
plt.show()