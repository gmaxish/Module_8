"""
Изменить класс "Дробь" следующим образом:
- все статические свойства классов должны должны изменяться только внутри классовых методов.
- выделить один или несколько вспомогательных методов (если это небыло сделано ранее) и оформить их в виде статических
методов.
"""


class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.proper_fr_count += 1
        else:
            cls.improper_fr_count += 1

    def set(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.inc_fr_count(numerator < denominator)

    def print(self):
        print('\u0332'.join(f'{self.numerator}  '))
        print(f'{self.denominator}')

    def get_reversed(self):
        print("The reversed fraction of")
        self.print()
        print("is:")
        rev_fr = Fraction()
        rev_fr.set(self.denominator, self.numerator)
        rev_fr.print()

    @staticmethod
    def get_nod(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def reduse(self):
        nod = Fraction.get_nod(self.numerator, self.denominator)
        if nod != 1:
            print("The fraction")
            self.print()
            print("after reduction is: ")
            self.set(self.numerator//nod, self.denominator//nod)
            self.print()
        else:
            print("Thr fraction")
            self.print()
            print("can't be redused!")
