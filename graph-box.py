import matplotlib.pyplot as plt

filename = input("Please enter filename in local directory:")
title = input("Please enter title of graph:")
ylabel = input("Please enter Y label of graph:")
figureImgFile = input("Please enter the filename to save to [ENTER to skip]:")

file = open(filename,'r')

lines = file.readlines()
labels = lines.pop(0)
xsticklabels = labels.strip('\r\n').split(',')

file.close()

data = []

for _ in range(0, len(xsticklabels)):
    data.append([])

for line in lines:
    row = line.strip('\r\n').split(',')
    for i in range(0, len(row)):
        if row[i] != "":
            data[i].append(float(row[i]))

fig = plt.figure(figsize =(7, 7))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist = True, vert = 1)


# x-axis labels
ax.set_xticklabels(xsticklabels)

# Adding titles
plt.title(title)
plt.ylabel(ylabel)

if figureImgFile:
    plt.savefig(figureImgFile)

# show plot
plt.show()
