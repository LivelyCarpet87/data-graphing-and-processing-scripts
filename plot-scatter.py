#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 4:
    print(f"Please use: python3 {sys.argv[0]} [input_data.csv] [x axis title string] [y axis title string]")
    exit(1)

filename = sys.argv[1]
x_title = sys.argv[2]
y_title = sys.argv[3]

data_input_file = open(filename,'r')

lines = data_input_file.readlines()
legend_titles = lines.pop(0)
legend_titles = legend_titles.strip('\r\n').split(',')
num_samples = int(len(legend_titles)/2)

data = []
for i in range(num_samples):
    data.append( (legend_titles[2*i], [], []) )

for line in lines:
    line_data = line.strip('\r\n').split(',')
    for i in range(num_samples):
        try:
            x = float(line_data[2*i])
            y = float(line_data[2*i+1])
        except:
            continue
        data[i][1].append(x)
        data[i][2].append(y)

data_input_file.close()

fig, ax = plt.subplots()

for i in range(num_samples):
    label = data[i][0]
    x = data[i][1]
    y = data[i][2]
    ax.scatter(x, y, label=label, s=1)

plt.ylim([-0.1, 1.1])
plt.xlim([400, 750])
plt.legend()
plt.title(f"{y_title} VS. {x_title}")
plt.xlabel(x_title)
plt.ylabel(y_title)
plt.show()
