#code
name = "Montasir Alvi"                    #str
college = "Dhaka Polytechnic Institute"   #str
dream_company = "ALVOS"                   #str
print(name)
print(college)
print(dream_company)
# Create variables for your age, year of birth, and how many hours you study per day. Calculate how many hours you'll study in a full year.
#code
Age = 18                   #int
Year_of_birth = 2008       #int
Study_hours_in_a_day = 3   #int
print(Age)
print(Year_of_birth)
print(Study_hours_in_a_day*365)
import math
print(round(math.pi, 3))

# The Mercedes Deal
# You want to buy a Mercedes that costs $85,000.
# The showroom is giving a 15% discount.
# Write a program that:
# Stores the car price as a float
# Stores the discount percentage as a float
# Calculates the discount amount
# Calculates the final price after discount
# Prints the result like this:
#code
car_price = 85000
discount = 0.15                      #float
print("car price =", car_price)
print("discount =", car_price*discount)
print("final price =", car_price - (car_price*discount))

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
original_price = 999.99 #float
student_discount = 0.1  #float
eid_discount = 0.05     #float
#code
student_discount_save = original_price*student_discount
discount_save = original_price*eid_discount
costomer_need_to_pay = original_price-discount_save
student_need_to_pay = original_price-student_discount_save
in_eid_student_need_to_pay =student_need_to_pay-(student_need_to_pay*eid_discount)
print("costomer need to pay =",costomer_need_to_pay,"dollars")
print("student need to pay =",in_eid_student_need_to_pay,"dollars")
