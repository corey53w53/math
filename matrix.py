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
            for c in r: small_list.append(c)
            list_rows.append(small_list)
        self.list_rows=list_rows
        list_cols=[]
        for c in range(self.col):
            small_list=[]
            for r in range(self.row): small_list.append(list_rows[r][c])
            list_cols.append(small_list)
        self.list_cols=list_cols
        self.max_digits_list=[len(str(max([v for v in c]+[abs(10*v) for v in c if v<0]))) for c in list_cols]
    def __str__(self):
        big_s_list=[]
        for small_list in self.values:
            small_s="|"
            counter=0
            while counter<len(small_list):
                small_s+=str(small_list[counter]).center(self.max_digits_list[counter]+1)
                counter+=1
            big_s_list.append(small_s)
        while all([s[-1]==' ' for s in big_s_list]): big_s_list=[b[:-1] for b in big_s_list]
        big_s=""
        for s in big_s_list: big_s+=s+"|\n"
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
            for col in m2.list_cols: raw_values.append(sum([row[c]*col[c] for c in range(self.col)]))
        return Matrix(self.row,m2.col,raw_values)
    def det(self):
        assert self.col==self.row, "not a square matrix"
        if self.col==self.row==2:
            return self.raw_values[0]*self.raw_values[3]-self.raw_values[1]*self.raw_values[2]
        else:
            sum=0
            for counter in range(self.row):
                m=self.minor(counter)
                if not counter%2:
                    sum+=self.list_rows[0][counter]*m.det()
                else:
                    sum-=self.list_rows[0][counter]*m.det()
                counter+=1
            return sum
    def minor(self,col_num, row_num=0):
        assert col_num<self.col,"col_num argument is too large"
        assert row_num<self.col,"row_num argument is too large"
        raw_values_list=[]
        for r in range(self.row):
            for c in range(self.col):
                if c!=col_num and r!=row_num:
                    raw_values_list.append(self.raw_values[self.col*r+c])
        return Matrix(self.row-1,self.col-1,raw_values_list)
# m1=Matrix(3,3,[1,2,3,4,5,6,7,8,9])
# print(m1)
# print(m1.minor(1))

#1 2 3
#4 5 6
#7 8 9
m2=Matrix(3,3,[1,2,1,4,5,6,7,8,9])
print(m2)
print(m2.det())
# print(m1)
# print(m2)
# print(m1*m2)
#TODO
#find way to calc determinant
#find way to calc inverse