


### CTI-110
##
### P2HW2 - List
##
### Alya Saleh
##
### 6/22/2023
###Algorithm
##set a name for your list
##make each num a float.
##for this homework you should have six module in your list.
##after writing your list you should code the min,max,average,sum of your list.
##you have to use thir format to get an output.
##Then you are done.
### set variables
grade_list=[]

num1=float(input("Enter a grade for  Module 1:"))
grade_list.append(num1)               
num2=float(input("Enter a grade for  Module 2:"))
grade_list.append(num2)
num3=float(input("Enter a grade for  Module 3:"))
grade_list.append(num3)
num4=float(input("Enter a grade for  Module 4:"))
grade_list.append(num4)
num5=float(input("Enter a grade for  Module 5:"))
grade_list.append(num5)
num6=float(input("Enter a grade for  Module 6:"))
grade_list.append(num6)
minimum=min(grade_list)
print(minimum)
maximum=max(grade_list)
print(maximum)
sum1=sum(grade_list)
print(sum1)
average=sum(grade_list)/len(grade_list)
print(average)
print('----------Results----------')
print("Lowest Grade:     ",minimum)
print("Highest Grade:    ",maximum)
print("Sum of Grade:     ",sum1)
print("Average :         ",format(average,',.2f'))
print("-"*40)
print("pess any key to exit")
input()




