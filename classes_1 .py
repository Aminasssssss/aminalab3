#1. Define a class which has at least two methods:
#`getString`: to get a string from console input
#`printString`: to print the string in upper case.
class MyString:
    def getString(self):
        self.input_string = input()
    
    def printString(self):
        print(self.input_string.upper())
obj = MyString()
obj.getString()
obj.printString()
