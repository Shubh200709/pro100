class Atm:
    def _init_(self,cardno,pinno,transtype, amount):
        self.cardno = cardno
        self.pinno = pinno
        self.transtype = transtype
        self.amount = amount
    
    def Withdraw(self, amountType):
        self.amountType = amountType
        print(self.amount,"transfered '\n' please collect")
    
    def Deposit(self, amountType):
        self.amountType = amountType
        print(self.amount,"transfered to bank '\n' thank you")
    
    def BalanceEnquiry(self, amountLeft):
        self.amountLeft = amountLeft
        if(self.transtype=="withdraw"):
            balance = self.amountLeft - self.amount

            if(balance >= 0):
                print("Rs.",balance,"left in your account")
            else:
                print("Rs.",self.amount,"Cannot be withdrawn")
        elif(self.transtype == "deposit"):
            balance = self.amountLeft + self.amount
            print("Rs.",balance,"is there in your account")
        else:
            print("Invalid input '\n' Please try again")

cno = int(input("Enter your card Number"))
pno = int(input("Enter your pin number"))
type = input("Enter the type of transacction(withdraw/deposit)")
money = float("enter the amount")

atm = Atm(cno,pno,type,money)

if(type == "withdraw"):
    atm.Withdraw("withdraw")
    atm.BalanceEnquiry(2000)
else:
    atm.Deposit("deposit")
    atm.BalanceEnquiry(2000)