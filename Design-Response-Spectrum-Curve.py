from turtle import color
import matplotlib.pyplot as plt


response_spectrum = [0.2415,0.6037,0.6037,0.4753,0.4074,0.3565,0.3169,0.2852,0.2282,0.1901,0.163,0.1426,0.1268,0.1141,0.1037,0.0951,0.081,0.0698,0.0608,0.0535,0.0474,0.0423,0.0379,0.0342]

plt.plot(response_spectrum,label="design response spectrum", color="blue", markersize=5,linewidth=2)
plt.legend(loc="upper right")
plt.title("Design Response Spectrum")
plt.xlabel("Period, T (sec)")
plt.ylabel("Spectral Response Acceleration,Sa (g)")
plt.grid(linestyle="--")
plt.xlim(0,10)
plt.ylim(0,0.7)
# plt.xticks(list(range(0, 3, int(0.5))))
plt.show()