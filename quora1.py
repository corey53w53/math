l=[12, 15, 18, 21, 24, 30, 36]
target=102
for n in range(128):
    i = str(bin(n)).split("b")[1]
    while len(i)!=len(l):
        i = "0"+i
    num_list=[]
    for c in range(len(l)):
        if i[c]=="1": num_list.append(l[c])
    if sum(num_list)==target: print(num_list)



    