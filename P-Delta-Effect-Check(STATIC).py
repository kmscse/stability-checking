from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF"]
factor_of_safety = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
stability_coefficient_Ex = [0.0094,0.0145,0.0113,0.0099,0.0100,0.0090,0.0079,0.0080,0.0067,0.0054,0.0049,0.0033,0.0019]
stability_coefficient_Ey = [0.0097,0.0143,0.0107,0.0093,0.0093,0.0083,0.0073,0.0073,0.0061,0.0049,0.0044,0.0029,0.0016]

plt.plot(factor_of_safety,story_level,label="factor of safety",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(stability_coefficient_Ex,story_level,label="stability coefficient(X-dir)",marker = "D", color="deepskyblue",markersize=5,linewidth=2)
plt.plot(stability_coefficient_Ey,story_level,label="stability coefficient(Y-dir)",marker = "d", color="lightcoral",markersize=5,linewidth=2)
plt.legend(loc="upper left")
plt.title("P-Delta Effect Check")
plt.xlabel("Stability Coefficient, Ɵ")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,0.14)
plt.ylim("GF","RF")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()