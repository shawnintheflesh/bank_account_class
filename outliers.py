data = [2, 3, 125, 200, 365, 458, 525
        , 689, 783]

min_valid = 125
max_valid = 700

stop = 0

for index, value in enumerate(data):
        if value >= min_valid:
                stop = index
                break




print(stop)
del data[:stop]

start = 0
for index in range(len(data) -1, -1, -1):
        if data[index] <= max_valid:
                start = index + 1
                break
print(start)
del data[start:]
print(data)

