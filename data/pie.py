import matplotlib.pyplot as plt

values = [386, 239]
labels = ["Men", "Women"]
colors = ["gold", "red"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)

# generates pie chart
plt.show()