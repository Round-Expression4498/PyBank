#Create a database using a Python dictionary
#Use hardcoded values as default entries
#Name of the dict is pybank
#When users create new id it will add to pybank

pybank = {}


#This function takes the user's id, deposit value, and updates the dictionary pybank
def deposit(userid):
        deposit = float(input("How much would you like to deposit?"))
        dep = deposit + deposit * 0.02 + float(pybank[userid][2])
        pybank[userid][2] = str(dep)
        idbank = userid + "'s bank balance is " + pybank[userid][2] + " including our new PyBank 2.0% interest plan"
        print(idbank)     
    
#This function takes the user's id, withdrawal value, and updates the dictionary pybank
#This function temporarily stores the user's balance as a floating point number varaiable, then returns it back as a string
#It also checks if the user's withdrawl value is less then their current budget, and rejects the transaction
def withdraw(userid):
    print("How much would you like to withdraw?")
    withdraw = float(input())
    b = float(pybank[userid][2]) - withdraw
    idbank = userid + "'s bank balance is " + str(b)
    if b < 0:
         print ("You can't do that!")
         b + withdraw
    else:
        print(idbank)
        

#This function opens up the file, then clears it out
#Then this function will add the id, name, password, and bank balance to the file, for every single account, then closes out the file.


def write(pybank):
        bankinfo = open('C:\\Users\samra\\PyBank Main Database.txt','w')
        bankinfo.write("")
        bankinfo.close()
        for userid in pybank:
                bankinfo = open('C:\\Users\samra\\PyBank Main Database.txt','a')
                string1 = userid + "," + pybank[userid][0] + "," + pybank[userid][1] + "," + str(pybank[userid][2]) + "\n"
                bankinfo.write(string1)
                bankinfo.close()
                
                
                

#This loop asks the user what buttons they want to press, either deposit, withdraw, display current balance, or quit.c
#Then once button is determined, run the appropriate function to complete the requested process. 

def account():
        while(True):
            print("Press 1 to deposit, 2 to withdraw, 3 to show balance or 9 to quit")
            response = input(" ")
            bankbalance = 0
            if response == "1":
                deposit(userid)

            if response == "2":
                withdraw(userid)

            if response == "3":
                idbank = userid + "'s bank balance is " + pybank[userid][2]
                print(idbank)    
           
            if response == "9":
                print(" ")
                print("Thank you for working with PyBank!")
                write(pybank)
                print(" ")
                print(" ")
                print(" ")
                print("Copyright @ 2023 PyBank. All rights reserved. This isn't official")
                print("Would you like to view our Privacy Policiy? (yes or no)")
                priv = input()
                if priv == "yes":
                        print("PYBANK PRIVACY POLICIY")
                        print("1. No person should ever be given passwords, our access to our main database")
                        print("2. There isn't an option to expunge an account, since we always believe and hope that you will use it again")
                        print("3. We suggest more complex yet remerable passwords. We can't help store them as part of our database, so hackers won't access your passwords")
                        print("4. Yes, you are able to access your accounts from multiple devices, using the same login information")
                        print("5. All information we take is ID, Name, Password, and Account Balance")
                        print("6. If you decide to make multiple accounts, we suggest different passwords to avoid information being stolen periodically")
                        print("7. If you belive your bank account information or balance has been altered, contact us at skulk4s@k12.jh.edu")
                else:
                        print("PyBank Version 1.0")
                write(pybank)
                break

    
#This is the homescreen, it asks the user to either login to a hardcoded or previously create entry, or to create a new account
#Once the new account is created, (if needed to be) then it re-displays the home screen, so the user can log in with their existing id
print("Welcome to PyBank")
print("--------------------")
print("--------------------")
print(" ")
print("Press 1 to LOG IN...")
print("Press 2 to CREATE NEW ACCOUNT" + " ")

def usercheck(userid):
    for count in range(0,len(content)):
            if content[count] == userid:
                    print("That is already taken")

#This for loop reads the file, then converts it to a list.
#Once a list, it splits the list, then makes all the information except for the user's id a list, then makes that a value for the user id, which is the key.
bankinfo = open('C:\\Users\\samra\PyBank Main Database.txt')
content = bankinfo.readlines()
for count in range(0,len(content)):
        account1=content[count]
        a = account1.split(",")
        a[3] = a[3].replace("\n","")
        customer = [a[1],a[2],a[3]]
        balancea = a[3]
        pybank[a[0]] = customer
button = input()
#This checks if the user's information is corrected to the information listed in the pybank database file.
if button == "1":
        userid = input("Enter User Id:")
        if userid in pybank:
                mypass = input("Enter Password:")
                if mypass == pybank[userid][1]:
                        print("Customer Name: {}".format(pybank[userid][0]))
                        print("Balance: ${}".format(pybank[userid][2]))
                        account()
                        
        else:
                print("Those are invalid credentials")
#This helps the user create a new account, providing all the needed information to store their banking info and run the progran.
if button =="2":
    print(" ")
    userid = input("Please enter a new User ID:")
    usercheck(userid)
    customername = input("Please enter your Name:")
    password = input("Please enter a new Password:")
    balance = "0"
    customer = [customername, password, balance]
    pybank[userid] = customer
    print("Your account has now been created. Please log in with your User Id")
    print(" ")
    print("Welcome to PyBank")
    print("--------------------")
    print("--------------------")
    print(" ")
    print("Press 1 to LOG IN...")
    print("Press 2 to CREATE NEW ACCOUNT" + " ")
    button = input()
    if button == "1":
        userid = input("Enter User Id:")
        if userid in pybank:
                mypass = input("Enter Password:")
                if mypass == pybank[userid][1]:
                        print("Customer Name: {}".format(pybank[userid][0]))
                        print("Balance: ${}".format(pybank[userid][2]))
                        account()
                else:
                    print("Sorry those aren't correct. At Pybank we value our customer's safety as part of our Terms and Conditions. Please restart")
        else:
            print (" ")
            print("Hmmm, I don't recognize that account")
            print("Please try again! Sorry for the inconvenience")
    if button == "2":
            print("Please enter your new User ID")
            userid = input()
            pybank[userid]=0
            account()
            


