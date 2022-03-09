class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
        self.balances=50000

    def balance(self):
        print('balance is ',self.balances)
        

    def withdrawl(self,amount):
        self.balances=self.balances-amount
        print("your balance is: ", self.balances)

def main():
    cardnumber=input('enter your cardnumber')
    pin=input('enter your pin? ')

    user1= Atm(cardnumber,pin)

    activity=int(input('choose your activity 1.check balance  2. withdrawl money '))

    if(activity == 1):
        user1.balance()
    elif(activity == 2):
        amount=int(input('enter the amount to be withdrawned? '))
        user1.withdrawl(amount)
    else:
        print('enter a valid number')

main()
        
