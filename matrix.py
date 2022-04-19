import random


class Matrix:
    def __init__(self, row, col, values):
        assert (row*col == len(values)
                ), "number of values does not match rows and columns"
        self.row = row
        self.col = col
        self.raw_values = values
        self.list_rows = []
        for r in range(row):
            small_list = []
            for c in range(col):
                small_list.append(values[r*self.col+c])
            self.list_rows.append(small_list)
        self.list_cols = []
        for c in range(self.col):
            small_list = []
            for r in range(self.row):
                small_list.append(self.list_rows[r][c])
            self.list_cols.append(small_list)

    def __str__(self):
        big_s_list = []
        self.max_digits_list = [max([len(str(v)) for v in col])
                                for col in self.list_cols]
        for small_list in self.list_rows:
            small_s = ""
            counter = 0
            while counter < len(small_list):
                small_s += str(small_list[counter]
                               ).center(self.max_digits_list[counter]+2)
                counter += 1
            big_s_list.append(small_s)
        while all([s[-1] == ' ' for s in big_s_list]):
            big_s_list = [b[:-1] for b in big_s_list]
        while all([s[0] == ' ' for s in big_s_list]):
            big_s_list = [b[1:] for b in big_s_list]
        big_s = ""
        for s in big_s_list:
            big_s += "|"+s+"|\n"
        return big_s

    def __add__(self, m2):
        assert (self.col == m2.col and self.row ==
                m2.row), "columns or rows are not equal"
        return Matrix(self.row, self.col, [(self.raw_values[c]+m2.raw_values[c]) for c in range(len(self.raw_values))])

    def __sub__(self, m2):
        assert (self.col == m2.col and self.row ==
                m2.row), "columns or rows are not equal"
        return Matrix(self.row, self.col, [(self.raw_values[c]-m2.raw_values[c]) for c in range(len(self.raw_values))])

    def __mul__(self, m2):
        assert (self.col == m2.row), "number of columns in first matrix does not equal number of rows in second matrix"
        raw_values = []
        for row in self.list_rows:
            for col in m2.list_cols:
                raw_values.append(sum([row[c]*col[c]
                                  for c in range(self.col)]))
        return Matrix(self.row, m2.col, raw_values)

    def minor(self, row_num, col_num):
        assert col_num < self.col, "col_num argument is too large"
        assert row_num < self.col, "row_num argument is too large"
        raw_values_list = []
        for r in range(self.row):
            for c in range(self.col):
                if c != col_num and r != row_num:
                    raw_values_list.append(self.raw_values[self.col*r+c])
        return Matrix(self.row-1, self.col-1, raw_values_list).det()

    def det(self):
        assert self.col == self.row, "not a square matrix"
        if self.col == self.row == 1:
            return self.raw_values[0]
        elif self.col == self.row == 2:
            return self.raw_values[0]*self.raw_values[3]-self.raw_values[1]*self.raw_values[2]
        else:
            sum = 0
            for counter in range(self.row):
                if counter % 2:
                    sum -= self.list_rows[0][counter]*self.minor(0, counter)
                else:
                    sum += self.list_rows[0][counter]*self.minor(0, counter)
            return sum

    def transpose(self):
        big_list = []
        for counter in range(len(self.list_cols)):
            small_list = []
            for l in self.list_rows:
                small_list.append(l[counter])
            big_list += small_list
        return Matrix(self.col, self.row, big_list)

    def sign_rule(self):
        assert self.col == self.row, "not a square matrix"
        new_raw_value_list = []
        for r in range(self.row):
            for c in range(self.col):
                if (r+c) % 2:
                    new_raw_value_list.append(-self.list_rows[r][c])
                else:
                    new_raw_value_list.append(self.list_rows[r][c])
        return Matrix(self.row, self.col, new_raw_value_list)

    def cofactor(self):
        assert self.col == self.row, "not a square matrix"
        return Matrix(self.row, self.col, [self.minor(r, c) for r in range(self.col) for c in range(self.row)]).sign_rule()

    def adjoint(self):
        m = self.cofactor()
        return m.transpose()

    def inverse(self, r=2):
        """ param r: number of decimals to round to """
        m = self.adjoint()
        new_raw_values = [round(value/self.det(), r)
                          for value in m.raw_values]
        return Matrix(self.row, self.col, new_raw_values)

    def sum(self):
        return sum(self.raw_values)


def random_matrix(rows=3, cols=3, min=0, max=3):
    rand_list = []
    for _ in range(rows*cols):
        rand_list.append(random.randint(min, max))
    return Matrix(rows, cols, rand_list)


m1 = Matrix(3, 3, [-1.11, 2, 3, 4, 5, 6, 7, 8, 10])
m2 = random_matrix(5, 5)
print(m2)
print(m2.inverse())
