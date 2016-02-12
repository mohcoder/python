balance = float(input('Enter value of the payment by credit card: $$ '))
interestRate= float(input('Enter the annual interest rate: % '))
monthlyRate = float(input('Enter the minimum monthly payment rate: % '))
monthlyPayment = float(input('Desired monthly payment: $$ '))
interestRate/= 100
monthlyRate /= 100

dailyRate = interestRate/365
annualRate = (((dailyRate+1)**365)-1)
monthRate = annualRate/12
i = 0
totalInterestpaid = 0.00
totalPrinciplepaid = 0.00
initBalance = balance

while balance > 0:
    minp = max(float(balance*monthlyRate),monthlyPayment)
    iPay = float(monthRate*balance)
    pPay = float(minp-iPay)

    if balance > (initBalance * 100):
        break
    else:
        balance -= minp
        totalInterestpaid += iPay
        totalPrinciplepaid += pPay
        balance *= (monthRate+1)
        i += 1

if balance <= 0:
    print('------------------------------------------')
    print('Initial balance: %s $$'% round(initBalance, 3)) 
    print('Months to pay off: %s months' % i)
    print('Additional interest paid: %s $$' % round(totalInterestpaid, 2))
    print('------------------------------------------')

else:
    print ('------------------------------------------')
    print ('!!! Warning minimum monthly payment insufficient to pay off current balance !!!')
    print ('After %s months, your current balance is %s !' % (i, round(balance, 3)))
