# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum


# calc_sum(5, 10)

# #more lines of code

# calc_sum(2, 10)
 
# #more lines ofcode

# calc_sum(12, 17)



#function defintion
# 

#average of 3 numbers

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg


# calc_avg(4, 5, 10)

#qs1
# cities = ["delhi", "gurgoan", "pune", "gaya"]
# heroes = ["hanuman", "shiva", "krishna"]


# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
       

# print_list(heroes)


#qs3

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         print(fact)

# cal_fact(5)    


#qs4
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# converter(10 )    

#recursive function

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(8) 


# def fact(n):
#     if(n== 1 or n== 0):
#         return 1
#     return fact(n-1) * n

# print(fact(4))

#qs1
# def calc_sum(n):
#     if(n== 0):
#         return  0
#     return calc_sum(n-1) + n

# sum = calc_sum(10)
# print(sum)


 #qs2
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "litchi", "apple", "banan"]

print_list(fruits)
