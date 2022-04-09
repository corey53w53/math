class Matrix:
    def __init__(self, row, col, values):
        self.row=row
        self.col=col
        self.raw_values=values
        big_list=[]
        small_list=[]
        counter=0
        for r in range(row):
            small_list=[]
            for c in range(col):
                small_list.append(counter)
                counter+=1
            counter+=1
            big_list.append(small_list)
        self.values=big_list
    def __str__(self):
        s=""
        for small_list in self.values:
            s+=f'|{" ".join([str(a) for a in small_list])}|\n'
        return s

#|1 3 2|
#|3 4 4|
m1=Matrix(3,3,[1,2,3,4,5,6,7,8,9])
print(m1)