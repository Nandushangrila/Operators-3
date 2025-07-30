print("Enter your grades:")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

total=mark1+mark2+mark3+mark4+mark5
average=total/5
print("Your average grade was",average)

if average >=91 and average <=100:
    print("Your grade is an A+")
elif average >=81 and average <=90:
    print("Your grade is a B")
elif average >=71 and average <=80:
    print("Your grade is a C")
elif average >=61 and average <=70:
    print("Your grade is a F")
else:
    print("You have failed")