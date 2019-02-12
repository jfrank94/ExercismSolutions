from __future__ import division
import math

class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise Exception('No division by zero!')
        self.numer = numer
        self.denom = denom
        if self.gcd(numer, denom) != 1:
           self.numer, self.denom = self.reduced_rational(numer, denom)


    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def reduced_rational(self, a, b):
        a, b = int(a), int(b)
        gcd = self.gcd(a, b)
        print(a, b)
        if gcd != 1:
            new_numer = a/gcd
            new_denom = b/gcd
            return int(new_numer), int(new_denom)
        else:
            return a, b

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        res = (a * b)//self.gcd(a, b)
        return res

    def __add__(self, other):
        lcm_denom = self.lcm(self.denom, other.denom)
        res_numer = ((lcm_denom/self.denom) * self.numer) + ((lcm_denom/other.denom) * other.numer)
        res_numer, res_denom = self.reduced_rational(res_numer, lcm_denom)
        return Rational(res_numer, res_denom)

    def __sub__(self, other):
        if self.numer - other.numer == 0:
            return Rational(0, 1)
        lcm_denom = self.lcm(self.denom, other.denom)
        res_numer = ((lcm_denom/self.denom) * self.numer) - ((lcm_denom/other.denom) * other.numer)
        res_numer, res_denom = self.reduced_rational(res_numer, lcm_denom)
        return Rational(res_numer, res_denom)

    def __mul__(self, other):
        res_numer, res_denom = self.reduced_rational(self.numer * other.numer, self.denom * other.denom)
        return Rational(res_numer, res_denom)

    def __truediv__(self, other):
        res_numer = self.numer * other.denom
        res_denom = self.denom * other.numer
        if res_numer < 0 and res_denom < 0:
            res_numer *= -1
            res_denom *= -1
        res_numer, res_denom = self.reduced_rational(res_numer, res_denom)
        return Rational(res_numer, res_denom)

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return Rational(self.numer, self.denom)

    def __pow__(self, power):
        res_numer = self.numer ** power
        res_denom = self.denom ** power
        return Rational(res_numer, res_denom)

    def __rpow__(self, base):
        res_exp = self.numer / self.denom
        return base ** res_exp
