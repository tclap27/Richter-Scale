#PYTHON RICHTER SCALE CALCULATION
#Your first and last name: Tom Clappsy
#Your ID: s1218375

#REQUIREMENTS:
# ask the user to "Enter the Richter scale value or -99 to end: "
# the program must end when the user enters -99
# the richter scale value entered must be greater than 0
# if the richter scale value is less than 0, the program must print  "Value must be greater than 0"
#   and the user must re-enter the richter scale value
# program must print the correct warning message for the richter scale value entered as per the accompanying diagram
# program must print only 1 warning message for each richter scale value entered
# the program must be tested so that it repeats until user enters -99
# the program must be tested so that if user enters a richter scale value less than 0,
#   "Value must be greater than 0" prints and the user must re-enter it
# the program must be tested with each of the following values to make sure the correct warning message is printed
#    8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
#-------------------------------------------------------------------------

# HINT: Use the base number conversion program for guidance
#--------------------------------------------------------------------------------------------
# 1. Develop the ALGORITHM for Richter Scale program from the requirements and enter it below
#--------------------------------------------------------------------------------------------
#   Input value
#   while(value is present)
#   quit entire program if input is = -99
#   make sure input is > 0, if not the loop through program until it is not
#   compare value input with comparisons
#   print out damage message depending on the value of the input
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 2. Convert the ALGORITHM to PSEUDOCODE and enter it below
#-------------------------------------------------------------------------
#   Write "Enter the Richter scale value or -99 to end: 
#   input value
#   quit program is input is = -99
#   restart program if input is <= 0
#   compare input with values
#   print out damage messages
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 3. Convert the PSEUDOCODE into PYTHON CODE and enter it below
#-------------------------------------------------------------------------

value = float(input("Enter the Richter scale value or -99 to end: "));
while True:
    if(value == -99):
        print("quitting");
        break;
    elif(value <= 0):
        print("Value must be greater than 0")
        value = float(input("Enter the Richter scale value or -99 to end: "));
    elif(value >= 8.0) :
        print("Most structures fall");
        break;
    elif(value >= 7.0 and value < 8.0):
        print("Many buildings destroyed");
        break;
    elif(value >= 6.0 and value < 7.0):
        print("Many buildings considerably damaged, some collapse");
        break;
    elif(value >= 4.5 and value < 6.0):
        print("Damage to poorly constructed buildings");
        break;
    else :
        print("No destruction of buildings");
        break;
            
        

            


