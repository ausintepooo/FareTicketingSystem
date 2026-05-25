# User Guide for Fare Ticketing

## Introduction 
The Fare Ticketing System is a Python-based terminal system,  
designed to help jeepney or transport operators, and manage  
passenger fares from the starmall ↔ sampol route.  

The system:  
- Calculates passenger fares
- Applies disscounts automatically
- Prints a ticket like summary
- Tracks total money collected during the session

## System Requirements
Before running the system, make sure you have:  
- Python 3 Installed  
- A terminal or command prompt to check if Python is installed:  
- Type on the terminal (python --version)  

## How to Run the Program
Save the code as: 

1. Any file name that can be easily identified then add ".py" at the end, ex. (Goorpu.py)  
2. Open terminal or command prompt  
3. Navigate to the folder where the file is saved  
4. Run the program  
5. python goorpu.py

## Starting the system
When the program starts, the system will ask for the following:

Enter Driver Name:  
Enter Conductor Name:  
Enter Body Number:  
- Example:  
Enter Driver Name: Johnrick  
Enter Conductor Name: Stephen   
Enter Body Number: 101  

After entering the information, the system displays:  
Good Day Johnrick and Stephen 

## Main menu
The system will display the route of menu:  
  
<img width="250" height="70" alt="image" src="https://github.com/user-attachments/assets/7e0d340d-4789-453f-b0f6-406dc2b33460" />
 
1. Starmall -> Sampol  
2. Sampol -> Starmall  

Press 0 to end session  
Menu Options  
Option Description  
1 Travel from Starmall to Sampol  
2 Travel from Sampol to Starmall  
0 End the session  

## Selecting a Route
Choose a route by typing the corresponding number.  
Example  
Choose route: 1  

## Selecting Pick-up and Drop-off Points 
After selecting a route, the system will display all available locations.

Example  
Starmall  
Bulacan State University  
Carissa 4B  
.....  
Sampol  

## Steps
Step 1 - Choose Pick-Up Point  
Choose pick-up point:  
Step 2 - Choose Drop-off Point  
Choose drop-off point:  
Step 3 - Enter Passenger Quantity  
Enter Quantity:  

## Discount Selection:
The system supports the following discounts:  
1. Student  
2. Senior Citizen  
3. PWD  
4. Regular  

Discount Rules  
Type Discount:  
Student = 20%  
Senior Citizen = 20%  
PWD = 20%  
Regular = No Discount  

## Fare Computation
The system automatically computes:  

Base Fare  
Discount Amount  
Total Fare  

Formula Used  
For discounted passengers:
Total Fare = Base Fare x 0.80 x Quantity  

For Regular passengers:    
Total Fare = Base Fare x Quantity

## Ticket Output
After entering all information, the system prints a ticket summary.

Example Output:  
<img width="240" height="70" alt="image" src="https://github.com/user-attachments/assets/bcc29566-405c-445f-9467-0966ead7ccaf" />

Driver's Name: Johnrick  
Conductor's Name: Stephen  
Body Number: 101  
Date and Time: 2026-05-15  11:30:00  

From: Starmall  
To: Sampol  
Discount: Student  
Fare: P23.00 x 2 = 46.00  
Discount Amount: P9.20  
Total: P36.80  

## Switching Routes
To switch routes:  
Press 0 to switch route  
The system returns to the main route menu.  

## Ending the Session
1. Return to the Route Menu  
2. Press 0  
The system dispplay the total money collected.  

## Example:
Total money collected: 560.00  
Thank You...  

## Error Handling
Error:  
Invalid input  
Program crashes  
Route not switching  

Cause:  
Wrong menu number entered  
Non-numeric input  
Incorrect route selection  

Solution:  
Enter valid option only
enter numbert only
press 0 to return 

## Features of the System
- Automated fare computation  
- Discount processing  
- Digital receipt generation  
- Passenger trip recording  
- Total earnings computation  
- bidirectiona; route management  

## Developers: 
- Johnrick Ausinte  
- Janine Garcia  
- Stephen Osita  
- Julia Regino  
- Christian Salas  

## Conclusion
The E-jeep Ticketing System improves the efficiency of fare management  
and helps drivers and conductors provide faster and more accurate  
service to passengers through automated fare calculation and receipt 
generation.  
