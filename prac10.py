def decimal_others(value,choice):
  if choice==1:
    return value
elif choice==2:
  return '{0:b}'.format(value)
elif choice==3:
  return '{0:o}'.format(value)
elif choice==4:
  return '{0:x}'.format(value)
else:
  return "Invalid option"
def binary_others(value,choice):
  if choice==1:
    return value
  elif choice==2:
    return int(value,2)
  elif choice==3:
    return '{0:o}'.format(int(value,2))
  elif choice==4:
    return '{0:x}'format(int(value,2))
  else:
    return "Inavalid Option"
def octal_others(value,choice):
  if choice==1:
    return value
  elif choice==2:
    return int(value,8)
  elif choice==3:
    return '{0:b}'.format(int(value,8))
  elif choice==4:
    return '{0:x}'.format(int(value,8))
  else:
    return "Invalid Option"
def hex_others(value,choice):
  if choice==1:
    return value
  elif choice==2:
    return int(value,16)
  elif choice==3:
    return '{0:0}'.format(int(value,16))
  elif choice==4:
    return '{0:b}'.format(int(value,16))
  else:
    return "Invalid Option"
print("Convert from: 1: decilmal ,2: binary ,3: octal ,4: hexadecimal")
input_choice=int(input("enter the choice: \n"))
if input_choice==1:
  decimal_num=int(input("enter decimal number: "))
  print('Convert to: 1: binary,2: decimal,3: octal,4: hexadecimal')
  choice=int(input("enter target conversion: \n"))
  print("Conversion value: ",decimal_others(decimal_num,choice))
elif input_choice==2:
  binary_num=int(input("enter decimal number: "))
  print('Convert to: 1: binary,2: decimal,3: octal,4: hexadecimal')
  choice=int(input("enter target conversion: \n"))
  print("Conversion value: ",binary_others(binary_num,choice))
elif input_choice==3:
  octal_num=int(input("enter decimal number: "))
  print('Convert to: 1: binary,2: decimal,3: octal,4: hexadecimal')
  choice=int(input("enter target conversion: \n"))
  print("Conversion value: ",octal_others(octal_num,choice))
elif input_choice==4:
  hex_num=int(input("enter decimal number: "))
  print('Convert to: 1: binary,2: decimal,3: octal,4: hexadecimal')
  choice=int(input("enter target conversion: \n"))
  print("Conversion value: ",hex_others(hex_num,choice))