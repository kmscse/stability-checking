from turtle import color
import matplotlib.pyplot as plt


story_level = ["1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF"]
minimum_resisting_and_overturning_moment_ratio = [1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]
Resisting_and_Overturning_Moment_Ratio_SPECx = [24.68,26.17,27.18,28.28,29.64,31.26,33.26,36.11,40.12,46.10,56.29,67.72]
Resisting_and_Overturning_Moment_Ratio_SPECy = [22.64,24.04,25.01,26.07,27.39,28.95,30.89,33.61,37.40,42.99,52.42,62.44]

plt.plot(minimum_resisting_and_overturning_moment_ratio,story_level,label="minimum resisting and overturning moment ratio",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(Resisting_and_Overturning_Moment_Ratio_SPECx,story_level,label="resisting and overturning moment ratio(X-dir)",marker = "D", color="teal",markersize=5,linewidth=2)
plt.plot(Resisting_and_Overturning_Moment_Ratio_SPECy,story_level,label="resisting and overturning moment ratio(Y-dir)",marker = "d", color="purple",markersize=5,linewidth=2)
plt.legend(loc="lower right", fontsize="small")
plt.title("Overturning Effect Check")
plt.xlabel("Resisting and Overturning Moment Ratio")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,70)
plt.ylim("1F","RF")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()