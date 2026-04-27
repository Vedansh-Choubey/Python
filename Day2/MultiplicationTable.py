# Printing Multiplication table till 10

n = int (input("Enter Any Number: "))    
for i in range (1,11):
  print (n ,"*", i , "=" , i*n)



#Printing Multiplication Table Upto The Value Entered By the user

n = int (input("Enter Any Number: "))
m = int (input("Enter the Range (upto): "))

for i in range (1 , m+1):
  print (n , "*" , i , "=" , i*n)
