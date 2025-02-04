MAX_LINES=3

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


def get_number_of_lines():
  

def main():
 balance=deposit()

main()


  