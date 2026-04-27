#Checking a single number is Even Or Odd

n = int(input("Enter Any Number: "))
if n % 2 == 0:
  print ("Entered Number is Even ")
else :
  print ("Its An Odd Number ")

#Chevking Even And Odd Number in Range

n = int (input("Enter intial Number: "))
m = int (input("Enter Last Number: "))

for i in range (n , m):
    if i%2 == 0:
      print ("Even", i)
    else :
      print("Odd", i)
