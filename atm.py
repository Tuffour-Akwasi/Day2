class atm(object):
    charges = 0

    def __init__(self, name, act_num, act_tp, act_pin, balance,):

        self.name = name
        self.act_num = act_num
        self.act_pin = act_pin
        self.act_tp = act_tp
        self.balance = balance


#        self.max_rdw = max_rdw
    def History(self):
        return "Name: {} Account Number: {} Account Type: {} Pin Code: {} Amount: {}".format(self.name, self.act_num, self.act_tp, self.act_pin, self.balance)

    def checkPin(self):
        return "Your Pin Number is: {}".format(self.act_pin)

    def deposit(self, amount):
        self.balance = self.balance + amount + atm.charges

    def withdraw(self, amount):
        self.balance = self.balance - amount - atm.charges


p1 = atm('frank', '0001', 'savings','A2B2#4',500)
print(p1.History())
p1.deposit(200)
print(p1.balance)
print(p1.History())
p1.withdraw(500)
print(p1.balance)
print(p1.History())
print(p1.checkPin())
