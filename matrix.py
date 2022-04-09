class Matrix:
    def __init__(self, row, col, values):
        assert (row*col==len(values)),"number of values does not match rows and columns"
        self.row=row
        self.col=col
        self.raw_values=values

        big_list=[]
        counter=0
        for _ in range(row):
            small_list=[]
            for _ in range(col):
                small_list.append(values[counter])
                counter+=1
            big_list.append(small_list)
        self.values=big_list
        list_rows=[]
        for r in self.values:
            small_list=[]
            for c in r:
                small_list.append(c)
            list_rows.append(small_list)
        self.list_rows=list_rows
        list_cols=[]
        
        for c in range(self.col):
            small_list=[]
            for r in range(self.row):
                small_list.append(list_rows[r][c])
            list_cols.append(small_list)
        self.list_cols=list_cols
        self.max_digits=len(str(max([v for v in values]+[abs(10*v) for v in values if v<0])))
        #i feel proud for thinking of line above, takes into account the negative sign.
        self.max_digits_list=[len(str(max([v for v in c]+[abs(10*v) for v in c if v<0]))) for c in list_cols]
    def __str__(self):
        big_s=""
        for small_list in self.values:
            small_s="|"
            counter=0
            while counter<len(small_list):
                if counter==0:
                    small_s+=str(small_list[counter]).ljust(self.max_digits_list[counter]+1)
                    counter+=1
                elif counter==len(small_list)-1:
                    small_s+=str(small_list[counter]).rjust(self.max_digits_list[counter]+1)
                    counter+=1
                else:
                    small_s+=str(small_list[counter]).center(self.max_digits_list[counter])
                    counter+=1
            big_s+=small_s+"|\n"
        return big_s
    def __add__(self,m2):
        assert (self.col==m2.col and self.row==m2.row),"columns or rows are not equal"
        return Matrix(self.row,self.col,[(self.raw_values[c]+m2.raw_values[c]) for c in range(len(self.raw_values))])
    def __sub__(self,m2):
        assert (self.col==m2.col and self.row==m2.row),"columns or rows are not equal"
        return Matrix(self.row,self.col,[(self.raw_values[c]-m2.raw_values[c]) for c in range(len(self.raw_values))])
    def __mul__(self,m2):
        assert (self.col==m2.row), "number of columns in first matrix does not equal number of rows in second matrix"
        raw_values=[]
        for row in self.list_rows:
            for col in m2.list_cols:
                raw_values.append(sum([row[c]*col[c] for c in range(self.col)]))
        return Matrix(self.row,m2.col,raw_values)
        
# m1=Matrix(3,3,[2,2,3,4,5,100,7,8,-10])
# m2=Matrix(3,3,[1,2,3,4,5,6,7,8,9])
# print(m1*m2)
m3=Matrix(2,3,[10000,2,300000,40,50000,6])
m4=Matrix(3,2,[10,11,20,21,30,3001])
print(m3*m4)
#10 11
#
print(m3)
print(m4)