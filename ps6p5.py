def comptuition(credithrs, districtcode):

    if districtcode == "I":
        rate = 250
    elif districtcode == "O":
        rate = 550
    else:
        rate = 0

    tuition = credithrs * rate
    return tuition

totaltuition = 0.0

r = input("Do you want to enter a student? (Yes/No): ")

while r == "Yes":
    lastname = input("Enter student's last name: ")
    credithrs = int(input("Enter number of credit hours: "))
    districtcode = input("Enter district code (I for In-district, O for Out-of-district): ")

    tuition = comptuition(credithrs, districtcode)
    totaltuition = totaltuition + tuition

    print("Student: ", lastname)
    print("Tuition Owed: ", tuition)


    r = input("Do you want to enter another student? (Yes/No): ")

print(f"Total Tuition Owed by All Students: ", totaltuition)
