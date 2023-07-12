# CTI-110

# P3HW2 - Salary

# Your Name
#Alya Saleh

# Date
#6/29/2023
#algorithm : This program calculate the employee's Salary(Hours Worked,Pay Rate,OverTime,OverTime Pay, and RegHour Pay)
num1=input('Enter name of employee? ')
num2=float(input('Enter number of hours the employee worked this week? '))
num3=float(input("Enter employee's pay Rate? "))
print('-'*40)
print('Employee Name:   ',num1)
print()
print('Hours Worked    Pay Rate     OverTime     OverTime Pay     RegHour Pay')
print('-'*80)
if num2 > 40 :
    overTime_Hours= num2 - 40
    overTime_rate= num3 * 1.5
    overTime_pay=overTime_Hours * overTime_rate
    reg_pay=num3 * 40
    gross_pay=overTime_pay + reg_pay
else:
    overTime_Hours= 0.0
    overTime_rate= 0.0
    overTime_pay= 0.0
    reg_pay= num3 * num2
    gross_pay= reg_pay
print(f'{num2:<15.2f}{num3:<15.2f}{overTime_Hours:<15.2f}{overTime_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<10.2f}')
print('-'*40)
print('press any key to exit')
input()
#I'm keeping this so I don't forget how to do different format.
##if num2 > 40 :
##    overTime_Hours= num2 - 40
##    overTime_rate= num3 * 1.5
##    overTime_pay=overTime_Hours * overTime_rate
##    reg_pay=num3 * 40
##    gross_pay=overTime_pay + reg_pay
##else:
##    overTime_Hours= 0.0
##    overTime_rate= 0.0
##    overTime_pay= 0.0
##    reg_pay= num3 * num2
##    gross_pay= reg_pay
##print(overTime_Hours)
###print(overTime_rate)
##print(overTime_pay)
##print(reg_pay)
##print(gross_pay)
