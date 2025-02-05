 
'''def greeting():
  username, age =input('Enter your name and age with a space ').split()
  if username.isalpha() and age.isdigit():
   print(f'Hi welcome {username} and your age is: {age}')
  else:
    print('give a valid input')

def even_odd():
  number=input('type a number')
  if number.isdigit():
    numb=int(number)
    if(numb%2==0):
     print(f'{numb} is even')
    else:
      print('odd number')
  else:
    print('enter a number')'''

def check():
  num=9
  number=['even' if num%2==0 else 'odd'  ]
  print(number)

def main():
  #greeting()
  #even_odd()
  check()

main()
