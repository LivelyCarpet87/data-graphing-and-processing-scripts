import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

filename = input("Please enter filename in local directory:")
fit_deg = int(input("Please enter the degree of polynomial to fit [1,2]:"))
padding_x = float(input("Please enter the amount of padding for x direction:"))
padding_y = float(input("Please enter the degree of padding for y direction:"))
figureImgFile = input("Please enter the filename to save to [ENTER to skip]:")

file = open(filename,'r')

lines = file.readlines()
titles = lines.pop(0)
x_title, y_title = titles.strip('\r\n').split(',')
x = []
y = []
for line in lines:
    x_val, y_val = line.strip('\r\n').split(',')
    x.append(float(x_val))
    y.append(float(y_val))

plt.scatter(x,y, marker="o", s=3)

m, v = np.polyfit(x, y, fit_deg, cov="true")
if fit_deg == 1:
    fitted_func = f"y=({round(m[0],3)}±{round(sqrt(v[0][0]),4)})x + ({round(m[1],4)}±{round(sqrt(v[1][1]),5)})"
    print(fitted_func)
elif fit_deg == 2:
    fitted_func = f"y=({round(m[0],3)}±{round(sqrt(v[0][0]),3)})x² + ({round(m[1],3)}±{round(sqrt(v[1][1]),3)})x + ({round(m[2],3)}±{round(sqrt(v[2][2]),3)})"
    print(fitted_func)

model= np.poly1d(np.polyfit(x, y, fit_deg))

yhat = model(x)
ybar = np.sum(y)/len(y)
ssreg = np.sum((yhat-ybar)**2)
sstot = np.sum((y - ybar)**2)
r_squared = ssreg / sstot
print('r_squared', r_squared)

sig_fig = 3
rounded_r_squared = 1
while sig_fig <= 10 and (rounded_r_squared == 1 or str(rounded_r_squared)[-1] == "9"):
    rounded_r_squared = round(r_squared,sig_fig)
    sig_fig += 1

print(sig_fig, rounded_r_squared)

min_x = min(x) - padding_x
max_x = max(x) + padding_x

min_y = min(y) - padding_y
max_y = max(y) + padding_y

polyline = np.linspace(min_x, max_x, num=100)
plt.plot(polyline, model(polyline), c="#EE82EE", label=f"{fitted_func}\nR²≈{rounded_r_squared}")
print(model)

plt.xlim([min_x, max_x])
plt.ylim([min_y, max_y])

plt.legend()
plt.title(f"{y_title} VS. {x_title}")
plt.xlabel(x_title)
plt.ylabel(y_title)
if figureImgFile:
    plt.savefig(figureImgFile)
plt.show()
