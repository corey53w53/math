from matplotlib.pyplot import get


def get_factors_list(num):
    factor_list = []
    for counter in range(1, 1+num//2):
        if num % counter == 0.0:
            factor_list += [counter, num//counter]
    return sorted(list(set(factor_list)))


def gcf(a, b):
    a_list = get_factors_list(a)
    b_list = get_factors_list(b)
    for num in reversed(a_list):
        if num in b_list:
            return num


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def simplify(self):
        factor = gcf(self.num, self.den)
        self.num //= factor
        self.den //= factor
        return self

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        return Fraction((self.num*other.den)+(other.num*self.den), self.den*other.den).simplify()


f = Fraction(3, 6)
f1 = Fraction(6, 6)
print(f+f1)
