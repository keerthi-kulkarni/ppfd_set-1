while True:
  l=float(input("enter the length: \n"))
  b=float(input("enter the breadth: \n"))
  print("1.area\n2.perimeter\n3.exit ")
  cho=int(input("\nenter the choice: "))
  if cho==1:
    area=l*b
    print("\narea of the rectangle with length",end=" ")
    print(l,"and breadth",b,"is: ",area)
  elif cho==2:
    per=2*(l+b)
  elif cho==3:
    break
  else:
    print("Invalid input!")