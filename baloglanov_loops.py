#Q1

for i in range (10,0,-1):
    print(i)
print("Liftoff!")

#Q2

childticket = 0

for i in range(1, 6):
    print("Age of visitor", i, ":", end=" ")
    age = int(input())
    if age < 18:
        childticket += 1

print("Child tickets:", childticket)
print("Adult tickets:", 5 - childticket)

#Q3

# 1,3,5,7,9

#Q4

total=0
for i in range(1, 6):
    print("Price of item", i, ":", end=" ")
    price = float(input())
    total+=price
print("Total :",total)
print("Average :",total/5)

#Q5

password=input("New password :")
while len(password)<8:
    print("Too short, try again")
    password=input("New password :")
print("Password accepted")

#Q6

# 70
# 40
# 10
# -20
# Done

#Q7

steps=1200
for day in range(1,8):
    print("Day",end=" ")
    print(day,":",steps)
    steps+=1200

#Q8

username=input("Username :")
password=input("Password :")
while username!="admin" or password!="1234":
    print("Wrong username or password")
    username=input("Username :")
    password=input("Password :")
print("Welcome")

#Q9

balance=500
while balance!=0:
    amount=int(input("Amount :"))

    if amount<0:
        print("Invalid amount")
        continue
    elif amount==0:
        print("Goodbye")
    elif amount>balance and amount>=0:
        print("Insufficient funds")
    else:
        balance-=amount
        print("Balance :",balance)

print("Goodbye")

#Q10

# 3

#Q11

passs=0
fail=0
max=0
m=0
grade=int(input("Grade :"))
while grade!=-1:
    m+=grade
    if grade>=51:
        passs+=1
    else:
        fail+=1
    if max<grade:
        max=grade
    grade=int(input("Grade :"))
print("Passed :",passs)
print("Failed :",fail)
print("Highest :",max)
print("Average :",m/(fail+passs))

#Q12

freespaces=20
command=input("Command :")
while command!="stop":
    if command=="in":
        if freespaces==0:
            print("Garage is full")
        else:
            freespaces-=1
            print("Free spaces :",freespaces)
    elif command=="out":
        if freespaces==20:
            print("Garage is empty")
        else:
            freespaces+=1
            print("Free spaces :",freespaces)
    elif command=="stop":
        break
    else:
        print("Unknown command")
    command=input("Command :")

#Q13

s=0
hottestday=0
hotdays=0
for i in range(1,8):
    print("Day",i,":",end=" ")
    temperature=int(input(""))
    if s<temperature:
        s=temperature
        hottestday=i
    if temperature>30:
        hotdays+=1
print("Hot days :",hotdays)
print("Hottest day",hottestday)

#Q14

#We should write attempts=0 outside of the loop because everytime when loop starts again it become 0

password = "secret"
attempts = 0
while True:
    
    entered = input("Password: ")
    if entered == password:
        print("Welcome")
        break
    attempts += 1
    if attempts == 3:
        print("Account locked")
        break

#Q15

password=input("Password :")
digit=0
upper=0
lower=0
for i in password:
    if i.isdigit():
        digit+=1
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
if len(password)>=8 and digit!=0 and upper!=0 and lower!=0:
    print("Strong Password")
elif digit==0 :
    print("Weak Password,no digit")
elif upper==0 :
    print("Weak Password,no uppercase")
elif digit==0 :
    print("Weak Password,no lowercase")
else:
    print("Weak Password,shorter than 8")

#Q16

balance=0
start=50
month=0
while balance<1000:
    balance+=start
    start+=10
    month+=1
    print("Month",month,":",balance)
print("Goal reached in month",month)

#Q17

# 105

#Q18


attempt = 0
balance = 1000

while attempt < 3:
    pin = input("Enter PIN :")

    if pin == "2580":
        print("Successful login")
        break
    else:
        attempt += 1
        print("Wrong PIN")

if attempt == 3 and pin != "2580":
    print("Card blocked")
else:
    choice = "0"

    while choice != "4":
        print("1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit")

        choice = input("Your Choice :")

        if choice == "1":
            print(balance)

        elif choice == "2":
            amount = int(input("Amount :"))
            if amount <= 0:
                print("Invalid amount")
            else:
                balance += amount
                continue

        elif choice == "3":
            amount = int(input("Amount :"))
            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print("Insufficient funds")
            else:
                balance -= amount
                continue

        elif choice == "4":
            print("Goodbye")

        else:
            print("Invalid choice")

#Q19

balance=0
while balance<1.5:
    coin=float(input("Insert coin :"))
    if coin!=1.0 and coin!=0.5 and coin!=0.2 and coin!=0.1 and coin!=0.05:
        print("Coin not accepted")
    else:
        balance+=coin
        print("Total",balance)
if balance>=1.5:
    print("Here is your water")
    print("Change :", balance-1.5)

#Q20

m=0
def sade(x):
    s=0
    for i in range(2,x):
        if x%i==0:
            s+=1
    return s
for i in range(2,100):
    if sade(i)==0:
        print(i)
        m+=1
print("Total codes :",m)

#Q21

#101 102 201 202 301 302 

#Q22

for floor in range(1,6):
    if floor==4:
        continue
    else:
        print("Floor",floor,":", end=" ")
        for i in range(1,5):
            print(floor*100+i,end=" ")
        print()

#Q23

time=60
number=1
exptime=0
while time>0:
    print("Customer",number,"needs(min):",end=" ")
    exptime=int(input())
    
    if time-exptime<0:
        print("Sorry, come back tomorrow")
        break
    else:
        time-=exptime
        number+=1
print("Customers served :",number-1)
print("Minutes Left :",time)

#Q24

vote=""
a=0
b=0
c=0
spoiled=0

while vote!="end":
    vote=input("Vote :")
    if vote=="A":
        a+=1
    elif vote=="B":
        b+=1
    elif vote=="C":
        c+=1
    elif vote=="end":
        break
    else:
        spoiled+=1
print("A :",a,"B :",b,"C :",c)
print("Spoiled :",spoiled)
if a>b and a>c:
    print("Winner: A")
elif b>a and b>c:
    print("Winner: B")
elif c>a and c>b:
    print("Winner: C")
else:
    print("Tie")

#Q25

bank = input("Enter 16 digit card number :")

while len(bank) != 16 or not bank.isdigit():
    print("Must be 16 digits")
    bank = input("Enter 16 digit card number :")

m = 0
total = 0

for i in range(15, -1, -1):
    m = int(bank[i])

    if i%2==0:
        m = m * 2
        if m > 9:
            m = m - 9

    total += m

if total%10==0:
    print("Valid card number")
else:
    print("Invalid card number")
