from math import h

class Fraction:

    def __init__(self, num:int, denom:int):
        try:
            self.num = num
            self.denom = denom
        except TypeError:
            print("Only integers are allowed!")

    def __str__(self):
        return f'{self.num} / {self.denom}'

    def __add__(self, other):
        if(other.denom != self.denom):
            first = self.num * other.denom
            second = other.num * self.denom
            bottom = self.denom * self.denom

            return f"{first + second} / {bottom}"
        else:
            return f"{other.num + self.num} / {self.denom}"

    def __sub__(self, other):
        if(other.denom != self.denom):
            first = self.num * other.denom
            second = other.num * self.denom
            bottom = self.denom * self.denom

            return f"{first - second} / {bottom}"
        else:
            return f"{other.num - self.num} / {self.denom}"

    def __mul__(self, other):
        return f"{self.num * other.num} / {self.denom * other.denom}"

    def __truediv__(self, other):
        return f"{self.num * other.denom} / {self.denom * other.num}"

    def __gt__(self, other):
        return (self.num / self.denom) > (other.num / other.denom) 
    
    def __ge__(self, other):
        if(self.num == other.num and self.denom == other.denom): return True
        return (self.num / self.denom) > (other.num / other.denom) 
    
    def __lt__(self, other):
        return (self.num / self.denom) < (other.num / other.denom) 
    
    def __le__(self, other):
        if(self.num == other.num and self.denom == other.denom): return True
        return (self.num / self.denom) < (other.num / other.denom)     

    def getNum(self):
        return self.num

    def getDenom(self):
        return self.denom

a = Fraction(3,4)
b = Fraction(1,3)

print(a > b)