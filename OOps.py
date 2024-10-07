# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database..")


# s1 = Student("karan", 97)  
# print(s1.name, s1.marks)


# s2 = Student("arjun", 88)
# print(s2.name, s2.marks) 

#qs1

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi", self.name, "your avg score is:", sum/3)    

# s1 = Student("karan", [88,36, 56])  
# s1.get_avg()



# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance = ", self.get_balance())
            

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was crediteed")
#         print("total balance = ", self.get_balance()) 

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000, 12345)
# acc1.credit(1000)
# acc1.debit(500)       



# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("shradha")
# print(s1.name)
# del s1.name
# print(s1.name)


# class Car:
#     @staticmethod
#     def start():
#         print("car started..")


#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand


# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type        


# car1 = Fortuner("diesel")
# car1.start(  )
       

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img


#     def showNumber(self):
#         print(self.real, "i +",self.img, "j")

#     def add(sself, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber() 


#qs1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 22/7 * self.radius ** 2

#     def perimeter(self):
#         return 2 * 22/7 * self.radius


# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())          


#Qs2

   