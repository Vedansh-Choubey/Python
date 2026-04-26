#num1 = int(input("Enter Any Number: "))
#if num1 > 0:
#  print ("Its a Positive Number!!")
#elif num1 = 0:
#  print ("Entered Muber is Zero!!")
#else:
#  print ("Its a Negative Number ") 

cgpa = float (input("Enter Your Current CGPA: "))
if cgpa <= 5.0:
  outcome ="Very Poor, Need maximum Efforts"

elif cgpa <= 6.0:
  outcome ="Need more efforts!!"

elif cgpa <= 7.0:
  outcome ="Need to Study more!"

elif cgpa <= 8.0:
  outcome ="You Are already Ahead of 70% students, Study more to level up"

else:
  outcome ="You are doing Great Champion, Keep Working Hard"

print ("According To Your CGPA: " , outcome)
 
