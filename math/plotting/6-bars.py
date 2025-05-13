#!/usr/bin/env python3
np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))
fruit_label = ["apples","bananas","orages","peaches"]
colors = ["red","yellow","#ff8000","#ffe5b4"]
people_label = ["Farrah","Fred","Felicia"]
fig,ax = plt.subplots()
bottom = np.zeros(3)
for i, fruit_type in enumerate (fruit_label):
  fruit_data = fruit[i,:]
  p = ax.bar(np.arange(3), fruit_data, bottom=bottom, width=0.5, label=fruit_type, color=colors[i])
  bottom += fruit_data
  ax.set_xticks(np.arange(3))
  ax.set_xticklabels(people_label)
  ax.set_ylabel("Quality of Fuit")
  ax.set_ylim(0,80)
  ax.set_yticks(np.arange(0,81,10))
  ax.set_title("Number of Fruits per Person")
ax.legend(loc="upper right")
plt.show()

