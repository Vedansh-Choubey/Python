# Practice Program 1

total = 0
n = int (input("Enter N Value: "))
for i in range (1, n+1 ):           #Only n will lead to the (n-1)th value and the value n will be missed
    total += i

print ("Sum Of N Numbers will be: ", total)


# Practice Program 2

total = 0
subjects = int (input("Enter Your Subject Counts: "))

for i in range (1 , subjects +1):
    sub = int( input ("Enter Achieved marks out of 100: ")
    total += sub

print("Your Total Marks: " , total ," Out Of " , subjects *100)
print("Your Average Marks: ", total / subjects)

