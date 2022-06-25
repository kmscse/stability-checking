from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF","PWALL","PH"]
allowable_displacement = [2.4,2.88,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,2.4,0.96,0.96]
drift_Ex = [0.97,1.88,1.33,1.28,1.40,1.36,1.30,1.42,1.28,1.11,1.08,0.78,0.49,0.22,0.03]
drift_Ey = [1.00,1.85,1.26,1.20,1.30,1.26,1.20,1.30,1.17,1.00,1.98,0.70,0.41,0.19,0.22]

plt.plot(allowable_displacement,story_level,label="allowable displacement",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(drift_Ex,story_level,label="story drift(X-dir)",marker = "^",color="blue", markersize=5,linewidth=2)
plt.plot(drift_Ey,story_level,label="story drift(Y-dir)",marker = "D", color="green",markersize=5,linewidth=2)
plt.legend(loc="upper right")
plt.title("Story Drift Check")
plt.xlabel("Displacement (in)")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,3)
plt.ylim("GF","PH")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()