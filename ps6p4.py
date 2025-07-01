def comppay(jobcode, hrs):


    if jobcode == "L":
        rate = 25.00
    elif jobcode == "A":
        rate = 30.00
    elif jobcode == "J":
        rate = 50.00
    else:
        rate = 0.00

    if hrs > 40:
        overtime = hrs - 40
        grosspay = (40 * rate) + (overtime * rate * 1.5)
    else:
        grosspay = hrs * rate

    return rate, grosspay


totalgrosspay = 0.0

r = input("Do you want to enter employee info? (Yes/No): ")

while r == "Yes":
    lastname = input("Enter employee's last name: ")
    jobcode = input("Enter job code (L, A, or J): ")
    hrs = float(input("Enter hours worked: "))

    rate, grosspay = comppay(jobcode, hrs)
    totalgrosspay = totalgrosspay + grosspay

    print("Employee: ", lastname)
    print("Hours Worked: ", hrs)
    print("Pay Rate: ", rate)
    print("Gross Pay: ", grosspay)


    r = input("Do you want to enter another employee? (Yes/No): ")

print("Total Gross Pay for all Employees: ", totalgrosspay)
