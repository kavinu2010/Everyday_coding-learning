def deposit():
  while(True):
    amount=input('what would like to deposit? $ ')
    if amount.isdigit() :
      amount= int(amount)
      if amount>0:
        break
      else:
        print('amount must be greater than 0')
    else:
      print('Plesas enter a number')

  return amount

deposit()

  