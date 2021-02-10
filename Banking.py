class Banking_Services:
    balance = 0
    amount_deposited = 0
    amount_withdrawn = 0

    def account(self):
        self.account_no = int(input("Enter the account number :"))
        self.name = str(input("Enter the name :"))

    def money_deposit(self):
        self.amount_deposited = float(input('Enter the amount to deposit:'))
        self.balance += self.amount_deposited
        if self.amount_deposited >= 500:
            print("Better Luck Next Tme...")

    def money_withdraw(self):
        self.amount_withdrawn = float(input("Enter Amount To Withdrawn :"))
        if self.balance >= self.amount_withdrawn:
            self.balance -= self.amount_withdrawn
        else:
            print("Insufficient Balance")

    def Balance_check(self):
        print('Balance is : %d\n' % self.balance)

    def Transaction_Statements(self):
        print('Account Number=%d' % self.account_no)
        print('Account Holder=%s' % self.name)
        print('Amount Deposited=%d' % self.amount_deposited)
        print('Amount Withdrawn=%d' % self.amount_withdrawn)


bank = Banking_Services()
bank.account()
bank.money_deposit()
bank.money_withdraw()
bank.Balance_check()
bank.Transaction_Statements()