num1=input("Enter the employee's" + ' name or "Done" to terminate: ')
count = 0  # number of employees
totalOvtPay = 0
regP=0
grossP=0
while num1.lower() != "done":
    count += 1
    
    
#print(" num1=input('Enter name of employee? ")
 
    num2=float(input('Enter number of hours the employee worked this week? '))
     
    num3=float(input("Enter employee's pay Rate? "))
     
    print('-'*40)
     
    print('Employee Name: ',num1)
     
    print()
     
    print('Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    gross_pay')
     
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
        
    totalOvtPay += overTime_pay
    regP +=  reg_pay
    grossP+= gross_pay
     
    print(f'{num2:<15.2f}{num3:<15.2f}{overTime_Hours:<15.2f}{overTime_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<10.2f}')
     
##    print('Employee Name: ',num1)
##     
##    print()
##     
##    pay=(overTime_pay)
##     
##    print("The amount paid for Overtime is : $",pay )
##     
##    print()
##     
##    regP=(reg_pay)
##     
##    print("The amount paid for regular hours : $",regP )
##     
##    print()
##     
##    grossP=(gross_pay)
##     
##    print("The amount paid in gross : $",grossP )
     
    print()
     
    num1=input("Enter the employee's" + ' name or "Done" to terminate: ' )
print("Ttoal number of employees entered:", count)
print("Ttoal amount paid for overtime:  $", totalOvtPay)
print("Ttoal amount paid for regular hours : $",regP)
print("Ttoal amount paid in gross : $ ",grossP)


