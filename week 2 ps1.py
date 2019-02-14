# Paste your code into this box
minimum_pay = 0
monthlyPaymentRate = 0.04
balance = 484
annualInterestRate = 0.2
for i in range(12):
    minimum_pay = round(monthlyPaymentRate*balance,2)
    #print(minimum_pay)
    unpaidbal = round((balance - minimum_pay),2)
    #print(unpaidbal)
    balance = round(unpaidbal+((unpaidbal*annualInterestRate)/12),2)
    #print(balance)
    #print('Remaining Balance '+str(round(balance,2)))
    #print(minimum_pay,unpaidbal,balance)

print('Remaining Balance '+str(round(balance,2)))
