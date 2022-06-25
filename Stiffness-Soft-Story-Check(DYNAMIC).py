from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF","PWALL","PH"]
minimum_lateral_stiffness_proportion_70percent = [0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.70,0.00,0.00]
minimum_lateral_stiffness_proportion_80percent = [0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.8,0.00,0.00,0.00]
stiffness_proportion_of_two_stories = [2.03,0.72,0.98,1.13,1.02,1.02,1.20,1.01,1.02,1.25,1.06,1.42,6.80,3.27,0.00]  #SPECx
stiffness_proportion_of_four_stories = [1.61,1.01,1.07,1.16,1.09,1.15,1.21,1.10,1.20,1.43,1.76,3.56,0.00,0.00,0.00] #SPECx
stiffness_proportion_of_two_stories = [1.9,0.7,1.0,1.1,1.0,1.0,1.2,1.0,1.0,1.2,1.1,1.4,7.2,3.2,0.00]  #SPECy
stiffness_proportion_of_four_stories = [1.4,0.7,1.0,1.1,1.1,1.1,1.2,1.1,1.2,1.4,1.7,3.6,0.00,0.00,0.00] #SPECy

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