def compmpgcost(miles, gallons):
    if gallons > 0:
        mpg = miles / gallons
    else:
        mpg = 0
    gascost = gallons * 3.00
    return mpg, gascost

tripcount = 0
totalmiles = 0.0
totalgas = 0.0

r = input("Do you want to enter a trip? (Yes/No): ")

while r == "Yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))

    mpg, gascost = compmpgcost(miles, gallons)

    tripcount = tripcount + 1
    totalmiles = miles + 1
    totalgas = gascost + 1

    print("Destination: ", city)
    print("Miles Travelled: ", miles)
    print("Miles Per Gallon: ", mpg)
    print("Gas Cost: ", gascost)


    r = input("Do you want to enter another trip? (Yes/No): ")

print("Total Trips: ", tripcount)
print("Total Miles Travelled: ", totalmiles)
print("Total Gas Cost: ", totalgas)
