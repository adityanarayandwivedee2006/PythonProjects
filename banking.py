# Banking Program

def show_balance(balance):
    print(f"Your balance is {balance:.2f}")



def deposite():
    amount =float(input("Enter an amount to bedeposited"))
    if amount<0:
        print("That's not a valid amount")
        return 0
    else: 
         return amount      

def withdraw(balance):
    amount=float(input("Enter amount to be withdrawn : "))
    if amount>balance:
        print("Insufficient funds")
        return 0
    elif amount<0:
        print("Amount must be greater than 0")   
        return 0
    else:
        return amount     
def main():
    balance=0
    is_running=True

    while  is_running:
        print("Banking program")
        print("1 Show Balance")
        print("2 Deposite")
        print("2 Withdraw")
        print("4 Exit")

        choice=input("Enter your choice (1-4) : ")
        if choice =='1':
            show_balance(balance)
        elif choice =='2':
            balance += deposite()
        elif choice =='3':
            balance-=withdraw(balance)
        elif choice =='4':
            is_running=False
        else:
            print("That is not a valid choice")  
if __name__=='__main__':
    main()  