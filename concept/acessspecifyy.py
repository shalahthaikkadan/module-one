class Detail():

    def __init__(self,name,age,password):
        self.name=name
        self._age=age
        self.__password=password

    def show_password(self):
        return f'password {self.__password}'

obj=Detail('Shalah',22,12345)
print(obj.name)
print(obj._age)
print(obj.show_password())