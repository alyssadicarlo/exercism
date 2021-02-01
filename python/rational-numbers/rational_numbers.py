from __future__ import division

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        reduced_self = self.reduce(self.numer, self.denom)
        reduced_other = self.reduce(other.numer, other.denom)
        if (reduced_self.numer == reduced_other.numer and reduced_self.denom == reduced_other.denom):
            return True
        else:
            return False

    def __repr__(self):
        reduced = self.reduce(self.numer, self.denom)
        self.numer = reduced.numer
        self.denom = reduced.denom
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numerator = self.numer * other.denom + other.numer * self.denom
        denominator = self.denom * other.denom
        return self.reduce(numerator, denominator)

    def __sub__(self, other):
        numerator = (self.numer * other.denom - other.numer * self.denom)
        denominator = (self.denom * other.denom)
        return self.reduce(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numer * other.numer
        denominator = self.denom * other.denom
        return self.reduce(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numer * other.denom
        if other.numer * self.denom == 0:
            raise ValueError("Dividing by 0")
        else:
            denominator = other.numer * self.denom
        return self.reduce(numerator, denominator)

    def __abs__(self):
        numerator = abs(self.numer)
        denominator = abs(self.denom)
        return Rational(numerator, denominator)

    def __pow__(self, power):
        if power == 0:
            return Rational(1,1)
        elif power > 0:
            numerator = self.numer
            denominator = self.denom
            for _ in range(1,power):
                numerator *= self.numer
                denominator *= self.denom
        elif power < 0:
            numerator = self.denom
            denominator = self.numer
            for _ in range(1,abs(power)):
                numerator *= self.denom
                denominator *= self.numer
        return self.reduce(numerator, denominator)

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)

    def reduce(self, numerator, denominator):
        if numerator == 0:
            return Rational(0,1)
        gcf = 0
        for i in range(1,abs(numerator)+abs(denominator)):
            if numerator % i == 0 and denominator % i == 0:
                gcf = i
        if gcf != 0:
            numerator = numerator/gcf
            denominator = denominator/gcf
        if (numerator < 0 and denominator < 0) or (numerator > 0 and denominator < 0):
            return Rational(int(-numerator), int(-denominator))
        return Rational(int(numerator), int(denominator))