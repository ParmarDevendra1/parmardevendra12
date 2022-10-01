print(" \t\t........Calculater Project..............")
print("          1.Addition")
print("          2.Substraction")
print("          3.Multiplication")
print("          4.Division")
print("          5.Modulo Division")

ch=int(input("      Enter Your Choice......:  "))
a=int(input("Enter Any First no:  "))
b=int(input("Enter Any  Second no:  "))


if  ch==1:
	print(" \t\t 1.Addition Calculater....")
	sum=a+b
	print("          ->",a ," + ", b," = ",sum)
	print("            Addition:  " + str(sum))

elif ch==2:
	  print(" \t\t  2.Substraction Calculater....")
	  sub=a-b
	  print("             ->",a," - ",b," = ",sub)
	  print("             Substraction:  " + str(sub))
	  
elif ch==3:
  	print(" \t\t 3.Multiplication Calculater...")
  	mul=a*b
  	print("           ->",a," * ",b," = ",mul)
  	print("            Multiplication:  " + str(mul))
  
elif ch==4:
	print(" \t\t  4.Division Calculater.....")  
	div=a%b
	print("             ->",a," % ",b," = ",div)
	print("              Division:  " + str(div))
	
elif ch==5:
	print("\t\t  5.Modulo Divsion Calulator...")
	md=a/b
	print("            ->",a," / ",b," = ",md)
	print("            Modu...Division:  " + str(md))
	
else:
	print("Wrong Choice....,No Operator calculate...")
