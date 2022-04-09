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
        print(big_list)
        self.values=big_list

#1 2
#3 4
matrix1=[[1,2],[3,4]]
#3 1
#1 0
matrix2=[[3,1],[1,0]]

m1=Matrix(3,3,[1,2,3,4,5,6,7,8,9])

l=[]
for r in matrix1:
    for c in r:
        pass
