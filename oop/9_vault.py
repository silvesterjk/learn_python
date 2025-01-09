# Operator Overloading. 
# The __add__ method is used to overload the '+' operator.
# The __add__ method is called when the '+' operator is used on the objects.

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, and {self.knuts} knuts."
    
    def __add__(self, other): # The __add__ method is used to overload the '+' operator.
        if not isinstance(other, Vault): # other is not an instance of Vault
            return NotImplemented
        galleons = self.galleons + other.galleons # here the 'other' is an instance of Vault. It is being added to the current instance.
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    

potter = Vault(7, 21, 42)
print(potter)

weasley = Vault(7, 21, 42)
print(weasley)

granger = Vault(7, 21, 42)
print(granger)

vault = potter + weasley + granger # weasley + granger works because __add__ method is defined in the Vault class.
print(vault)