# A brief description of the project
#This program will help the user to know if they will have a Remaining
# from Their Budget amount or not.
# Date: 6/9/2023
# CTI-110 P1HW2 - Travel Expense
# Alya Saleh
# Algorithm :
# 1- Enter your Budget, 2- Enter your destination, 3- Enter your spendings on gas
# 4- Enter your accomodation,5- Enter your spendings on food.
# 6- Add all the expenses and Subtract it from budget.
# You have to format your results to float.
print('This Program Calculates the expenses')
print()
user_num1=int(input("Enter Budget:"))
print()
user_num2=input("Enter your travel destination:")
print()
user_num3=int(input("How much do you think you will spend on gas?"))
print()
user_num4=int(input("Approximately, how much will you need for accomodation/hotel?"))
print()
user_num5=int(input("Last, how much do you need for food?"))
print()
print('----------Travel Expenses----------')
print('Location:',user_num2)
print('Budget:','$', format(user_num1,',.1f'))
print('Fuel:','$', format(user_num3,',.1f'))
print('accomodation:','$', format(user_num4,',.1f'))
print('food:','$', format(user_num5,',.1f'))
print('Remaining Balansce:','$',user_num1 -(user_num3 + user_num4 + user_num5))
print("Press any key to exit")
input()
