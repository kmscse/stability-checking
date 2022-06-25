from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF"]
factor_of_safety = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
stability_coefficient_SPECx = [0.0094,0.0151,0.0119,0.0105,0.0106,0.0095,0.0084,0.0085,0.0070,0.0056,0.0050,0.0032,0.0016]
stability_coefficient_SPECy = [0.0096,0.0140,0.0105,0.0092,0.0092,0.0082,0.0072,0.0072,0.0059,0.0047,0.0042,0.0027,0.0013]

plt.plot(factor_of_safety,story_level,label="factor of safety",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(stability_coefficient_SPECx,story_level,label="stability coefficient(X-dir)",marker = "D", color="springgreen",markersize=5,linewidth=2)
plt.plot(stability_coefficient_SPECy,story_level,label="stability coefficient(Y-dir)",marker = "d", color="darkorange",markersize=5,linewidth=2)
plt.legend(loc="upper left")
plt.title("P-Delta Effect Check")
plt.xlabel("Stability Coefficient, Ɵ")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,0.14)
plt.ylim("GF","RF")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()