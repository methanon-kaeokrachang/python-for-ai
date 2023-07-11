#Blueprint or Model (in MVC Design Patterns)
class Customer():
  def __init__(self,id ,name ,age , address, email , balance, stocks):
    self.id = id
    self.name = name
    self.age = age
    self.address = address
    self.email = email
    self.balance = balance
    self.stocks = stocks
# Deposit Controller
class deposit():
  def __init__(self,customer):
    self.customer = customer
  
  def addCash(self, inputCash):
    self.customer.balance +=inputCash
  
  def printHello():
    print("kkk")

#Withdraw Controller
class withdraw():
  def __init__(self,customer):
    self.customer = customer
  
  def removeCash(self, inputCash):
    self.customer.balance -=inputCash
  
#Trade Controller
class trade():
  def __init__(self,customer): #Costuctor Method
    self.customer = customer
  
  def buy(self, stockName, volume):
    self.customer.stocks[stockName]+=volume
  
  def sell(self, stockName, volume):
    self.customer.stocks[stockName]-=volume
                  #stocks["AOT"]


stocks = {"AOT":4000, 
          "CPF":1000,
          "PTT":2000}
methanon = Customer(1001, "methanon", 24, "xxx", "xxx@xxx.com", 4000, stocks)
print("id:", methanon.id)
print("name:", methanon.name)
print("age:", methanon.age)
print("address:", methanon.address)
print("email:", methanon.email)
print("balance:", methanon.balance)
print("stocks:", methanon.stocks)

################################################################################
methanonDeposit = deposit(methanon)
methanonDeposit.addCash(1000)

print("After add Cash, ", methanonDeposit.customer.balance)

################################################################################
methanonWithDraw = withdraw(methanon)
methanonWithDraw.removeCash(100)
print("After remove Cash, ", methanonWithDraw.customer.balance)

################################################################################
methanonTrade = trade(methanon)
print("Old Hoding CPF, ", methanonTrade.customer.stocks["CPF"])
methanonTrade.buy("CPF", 21)
print("New Hoding CPF, ", methanonTrade.customer.stocks["CPF"])

