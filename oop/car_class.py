class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def __str__(self):
        return f"Is the {self.year} {self.colour} {self.model} for sale? : {self.for_sale}."
    
    def drive(self):
        return f"{self.model} is driving." 
    
    def description(self):
        return f"{self.year} {self.colour} {self.model} is a car for sale."