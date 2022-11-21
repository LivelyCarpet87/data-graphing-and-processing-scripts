import os

print("Please enter filename in local directory...")
filename = input("> ")
print("Please enter the extraction pattern, where 'x' is for a column to discard and '_' is for a column to keep...")
print("eg. To keep only the 3rd and 4th column out of 5 columns, use: x x _ _ x")
extraction_pattern_str = input("> ")

extraction_pattern = []
for char in extraction_pattern_str:
    if char == "x":
        extraction_pattern.append(False)
    elif char == "_":
        extraction_pattern.append(True)

file = open(filename,'r')
raw_data = []
lines = file.readlines()
for line in lines:
    raw_data.append(line.strip('\r\n').split(','))

if  len(raw_data[0]) % len(extraction_pattern) != 0:
    print("Extraction pattern does not match data.")
    exit()

trials = []
for i in range(0,int(len(raw_data[0]) / len(extraction_pattern))):
    trials.append([])

for row in raw_data:
    trial_num = 0
    trial_row = []

    col = 0

    for item in row:
        if extraction_pattern[col]:
            trial_row.append(item)
        col += 1
        if col == len(extraction_pattern):
            trials[trial_num].append(trial_row)
            col = 0
            trial_row = []
            trial_num += 1
            if trial_num == len(trials):
                trial_num = 0

os.mkdir("data")

trial_rows = []
for trial in trials:
    trial_name = trial[0][0]
    trial.pop(0)
    for row in trial:
        row_csv = ",".join(row)
        if row_csv.strip(",") != "":
            trial_rows.append(row_csv)
    trial_csv = '\n'.join(trial_rows)
    trial_rows = []

    file = open(os.path.join("data",f"{trial_name}.csv"), "w")
    file.write(trial_csv)
    file.close

print(f"Processed {len(trials)} trials into data folder")