def rectangle():
  length, bredth = input('enter length and bredth of the rectangle').split()
  print(f'length: {length}, bredth: {bredth}')
  
  if length.isdigit() and bredth.isdigit():
    len=int(length)
    bre=int(bredth)
    area=len*bre
    print(f'area of rectangle is >> {area}')
  else:
    print('type valid number')


def main(): 
 rectangle()

main()

  
