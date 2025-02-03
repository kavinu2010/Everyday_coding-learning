'''array_value = []

while True:
    user_input = input("Enter a value or type 'EXIT' to quit: ")

    if user_input.lower() == 'exit':
        break  # Exit the loop

    try:
        value = int(user_input)  # Convert input to an integer
        array_value.append(value)  # Add to list
        print(f"Stored Value: {value}")
    except ValueError:
        print("Invalid input! Please enter a number or type 'EXIT' to quit.")

print("Final List of Values:", array_value)'''













import math

array_value=[]

while(True):
  user_input=input('enter the lsit of value of type exit >>' )

  if user_input.lower()=='exit':
    break

  try:
    value=int(user_input)
    array_value.append(value)
    print(f'stored value is :  {value}')

  except ValueError:
    print('Print invalid input!. type exit to quit')

print(array_value)

sum_value=sum(array_value)
print(sum_value)

mul=math.prod(array_value)
print(mul)

max=max(array_value)
print(max)
  