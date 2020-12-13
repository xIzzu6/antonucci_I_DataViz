import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Canada", "United States", "Germany", "Norway"])
y = np.array([0, 100, 200, 300, 400, 500, 600, 700, 800])

x = ["Canada", "United States", "Germany", "Norway"]
y = [625, 653, 360, 457]

plt.ylabel("Total Medals")
plt.xlabel("Countries")
plt.title("Total Medals By Country")

plt.bar(x,y, color = "hotpink")
plt.show()