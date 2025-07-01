# input
def compextprice(qty, unitprice):
    extprice = qty * unitprice

    if extprice > 10000.00:
        discamt = extprice * 0.1
    else:
        discamt = 0

    return extprice

totalextprice = 0.0
r = input("Do you want to compute extended price (Yes/No)? ")

while r == "Yes":
    qty = float(input("Enter quantity: "))
    unitprice = float(input("Enter price: "))
    extprice = compextprice(qty, unitprice)
    totalextprice = totalextprice + extprice
    print("Extended price is $", extprice)
    r = input("Do you want to compute extended price (Yes/No)? ")

    print("Total extended price is $ ", totalextprice)