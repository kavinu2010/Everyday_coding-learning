MAX_LINES=3
MAX_BET=100
MIN_BET=1

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
  while(True):
    lines=input("enter the number of lines to be bet on (1-"+ str(MAX_LINES) + ")?  ")
    if lines.isdigit() :
      lines= int(lines)
      if 1<=lines<=MAX_LINES:
        break
      else:
        print('enter a valid numer')
    else:
      print('Plesas enter a number')

  return lines



def get_bet():
  while(True):
    amount=input('what would like to bett? $ ')
    if amount.isdigit() :
      amount= int(amount)
      if MIN_BET<=amount<=MAX_BET:
        break
      else:
        print(f'amount must be between the range {MIN_BET} - {MAX_BET}')
    else:
      print('Plesas enter a number')

  return amount




def main():
 balance=deposit()
 lines=get_number_of_lines()
 bet=get_bet()
 total_bet=lines*bet
 print(f'your betting {bet} for {lines}: total is {total_bet}')
 print(balance,lines)

main()


  