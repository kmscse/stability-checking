from turtle import color
import matplotlib.pyplot as plt


depth = ["100","88","80","72","64","56","48","40","32","24","16","8","0"]
design_capacity = [55.53,56.44,44.31,29.76,25.09,20.75,11.70,5.70,4.61,4.39,2.82,1.93,1.09]
borehole_1 = [71.41,70.32,51.02,32.43,27.31,22.73,11.71,5.05,4.79,4.56,2.89,2.00,1.16]
borehole_2 = [63.11,62.07,44.94,28.61,23.89,19.57,13.89,5.93,5.68,5.45,3.20,2.24,1.32]
borehole_3 = [55.91,54.83,53.87,39.68,34.78,24.15,15.22,9.27,5.63,5.39,2.87,1.96,1.13]
borehole_4 = [31.70,38.53,27.41,18.31,14.38,16.56,5.99,2.54,2.35,2.17,2.30,1.53,0.74]

plt.plot(design_capacity,depth,label="design capacity", color="red", markersize=5,linewidth=2)
plt.plot(borehole_1,depth,label="borehole-1 capcity", color="cyan",markersize=5,linewidth=2)
plt.plot(borehole_2,depth,label="borehole-2 capacity", color="lime",markersize=5,linewidth=2)
plt.plot(borehole_3,depth,label="borehole-3 capacity", color="blueviolet",markersize=5,linewidth=2)
plt.plot(borehole_4,depth,label="borehole-4 capacity", color="dodgerblue",markersize=5,linewidth=2)
plt.legend(loc="upper right")
plt.title("Geotechnical Capacity of Piles for All Boreholes")
plt.xlabel("Geotechnical Capacity of Piles (Tons)")
plt.ylabel("Depth (ft)")
plt.grid(linestyle="--")
plt.xlim(0,80)
plt.ylim("100","0")
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()