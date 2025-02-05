 
def greeting():
  username, age =input('Enter your name and age with a space ').split()
  if username.isalpha() and age.isdigit():
   print(f'Hi welcome {username} and your age is: {age}')
  else:
    print('give a valid input')




def main():
  greeting()

main()
