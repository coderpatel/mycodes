balance = 4773
annualInterestRate = 0.2
monthlyrate = annualInterestRate/12
lower = balance/12
upper = pow((balance+balance*annualInterestRate),12)/12
fixed_pay = (lower+upper)/2
print(lower,upper)
unpaid_bal = 0
previous_bal = balance
while unpaid_bal >=0:
    unpaid_bal = 0
    balance = previous_bal
    fixed_pay  = (lower+upper)/2
    for i in range(12):
        unpaid_bal = balance - fixed_pay
        balance = unpaid_bal + monthlyrate*unpaid_bal
    if balance < 0:
        upper = pow((balance+balance*annualInterestRate),12)/12
    else:
        lower = balance/12

print('Lowset Payment: '+str(int(fixed_pay)))
