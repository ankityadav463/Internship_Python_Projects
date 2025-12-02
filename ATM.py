print("Shree Radhe Radhe...\n")
  # ATM
c=1
while True:
    pin=1529
    Amount=48145
    print("Welcome\nAttempt",c)
    pn=int(input("Enter Your PIN:"))
    if pin==pn:
        print(f'Your current Amount is:{Amount}')
        draw=int(input("Enter Amount To Withdraw:"))
        f=Amount-draw
        print(f'Withdraw Amount is:{draw}\nYour Current Amount is:{f}')
    else:
        c+=1
        print("You Enter Wrong PIN")
        if c>3:
          print("Your account was blocked for 24 hours")
          break