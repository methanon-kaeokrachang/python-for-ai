#Blueprint or Model (in MVC Design Patterns)
class Customer():
  def __init__(self,id ,name ,age , address, email , balance):
    self.id = id
    self.name = name
    self.age = age
    self.address = address
    self.email = email
    self.balance = balance



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
  

methanon = Customer(1001, "methanon", 24, "xxx", "xxx@xxx.com", 4000)
print("id:", methanon.id)
print("name:", methanon.name)
print("age:", methanon.age)
print("address:", methanon.address)
print("email:", methanon.email)
print("balance:", methanon.balance)
################################################################################
methanonDeposit = deposit(methanon)
methanonDeposit.addCash(1000)

print("After add Cash, ", methanonDeposit.customer.balance)

################################################################################
methanonWithDraw = withdraw(methanon)
methanonWithDraw.removeCash(100)
print("After remove Cash, ", methanonWithDraw.customer.balance)

################################################################################
print(methanon)
print(methanonDeposit.customer)
print(methanonWithDraw.customer)
print(methanon.balance)
