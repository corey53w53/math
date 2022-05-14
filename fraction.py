def get_factors_list(num):
    if num == 1:
        return [1]
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
        self.num = abs(num)
        self.den = abs(den)
        self.negative = num*den < 0

    def simplify(self):
        negative = self.num*self.den < 0
        factor = gcf(abs(self.num), abs(self.den))
        self.num //= factor
        self.den //= factor
        if negative:
            self.num *= -1
        return self

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):

        return Fraction((self.num*other.den)+(other.num*self.den), self.den*other.den).simplify()

    def __sub__(self, other):
        return Fraction((self.num*other.den)-(other.num*self.den), self.den*other.den).simplify()

    def __mul__(self, other):
        return Fraction(self.num*other.num, self.den*other.den).simplify()

    def __truediv__(self, other):
        return self*other.reciprocol()

    def reciprocol(self):
        return Fraction(self.den, self.num)


f = Fraction(1, -2)
f1 = Fraction(1, 6)
for a in ["+", "-", "/", "*"]:
    exec("print(f" + a + "f1)")
