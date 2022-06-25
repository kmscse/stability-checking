from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF","PWALL","PH"]
minimum_lateral_stiffness_proportion_70percent = [0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.00,0.00]
minimum_lateral_stiffness_proportion_80percent = [0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.00,0.00,0.00]
stiffness_proportion_of_two_stories = [1.95,0.72,0.98,1.13,1.02,1.02,1.20,1.02,1.04,1.27,1.11,1.62,7.26,0.56,0.00]  #Ex
stiffness_proportion_of_four_stories = [1.53,0.98,1.07,1.15,1.09,1.16,1.23,1.13,1.24,1.54,1.95,3.52,0.00,0.00,0.00] #Ex
stiffness_proportion_of_two_stories = [1.86,0.69,0.97,1.12,1.01,1.02,1.19,1.02,1.03,1.27,1.09,1.51,7.65,4.07,0.00]  #Ey
stiffness_proportion_of_four_stories = [1.41,0.96,1.05,1.14,1.08,1.14,1.22,1.12,1.23,1.51,1.87,3.90,0.00,0.00,0.00] #Ey

plt.plot(minimum_lateral_stiffness_proportion_70percent,story_level,label="minimum stiffness proportion of 70%",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(minimum_lateral_stiffness_proportion_80percent,story_level,label="minimum stiffness proportion of 80%",marker = "o", color="pink", markersize=5,linewidth=2)
plt.plot(stiffness_proportion_of_two_stories,story_level,label="story stiffness proportion of 70%(X-dir)",marker = "^",color="palegreen",markersize=5,linewidth=2)
plt.plot(stiffness_proportion_of_four_stories,story_level,label="story stiffness proportion of 80%(X-dir)",marker = "D",color="darkcyan",markersize=5,linewidth=2)
plt.plot(stiffness_proportion_of_two_stories,story_level,label="story stiffness proportion of 70%(Y-dir)",marker = "^", color="slateblue",markersize=5,linewidth=2)
plt.plot(stiffness_proportion_of_four_stories,story_level,label="story stiffness proportion of 80%(Y-dir)",marker = "D", color="cornflowerblue",markersize=5,linewidth=2)
plt.legend(loc="lower right")
plt.title("Stiffness Soft Story Check")
plt.xlabel("Lateral Stiffness Ratio")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,8)
plt.ylim("GF","PH")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()