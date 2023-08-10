car1 = {"Toyota", "Sedan", "Automatic", "Black"} 
car2 = {"Honda", "SUV", "Manual", "White"}

common = set.intersection(car1, car2)
#these two sets have nothing in common
if not car1 & car2:
    print("Toyota and Honda have nothing in common")
else:
    print("Things that Toyota and Honda have in common:", common)


#right now i make it different
car3 = {"Mazda", "Sedan", "Automatic", "Construction year: 2024", "Yellow"}
car4 = {"Corvette", "Coupe", "Automatic", "Construction year: 2024", "Red"}
common1 = set.intersection(car3, car4)
print("Things that Mazda and Corvette have in common:", common1)