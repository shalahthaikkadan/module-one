class Square:

    def __init__(self, length):
        self.length = length

    def area(self):
        result = self.length * self.length
        return result

    def perimeter(self):
        result = 4 * self.length
        return result


obj = Square(5)

print(obj.area())
print(obj.perimeter())
    