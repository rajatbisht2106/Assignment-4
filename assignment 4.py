#Assignment 4
#Name: Rajat Singh Bishth
#SID: 21107047
#Branch: Mechanical
print("Q1")
while True:
    mark = int(input("Enter mark:"))
    if mark < 25:
        print("Grade: F")
    elif 25 <= mark < 45:
        print("Grade: E")
    elif 45 <= mark < 50:
        print("Grade: D")
    elif 50 <= mark < 60:
        print("Grade: C")
    elif 60 <= mark < 80:
        print("Grade: B")
    elif mark >= 80:
        print("Grade: A")
    user = input("Continue?(y/n)")
    if user == 'n':
        break
        
print("Q2")
a=int(input("Enter the year: "))
if a%400 == 0:
    print(a, "is a leap year.")
elif a%4 == 0:
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")

print('Q3')
import random

for i in range(1,11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f'Question {i}:{a}x{b}='))
    if ans == a*b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a*b)

print('Q4')
for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Answer:",i)
        
        
#--------------------------#
#Output for assignment-4
'''
Q1
Enter mark:70
Grade: B
Continue?(y/n)n
Q2
Enter the year: 2004
2004 is a leap year.
Q3
Question 1:3x7=21
Right!
Question 2:4x1=4
Right!
Question 3:7x5=45
Wrong. The correct answer is 35
Question 4:5x9=45
Right!
Question 5:1x3=3
Right!
Question 6:5x0=0
Right!
Question 7:3x4=12
Right!
Question 8:4x3=12
Right!
Question 9:0x7=0 
Right!
Question 10:5x6=30
Right!
Q4
Answer: 177
'''
