 
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
    print('enter a number')

def check():
  num=9
  number=['even' if num%2==0 else 'odd'  ]
  print(number)

array_ele=[]
def max_min():
  
  while(True):
   element=input('enter a list of number or else type exit  >> ' )

   if element.lower()=='exit':
     break
   
   try:
     
     value=int(element)
     array_ele.append(value)
     print(array_ele)

   except ValueError:
     print('enter a valid input to quit')

  print(array_ele)
  maximum=max(array_ele)
  minimum=min(array_ele)
  print(f'maximum number in the array list is :{maximum}')
  print(f'minimum number in the arrya lisr is :{minimum}')
     
     
   

def polyndrome(str):
  return str==str[::-1]'''

def fact(n):
  result=1
  for i in range(1,n+1):
    result*=i
  return result
     

def main():
  #greeting()
  #even_odd()
  #check()
  #max_min()
  #print(polyndrome('mom'))
  print(fact(10))


main()
