name = input ("Enter Your Name: ")     #String input 
print ("Hello " , name)

age = int (input("Enter Your Age: "))  #Integer input (need to define the Input Type'int'
print ("Your Are " , age ," Old")


#1st way
num1 = input ("Enter Any Number: ")    #We can take integer input like this but it can cause mistake in calculation 
num2 = input ("Enter 2nd Number: ")  

#Wrong structure
print ("Sum: ", num1 + num2)          #Computer don't understand that 10+10=20 or 10+10=1010 without int
#Output will be num1num2.  no matter input is integer or string 

#Right one (answer will be num1 + num2 only if input are integer
print ("Sum: ", int (num1) + int (num2))


#2nd way

num3 = int(input ("Enter Any Number: ") )       #
num4 = int(input ("Enter Any other Number: ") )

print ("Sum: ", num3 + num4)
