num=int(input("Enter any number: "))
fact=1
if num < 0:
   print("No factorial value")
elif num == 0:
   print("1")
else:
   for i in range(1,num + 1):
       fact = fact*i
   print(fact)
