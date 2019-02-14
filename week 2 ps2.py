balance = 4773
annualInterestRate = 0.2
monthlyrate = annualInterestRate/12
fixed_pay = 0
unpaid_bal = 0
previous_bal = balance
while unpaid_bal >=0:
    unpaid_bal = 0
    balance = previous_bal
    fixed_pay+=10
    for i in range(12):
        unpaid_bal = balance - fixed_pay
        balance = unpaid_bal + monthlyrate*unpaid_bal

print('Lowset Payment: '+str(int(fixed_pay)))
