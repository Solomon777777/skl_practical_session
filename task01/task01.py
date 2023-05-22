# import os

'''
word = "Lorem"
cnt = 0
lst = []

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if ".py" not in file:
            f = open(file, "r")
            for line in f.readlines():
                if word in line:
                    cnt = cnt + 1
            lst.append((file, cnt, os.path.getsize(file)))
            cnt = 0
            f.close()

max_no_of_occ = 0
max_size = 0

for i in range(len(lst)):
    if max_no_of_occ < lst[i][1]:
        max_no_of_occ = lst[i][1]
        max_size = lst[i][2]

g = open("output.txt", "w")
g.write("Numarul maxim de aparitii este: " + str(max_no_of_occ))
g.close()
'''

'''
def read_data(file):
   with open(file, "r") as f:
    data = []
    for line in f.readlines()[1:]:
        data.append(int(line.split(",")[1]))
    f.close()
    return data
def get_partial_sums(data):
    sums = [0]
    for i in range(1, len(data)+1):
        sums.append(sums[i-1] + data[i-1])
    return sums

file_data = read_data("input.txt")
sums = get_partial_sums(file_data)
'''

def read_data(file):
    with open(file, "r") as f:
        data = []
        for line in f.readlines()[1:]:
            data.append(int(line.split(",")[1]))
    return data

def get_partial_sums(data):
    sums = [0]
    for i in range(1, len(data)+1):
        sums.append(sums[i-1] + data[i-1])
    return sums

file_data = read_data("input.txt")
sums = get_partial_sums(file_data)
