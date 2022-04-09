class Matrix:
    def __init__(self, row, col, values):
        assert row*col==len(values),"number of values does not match rows and columns"
        self.row=row
        self.col=col
        self.raw_values=values
        self.max_digits=len(str(max([abs(v) for v in values]+[abs(10*v) for v in values if v<0])))
        #i feel proud for thinking of line above, takes into account the negative sign.
        print(self.max_digits)
        big_list=[]
        small_list=[]
        counter=0
        for _ in range(row):
            small_list=[]
            for _ in range(col):
                small_list.append(values[counter])
                counter+=1
            big_list.append(small_list)
        self.values=big_list
    def __str__(self):
        big_s=""
        for small_list in self.values:
            small_s="|"
            for v in small_list:
                small_s+=str(v).center(self.max_digits)
            small_s+="|\n"
            big_s+=small_s
        return big_s

m1=Matrix(3,3,[1,2,3,4,5,6,7,8,-100])
print(m1)