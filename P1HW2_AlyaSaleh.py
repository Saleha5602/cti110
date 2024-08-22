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

#Write program Pseudocode (detail algorithm)
#and add it as a comment block to the submitted program. 
print('This Program Calculate the expenses')
user_num1=int(input("Enter Budgets:"))#A git test
user_num2=input("Enter your travel destination:")
user_num3=int(input("How much do you think you will spend on gas?"))
user_num4=int(input("Approximately, how much will you need for accomodation/hotel?"))
user_num5=int(input("Last, how much do you need for food?"))
print('Travel Expenses')
print('Location:',user_num2)
print('Budget:',user_num1)
print('Fuel:',user_num3)
print('accomodation:',user_num4)
print('food:',user_num5)
print(user_num1,'-',user_num3,'+',user_num4,'+',user_num5,'Remaining Balansce:',user_num3 + user_num4 + user_num5 - user_num1)
print('Remaining Balansce:',user_num3 + user_num4 + user_num5 - user_num1)






