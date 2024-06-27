class Calc:
    def __init__(self,a,b):
       self.a=a
       self.b=b
    print("This is a calculator :")
    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

object_ref = Calc(3,4)
output = object_ref.sum()
print(output)
output = object_ref.sub()
print(output)
output = object_ref.mul()
print(output)
output = object_ref.div()
print(output)