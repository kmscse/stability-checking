from turtle import color
import matplotlib.pyplot as plt


story_level = ["1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF"]
minimum_resisting_and_overturning_moment_ratio = [1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]
Resisting_and_Overturning_Moment_Ratio_Ex = [14.53,15.30,15.89,16.64,17.66,18.98,20.73,23.23,26.81,32.15,40.93,51.44]
Resisting_and_Overturning_Moment_Ratio_Ey = [16.20,17.06,17.72,18.55,19.69,21.17,23.11,25.90,29.89,35.85,45.63,57.03]

plt.plot(minimum_resisting_and_overturning_moment_ratio,story_level,label="minimum resisting and overturning moment ratio",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(Resisting_and_Overturning_Moment_Ratio_Ex,story_level,label="resisting and overturning moment ratio(X-dir)",marker = "D", color="fuchsia",markersize=5,linewidth=2)
plt.plot(Resisting_and_Overturning_Moment_Ratio_Ey,story_level,label="resisting and overturning moment ratio(Y-dir)",marker = "d", color="blue",markersize=5,linewidth=2)
plt.legend(loc="lower right", fontsize="small")
plt.title("Overturning Effect Check")
plt.xlabel("Resisting and Overturning Moment Ratio")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,70)
plt.ylim("1F","RF")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()