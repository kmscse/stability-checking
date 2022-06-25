from turtle import color
import matplotlib.pyplot as plt


story_level = ["GF","1F","2F","3F","4F","5F","6F","7F","8F","9F","10F","11F","RF"]
allowable_story_displacement_ratio = [1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4]
story_displacement_ratio_of_points_one_and_sixteen = [1.08,1.08,1.08,1.09,1.09,1.09,1.09,1.09,1.09,1.08,1.08,1.08,1.08]  #SPECx
story_displacement_ratio_of_points_twenty_seven_and_thirty_nine = [1.06,1.07,1.08,1.08,1.09,1.09,1.09,1.09,1.09,1.08,1.08,1.08,1.08] #SPECx
story_displacement_ratio_of_points_sixteen_and_thirty_nine = [1.01,1.01,1.01,1.01,1.01,1.01,1.01,1.01,1.01,1.00,1.00,1.00,1.00]  #SPECy
story_displacement_ratio_of_points_one_and_twenty_seven = [1.01,1.01,1.01,1.01,1.01,1.01,1.01,1.01,1.01,1.00,1.00,1.00,1.00] #SPECy

plt.plot(allowable_story_displacement_ratio,story_level,label="allowable story displacement ratio",marker = "o", color="red", markersize=5,linewidth=2)
plt.plot(story_displacement_ratio_of_points_one_and_sixteen,story_level,label="story displacement ratio of points 1 and 16(X-dir)",marker = "^",color="lime",markersize=5,linewidth=2)
plt.plot(story_displacement_ratio_of_points_twenty_seven_and_thirty_nine,story_level,label="story displacement ratio of points 27 and 39(X-dir)",marker = "D",color="royalblue",markersize=5,linewidth=2)
plt.plot(story_displacement_ratio_of_points_sixteen_and_thirty_nine,story_level,label="story displacement ratio of points 16 and 39(Y-dir)",marker = "^", color="deeppink",markersize=5,linewidth=2)
plt.plot(story_displacement_ratio_of_points_one_and_twenty_seven,story_level,label="story displacement ratio of points 1 and 27(Y-dir)",marker = "D", color="cyan",markersize=5,linewidth=2)
plt.legend(loc="upper left", fontsize="x-small")
plt.title("Torsional Extreme Irregularity Check")
plt.xlabel("Story Displacement Ratio")
plt.ylabel("Story Level")
plt.grid(linestyle="--")
plt.xlim(0,1.6)
plt.ylim("GF","RF")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()


# LINK - https://matplotlib.org/stable/gallery/color/named_colors.html
# LINK -  https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html