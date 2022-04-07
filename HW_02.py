"""
Измените класс "Дробь" следующим образом:
- свойства класса - числитель и знаменатель - должны быть динамическими и определяться внутри нового метода,
задающего значения дроби.
- добавьте 2 статических свойства - количество правильных и не правильных дробей, - которые должны отображать количество
созданных объектов класса соответствующих типов.
"""


class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    def set(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        if numerator < denominator:
            Fraction.proper_fr_count += 1
        else:
            Fraction.improper_fr_count += 1

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

    def reduse(self):
        a = self.numerator
        b = self.denominator
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        if a != 1:
            print("The fraction")
            self.print()
            print("after reduction is: ")
            self.set(self.numerator//a, self.denominator//a)
            self.print()
        else:
            print("Thr fraction")
            self.print()
            print("can't be redused!")


f1 = Fraction()
f1.set(5, 45)
f1.print()
f1.get_reversed()
f1.reduse()

f1.set(5, 15)
f1.reduse()

print(f'Proper fraction count: {Fraction.proper_fr_count}')
print(f'Proper fraction count: {Fraction.proper_fr_count}')