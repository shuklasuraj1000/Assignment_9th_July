class ineuron1:
    def __init__(self):
        self.__instructor = "Sudhanshu"                 #Private variable
        self._instructor2 = "Sudhanshu"

    def trainer(self):
        print(self.__instructor)
        print(self._instructor2)

a = ineuron1()
a.trainer()

# We can't over-write private variable value from outside of class,
# protected variable can be change but without knowing class and variable name is quite difficult.
# Variables are encapsulated inside class ineuron1.

print("\n "
      "After changing variable value")
a.__instructor = "Krish"
a._instructor2 = "Sunny"
a.trainer()




