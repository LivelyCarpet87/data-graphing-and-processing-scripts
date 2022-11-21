import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import string
from scipy.optimize import curve_fit
from scipy import inf

filename = input("Please enter filename in local directory:")
equation = input("Please enter the polynomial to fit:")
bounds = eval(input("Please enter the fitting bounds:"))
padding_x = float(input("Please enter the amount of padding for x direction:"))
padding_y = float(input("Please enter the amount of padding for y direction:"))
figureImgFile = input("Please enter the filename to save to [ENTER to skip]:")

file = open(filename,'r')

lines = file.readlines()
titles = lines.pop(0)
x_title, y_title = titles.strip('\r\n').split(',')
time = []
height = []
for line in lines:
    t, h = line.strip('\r\n').split(',')
    time.append(float(t))
    height.append(float(h))

plt.scatter(time,height, marker="o", s=3)

x=time
y=height

params = ""
i = 0
while i in range(len(string.ascii_uppercase)):
    if string.ascii_uppercase[i] in equation:
        params += f",{string.ascii_uppercase[i]}"
    i+=1

exec(f"""
def func_to_fit(x{params}):
    return {equation}
""")

min_x = min(x) - padding_x
max_x = max(x) + padding_x

min_y = min(y) - padding_y
max_y = max(y) + padding_y

param, param_cov = curve_fit(func_to_fit, x, y, bounds=bounds)

print(param_cov)

fitted_func = "y="+equation
i=0
while i in range(len(string.ascii_uppercase)):
    if string.ascii_uppercase[i] in fitted_func:
        fitted_func=fitted_func.replace(string.ascii_uppercase[i],f"({round(param[i],3)} ± {round(sqrt(param_cov[i][i]),3)})")
        i+=1
    else:
        break

fitted_func=fitted_func.replace("**2","²")
fitted_func=fitted_func.replace("**","^")
fitted_func=fitted_func.replace("*","⋅")


polyline = np.linspace(min_x, max_x, num=100)
plotted = []
for x_point in polyline:
    plotted.append(eval(f"func_to_fit({x_point}, {','.join(map(str, param))})"))
plt.plot(polyline, plotted, c="#EE82EE", label=f"{fitted_func}\n")

plt.xlim([min_x, max_x])
plt.ylim([min_y, max_y])

plt.legend()
plt.title(f"{y_title} VS. {x_title}")
plt.xlabel(x_title)
plt.ylabel(y_title)
if figureImgFile:
    plt.savefig(figureImgFile)
plt.show()
