def compbatavg(hits, atbats):
    if atbats > 0:
        return hits / atbats
    else:
        return 0.0

playercount = 0
r = input("Do you want to enter player info? (Yes/No): ")

while r == "Yes":
    lastname = input("Enter player's last name: ")
    hits = float(input("Enter number of hits: "))
    atbats = float(input("Enter number of at bats: "))

    batavg = compbatavg(hits, atbats)
    playercount = playercount + 1

    print("Last name: ", lastname)
    print("Batting average: ", batavg)


    r = input("Do you want to enter another player? (Yes/No): ")

print("Total number of players entered: ", playercount)
