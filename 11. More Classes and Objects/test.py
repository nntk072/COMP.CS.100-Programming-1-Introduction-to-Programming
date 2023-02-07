class weight:
  def __init__(self, weight):
    self. weight= weight
  def __lt__(self,other):
    return self.weight<other.weight
  def __gt__(self,other):
    return self.weight>other.weight
a=weight(50)
b=weight(60)
c=weight(70)
print(a<b)
print(a>b)

"""
>>> frac1 = Fraction(1, 2)
>>> frac2 = Fraction(2, 3)
>>> frac1 < frac2
True
>>> frac1 > frac2
False
"""