# Python Object representing a purchase for a given amount
class Purchase(object):
    def __init__(self,amount):
       self.amount = amount
       
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0
        
    def calculateTip(self, tipPercentage):
        return self.amount * tipPercentage/100.0
        
    def calculateTotal(self, taxPercentage, tipPercentage):
        return self.amount * (1 + taxPercentage/100.0 + tipPercentage/100.0)
        
# Create Purchase object given an amount
purchase = Purchase(100.0)

# Set the tax and tip percentages
taxPercentage = 7.5
tipPercentage = 20.0

# Use the object to calculate tax and tip
tax = purchase.calculateTax(taxPercentage)
tip = purchase.calculateTip(tipPercentage)

# Display some useful information
print ('Tax: ',tax)
print ('Tip: ',tip)
print ('Total:', purchase.calculateTotal(taxPercentage, tipPercentage))

