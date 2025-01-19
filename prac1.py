while True:
  ch=int(input("enter your choice:\n1.Farebheit\n2.Celsius\n3.Exit\n"))
  if ch==1:
    far=float(input("\nEnter the temperature in Farenheit: "))
    cel=(far-32)*(5/9)
    print("\nThe temperature in Celsiusis:{:.2f}c".format(cel))
  elif ch==2:
      cel=float(input("\nEnter the temperaturein celsius: "))
      far=(cel*9/5)+far-32
      print("\nThe temperature in Farenheitis: {:.2f}F".format(far))
  elif ch==3:
      break
  else:
      print("\nInvalid choice. please enter 1,2 or 3.")