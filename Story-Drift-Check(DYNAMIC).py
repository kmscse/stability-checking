from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF","PWALL","PH"]
allowable_displacement = [2.4,2.88,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,0.96,0.96]
drift_SPECx = [0.69,1.39,0.95,0.87,0.92,0.88,0.83,0.91,0.83,0.74,0.75,0.55,0.31,0.14,0.16]
drift_SPECy = [0.85,1.56,1.02,0.92,0.97,0.91,0.86,0.94,0.85,0.75,0.76,0.55,0.31,0.15,0.17]

plt.plot(allowable_displacement,story_level,label="allowable displacement",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(drift_SPECx,story_level,label="story drift(X-dir)",marker = "^", color="blue",markersize=5,linewidth=2)
plt.plot(drift_SPECy,story_level,label="story drift(Y-dir)",marker = "D", color="green",markersize=5,linewidth=2)
plt.legend(loc="upper right")
plt.title("Story Drift Check")
plt.xlabel("Displacement (in)")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,3)
plt.ylim("GF","PH")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()