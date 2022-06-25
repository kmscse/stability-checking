from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F"]
allowable_effective_mass_ratio = [1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]
story_effective_mass_ratio = [0.47,1.06,1.00,1.05,1.00,1.00,1.05,1.00,1.00,1.04,1.01,1.20]

plt.plot(allowable_effective_mass_ratio,story_level,label="allowable effective mass ratio",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(story_effective_mass_ratio,story_level,label="story effective mass ratio",marker = "D", color="royalblue",markersize=5,linewidth=2)
plt.legend(loc="upper left")
plt.title("Weight(Mass) Irregularity Check")
plt.xlabel("Effective Mass Ratio")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,2)
plt.ylim("GF","11F")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()