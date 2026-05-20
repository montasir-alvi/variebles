#def function_name(parameters):
#    #code block
#   return result
# def myfun():
#     print("Hello World")
# myfun()#fhifgzhlogjfoghiou;f
# myfun()#fhifgzhlogjfoghiou;f
# myfun()#fhifgzhlogjfoghiou;f
# myfun()#fhifgzhlogjfoghiou;f
# myfun()#fhifgzhlogjfoghiou;f
# myfun()#fhifgzhlogjfoghiou;f
# # myfun()#fhifgzhlogjfoghiou;f
# def add(a,b):
#     return a+b
# print(add(21,3))
# print(add(27,34))
# print(add(2,636))
# print(add(24,31))
# import math
# print(math.pi)
# def sum_odd_numbers():
#     sum = 0
#     for i in range(1,101,2):   #1,3,5,.....999...
#         sum += i
#     return sum
# result = sum_odd_numbers()
# print("sum of odd numbers from 1 to 100 =", result)
# import math
# def circle():
#     r = float(input("Enter Your Circle Radius: "))
#     Area = math.pi*r**2
#     print("Your Circle Area is", Area)
# circle()
# def sum_list():
#     sum = 0
#     for i in num_list:
#         sum += i
#     return sum
# # list of 5 numbers
# num_list= [10,20,30,40,50]
# result =sum_list()
# print("Sum =", result)
# fruits = ["apple","banana","cherry"]
# print(fruits[2])
# name = "Montasir Alvi"                    #str
# college = "Dhaka Polytechnic Institute"   #str
# dream_company = "ALVOS"                   #str
# print(name)
# print(college)
# print(dream_company)
# Create variables for your age, year of birth, and how many hours you study per day. Calculate how many hours you'll study in a full year.
# Age = 18
# Year_of_birth = 2008
# Study_hours_in_a_day = 3
# print(Age)
# print(Year_of_birth)
# print(Study_hours_in_a_day*365)
# import math
# print(round(math.pi, 3))
# The Mercedes Deal
# You want to buy a Mercedes that costs $85,000.
# The showroom is giving a 15% discount.
# Write a program that:

# Stores the car price as a float
# Stores the discount percentage as a float
# Calculates the discount amount
# Calculates the final price after discount
# Prints the result like this:
# car_price = 85000
# discount = 0.15
# print("car price =", car_price)
# print("discount =", car_price*discount)
# print("final price =", car_price - (car_price*discount))
# The Phone Shop
# You want to buy an iPhone that costs $999.99.
# There are 2 discounts:
# Student discount: 10%
# Eid sale discount: 5%
# Both discounts apply one after the other — first the student discount, then the Eid sale discount on the already discounted price.
# Write a program that:
# Stores the original price as a float
# Stores both discounts as floats
# Calculates price after student discount
# Calculates final price after Eid discount
original_price = 999.99
student_discount = 0.1
eid_discount = 0.05
student_discount_save = original_price*student_discount
discount_save = original_price*eid_discount
costomer_need_to_pay = original_price-discount_save
student_need_to_pay = original_price-student_discount_save
in_eid_student_need_to_pay =student_need_to_pay-(student_need_to_pay*eid_discount)
print("costomer need to pay =",costomer_need_to_pay,"dollars")
print("student need to pay =",in_eid_student_need_to_pay,"dollars")