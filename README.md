# PyBank
A Python bank that lets users deposit/withdraw, check their bank balance, create and log in to their accounts, and store their information for multiple uses.



**Basic Information**: For my Python program, it includes different functions and a homepage. The file is called Pybank Main Database, and formats the options as ID, Name, Password, and then value. For example, John, 12345, 300.0\n,(the \n isn’t visible in the list of the file, but will still be there which is why my program will include code to replace that)

**Homepage**: The homepage will include an option for the user to create a new account, Python will ask them for their ID to be linked to their account, their name to be included in their account, the password to access the account, and the bank balance will be set as 0. 

**Previously Made Accounts**: For those users that have already made an account, Python will ask them for their ID and password. If the ID and password don’t match, then the program will shut down. If they do the program will print you their name as well as the value last saved.

**Inside The Program**: Once the user is inside of the program, there will be an option to deposit, withdraw, show balance, or quit the program. Each option is associated with a number and is in a while loop to keep prompting the user.

**Deposit**: The deposit function will be one of the many functions, first asking for the deposit value. Then it will add the value to the pybank dictionary, with the key of their userid and the last value in the list which is their account balance. 

**Withdraw**: The user also has the option to withdraw, prompting the user again to enter an amount. If the user’s amount is over their bank’s balance, the program will stop the transaction from being completed. Like the deposit function, this is also saved in the pybank dictionary.

**Showing A Balance**: If they enter showing balance, it will print out their balance saved most recently in the pybank dictionary, formatting it in the right way.

**Quitting & Writing**: Once the user quits, the program will clear out the previous information in the file and re-write what is most recently being saved for each userid. There will also be some additional information to make the program look more realistic, such as a fake copyright, and/or some terms and conditions/privacy policies.
