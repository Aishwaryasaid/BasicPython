# open command doesn't opens the file. it is a file handler
fh = open(filename, mode='r')

list_1 = ["from: 0.8450","Hi","Hello","from: 0.4897","from: 0.5897","from: 0.6897","from: 0.7897","from: jan2"]
total = 0
count = 0
for list2 in list_1:
    if list2.startswith("from:"):
        count += 1
        list3 = list2
        abc = list3.find("from")
        list4 = list3.find(":",abc)
        list5 = list3[5:]
        print(list5)
