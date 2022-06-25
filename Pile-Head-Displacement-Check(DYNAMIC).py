from turtle import color
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

load_type = ["SPECx", "SPECy"]
allowable_displacement = [0.394,0.394]
maximum_displacement = [0.111,0.121]

xpos = np.arange(len(load_type))

plt.xticks(xpos, load_type)
plt.ylabel("Displacement (in)")
plt.xlabel("Load Type")
plt.title("Pile Head Displacement Check")
plt.bar(xpos-0.2, allowable_displacement, width=0.4, label="allowable pile head displacement", color="red") 
plt.bar(xpos+0.2, maximum_displacement, width=0.4, label="maximum pile head displacement", color="dodgerblue") 
plt.legend()
plt.ylim(0,0.5)
plt.show()