# i = 1
# while i <= 10000 :
#   print("college", i)
# i+=1
# a = int("2")
# b = 4.24

# print(type(a))
# print(a + b)

#qs2
# i = 100
# while i >= 1: #stopping condition
#     print(i)
#     i -= 1

    #qs3(type)
# i = 1
# while i <= 10:
#     print(5 * i)
#     i += 1  

#qs3 actually 
# n = int(input("enter number :"))
# i = 1
# while i <=10:
#     print(n*i)
#     i +=1

#qs4
# nums =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print([idx])
#     idx += 1
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])

#heroes = ["hanuman", "ram", "krishnan", "shiva"]

#traverse
# i = 0
# while i < len(heroes):
#     print(heroes[i])
#     i += 1

#nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("FOUND at idx", i)
#         break
#     else:
#         print("founding..")
#     i +=1     

# print("end of loop")

# i = 0
# while i <= 10:
#     if(i%2 == 0): #(i%2 != 0) for odd number
#         i +=1
#         continue #skip
#     print(i)
#     i += 1

# veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]


# for val in veggies:
#     print(val)

# tup =(1, 2, 3 , 6)

# for num in tup:
#     print(num)

# str = "apnacollege"

# for char in str:
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)
# else:
#     print("END")   
 

# nums =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
# x = 49

# idx = 0
# for el in nums:
#     if(el == x): 
#         print("number found at idx", idx)
#     idx += 1

# seq = range(12) #range(stop)

# for i in seq:
#     print(i)

# 
# for i in range(1, 101, 3):
#     print(i)

# for i in range(1, 101):
#     print(i)

# for i in range (100, 0, -1):
#     print(i)

#qs3
# n = int(input("entr number :"))

# for i in range(1, 14):
#     print(n * i)    


# n = 5 

# sum = 0

# for i in range (1, n+1):
#     sum += i

#     print("total sum =", sum)

# n = 7 
# sum = 0
# i = 1
# while i  <=n:
#     sum += 1

# print("total sum =", sum)    

#qs 2 factorial question

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i 
#     i += 1

#     print("factorial =", fact)

#By using for
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

    print("factorial =", fact)      