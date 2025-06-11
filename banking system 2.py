#all the vaiables we need

clients_names=["Ahmad Ali","Zubair Baig","Abadullah Khan","dawood Qurashi","Ali Azhar"]
clients_pins=["0001",'0002',"0003","0004","0005"]
clients_balances=[10000,20000,30000,40000,50000]
clients_deposit=0
clients_withdraw=0
clients_balance=0

#banking system option screen
while True:
    print("**************************************************")
    print("================THE BANKING SYSTEM================")
    print("**************************************************")
    print("==========      (a) WITHDRAW MONEY      ==========")
    print("==========      (b) DEPOSIT MONEY       ==========")
    print("==========      (c) CHECK BALANCE       ==========")
    print("==========      (d) QUIT                ==========")
    print("**************************************************")

    client_option=input("Enter the letter from above:")

    # making of withdraw option
    pin_checker=True

    if client_option=="a":
        print("letter 'a' has been choosed by the client")
        while pin_checker:
            index=0
            name=input("Enter your name:")
            pin=input("Enter your pin:")
            while index < len(clients_names):
                if name==clients_names[index]:
                    if pin==clients_pins[index]:
                        pin_checker=False
                        clients_balance=clients_balances[index]
                        print("Your balance is:",clients_balance)
                        clients_withdraw=eval(input("Enter the value you want to withdraw:"))
                        print("Withdraw Sucessfully Done!")
                        clients_balance-=clients_withdraw
                        print("Your current balance is:", clients_balance)
                        clients_balances[index]=clients_balance
                index+=1
                
            if pin_checker:
                print("Your pin/name is invalid!")   
        
        backtomenu=input("Press the Enter key to go to the main menu")


#deposit option
    elif client_option=="b":
        print("letter 'b' has chosen by the client")
        w=0
        while w < 1:
            index=0
            name=input("Enter your name:")
            pin=input("Enter your pin:")
            while index < len(clients_names):
                if name==clients_names[index]:
                    if pin==clients_pins[index]:
                        w+=1
                        clients_balance=clients_balances[index]
                        print(f"Your current balance is:{clients_balance}")
                        clients_deposit=eval(input("Enter the value you want to deposit:"))
                        clients_balance+=clients_deposit
                        print("Deposition Successfully Done!")
                        print(f"Your current balance is:{clients_balance}")
                        clients_balances[index]=clients_balance
                index+=1
            if w < 1:
                print("Your pin/name is invalid!")
        backtomenu=("Press Enter key to go to the main menu")
        
#check balance option
    elif client_option=='c':
        l=0
        print("Letter 'c' has been chosen by the client")
        name=input("Enter your name:")
        pin=input("Enter your pin:")
        index=0
        while l < 1:
            while index < len(clients_names):
                if name==clients_names[index]:
                    if pin==clients_pins[index]:
                        l+=1
                        clients_balances[index]=clients_balance
                        print(f"Your balance is:{clients_balance}")
                index+=1
            if l < 1:
                print("Your name/pin is in valid")
        backtomenu=input("Press Enter key to go to the main menu:")
#Quit opion
    elif client_option=='d':
        print("Thanks for using our Banking system",'\n')
        print("Take care ,bye!","\U0001F600") 
                                                              
        break
    else:
        print("Invalid choise, please try again")



                        