import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Pile-Head-Displacement-Check2(STATIC).csv")
subjects = ["Ex", "Ey"]
dataset = df.groupby("Displacement")[subjects].mean()


indx = np.arange(len(subjects))
displacement_label = np.arange(0,0.9,0.3)
print(dataset.T)
allowable_displacement = list(dataset.T["allowable displacement"])
maximum_displacement = list(dataset.T["maximum displacement"])

bar_width = 0.35

fig, ax = plt.subplots()
bar_allowable_displacement = ax.bar(indx - bar_width/2, allowable_displacement, bar_width, label="allowable displacement")
bar_maximum_displacement = ax.bar(indx + bar_width/2, maximum_displacement, bar_width, label="maximum displacement")

# inserting x-axis label
ax.set_xticks(indx)
ax.set_xticklabels(subjects)

# inserting y-axis label
ax.set_yticks(displacement_label)
ax.set_yticklabels(displacement_label)

# inserting legend
ax.legend()

for i in indx:
    ax.annotate("{0:.0f}".format(bar_allowable_displacement[i].get_height()), 
        xy=(bar_allowable_displacement[i].get_x() + bar_allowable_displacement[i].get_width()/2, bar_allowable_displacement[i].get_height()), 
        xytext=(0, 0.2), 
        textcoords="offset points", 
        ha="center", 
        va="bottom")

for i in indx:
    ax.annotate("{0:.0f}".format(bar_maximum_displacement[i].get_height()), xy=(bar_maximum_displacement[i].get_x() + bar_maximum_displacement[i].get_width()/2, bar_maximum_displacement[i].get_height()), 
        xytext=(0, 0.2), 
        textcoords="offset points", 
        ha="center", 
        va="bottom")


plt.show()