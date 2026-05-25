import time
import os
import sys
from datetime import datetime
starmall_sampol = [
    "Starmall",
    "Bulacan State University", 
    "Carissa 4B",
    "Kaypian Elementary School",
    "Petron Karyapay",
    "SJDM City Hall",
    "Motorpol", 
    "Area E",
    "SJDM National Trade School",
    "Sampol"
    ]
sampol_starmall = [
    "Sampol",
    "SJDM National Trade School",
    "Area E",
    "Motorpol", 
    "SJDM City Hall",
    "Petron (Karyapay)",
    "Kaypian Elementary School",
    "Carissa 4B",
    "Bulacan State University",
    "Starmall",
    ]
fare = [
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 23],  
    [15, 0, 15, 16, 17, 18, 19, 20, 21, 22],  
    [16, 15, 0, 15, 16, 17, 18, 19, 20, 21],  
    [17, 16, 15, 0, 15, 16, 17, 18, 19, 20],  
    [18, 17, 16, 15, 0, 16, 17, 18, 19, 20], 
    [19, 18, 17, 16, 15, 0, 15, 16, 17, 18], 
    [20, 19, 18, 17, 16, 15, 0 ,15, 16, 17],  
    [21, 20, 19, 18, 17, 16, 15, 0, 15, 16],  
    [22, 21, 20, 19, 18, 17, 16, 15, 0, 15],  
    [23, 22, 21, 20, 19, 18, 17, 16, 15, 0]   
    ]
Discounts = [
    "Student", "Senior Citizen", "PWD", "Regular"
    ]

def type_writer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(delay)
    print()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


boundary = []

DriverName = input("Enter Driver Name: ")
ConductorName = input("Enter Conductor Name: ")
BodyNumber = int(input("Enter Body Number: "))
print(f"Good Day {DriverName} and {ConductorName}")
time.sleep(2)
now = datetime.now()
noms = now.replace(microsecond=0)

while True:
    clear()
    print("===================================")
    print("              ROUTE")
    print("===================================")
    print("1. Starmall -> Sampol")
    print("2. Sampol -> Starmall")
    print("       Press 0 to end session")
    route = int(input("Choose route: "))

    if route == 1:
        while route == 1:
            clear()
            print("===================================")
            print("           Pick-Up Point")
            print("==================================")
            for index, locations in enumerate(starmall_sampol):
                print(f"{index+1}. {locations} ")
            print("    Press 0 to switch Route")
            print("==================================")
            From = int(input("Choose pick-up point: "))
            if From == 0:
                clear()
                print("Switching route...")
                time.sleep(3)
                break
            elif From >= 11:
                print("Invalid Input...")
                time.sleep(2)
                break
            To = int(input("Choose drop-off point: "))
            Quantity = int(input("Enter Quantity: "))
            print("===================================")
            print("             DISCOUNT")
            print("===================================")
            print("1. Student \n2. Senior Citizen \n3. PWD \n4. Regular")
            Discount = int(input("Enter Discount: "))
            if Discount in (1, 2, 3):
                clear()
                Total = fare[From-1][To-1] * 0.80
                DiscountFee = fare[From-1][To-1] * 0.20
                print("             GOORPU")
                print("===================================")
                type_writer(f"Driver's Name: {DriverName}")
                type_writer(f"Conductor's Name: {ConductorName}")
                type_writer(f"Body Number: {BodyNumber}")
                type_writer(f"Date and Time: {noms}\n")
                type_writer(f"From: {starmall_sampol[From -1]}")
                type_writer(f"To: {starmall_sampol[To -1]}")
                type_writer(f"Discount: {Discounts[Discount-1]}")
                type_writer(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * Quantity:.2f}")
                type_writer(f"Discount Amount: P{DiscountFee * Quantity:.2f} ")
                type_writer(f"Total: P{Total * Quantity:.2f}")
                boundary.append(Total * Quantity)
                time.sleep(3)
                continue
            elif Discount == 4:
                clear()
                DiscountFee = 0
                Total = fare[From-1][To-1]
                print("\n\n              GOORPU")
                print("===================================")
                type_writer(f"Driver's Name: {DriverName}")
                type_writer(f"Conductor's Name: {ConductorName}")
                type_writer(f"Body Number: {BodyNumber}")
                type_writer(f"Date and Time: {noms}\n")
                type_writer(f"From: {starmall_sampol[From -1]}")
                type_writer(f"To: {starmall_sampol[To -1]}")
                type_writer(f"Discount: {Discounts[Discount-1]}")
                type_writer(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * Quantity:.2f}")
                type_writer(f"Discount Amount: P{DiscountFee}")
                type_writer(f"Total: P{Total * Quantity:.2f}")
                boundary.append(Total * Quantity)
                time.sleep(3)
                continue
            else:
                print("Invalid Input...")
                time.sleep(3)
                break


    elif route == 2:
        while route == 2:
            clear()
            print("===================================")
            print("           Pick-Up Point")
            print("==================================")
            for index, locations in enumerate(sampol_starmall):
                print(f"{index+1}. {locations} ")
            print("    Press 0 to switch Route")
            print("==================================")
            From = int(input("Choose pick-up point: "))
            if From == 0: 
                print("Switching route...")
                time.sleep(3)
                break
            elif From >= 11:
                print("Invalid Input...")
                time.sleep(2)
                break
            To = int(input("Choose drop-off point: "))
            Quantity = int(input("Enter Quantity: "))
            print("===================================")
            print("             DISCOUNT")
            print("===================================")
            for index, discounts in enumerate(Discounts):
                print(f"{index+1}. {discounts}")
            Discount = int(input("Enter Discount: "))
            if Discount in (1, 2, 3):
                clear()
                Total = fare[From-1][To-1] * 0.80
                DiscountFee = Total * 0.20
                print("\n\n              GOORPU")
                print("===================================")
                type_writer(f"Driver's Name: {DriverName}")
                type_writer(f"Conductor's Name: {ConductorName}")
                type_writer(f"Body Number: {BodyNumber}")
                type_writer(f"Date and Time: {noms}\n")
                type_writer(f"From: {sampol_starmall[From -1]}")
                type_writer(f"To: {sampol_starmall[To -1]}")
                type_writer(f"Discount: {Discounts[Discount-1]}")
                type_writer(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * Quantity:.2f}")
                type_writer(f"Discount Amount: P{DiscountFee * Quantity:.2f}")
                type_writer(f"Total: P{Total * Quantity:.2f}")
                boundary.append(Total * Quantity)
                time.sleep(3)
                continue
            elif Discount == 4: 
                clear()
                DiscountFee = 0
                Total = fare[From-1][To-1]
                print("\n\n              GOORPU")
                print("===================================")
                type_writer(f"Driver's Name: {DriverName}")
                type_writer(f"Conductor's Name: {ConductorName}")
                type_writer(f"Body Number: {BodyNumber}")
                type_writer(f"Date and Time: {noms}\n")
                type_writer(f"From: {sampol_starmall[From -1]}")
                type_writer(f"To: {sampol_starmall[To -1]}")
                type_writer(f"Discount: {Discounts[Discount-1]}")
                type_writer(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * Quantity:.2f}")
                type_writer(f"Discount Amount: P{DiscountFee}")
                type_writer(f"Total: P{Total * Quantity:.2f}")
                boundary.append(Total * Quantity)
                time.sleep(3)
                continue
            else:
                print("Invalid Input...")
                continue
    elif route == 0:
        clear()
        MoneyCollected = sum(boundary)
        print(f"Total money collected: {MoneyCollected:.2f}")
        print("Thank You...")
        time.sleep(5)
        print("Enjoy the rest of the day...")
        time.sleep(5)
        break

    else:
        print("Invalid Input...")
