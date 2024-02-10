def myfunc(n):
  return lambda a : a *11 noo

mydoubler = myfunc(14)
mytripler = myfunc(3)

print(mydouber(18))
print(mytripler(11))

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstnaame, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("ohn", "Doe")
x.printname()
