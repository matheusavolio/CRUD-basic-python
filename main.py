from crudFunctions import *
from time import sleep
from colors import *

continueProgram = True
menu = True

while continueProgram == True:
    try:
        menu = int(input("Choose one of the options below: \n"
                "[0] - exit: Be careful, "
                "if you leave the program,"
                "you will lose the product data \n"
                "[1] - New register\n" # Create
                "[2] - Read registers \n" # Read
                "[3] - Edit registers\n"  # Update
                "[4] - Remove registers\n"# Delete
                "You option: "))
            
        if menu not in [0, 1, 2, 3, 4]:
            errorMessage("Invalid option! Please enter a number between 0 and 4.")
    except ValueError:
        errorMessage("Error! Enter a valid number between 0 to 4")
    except KeyboardInterrupt:
            errorMessage("Error! Please enter a valid number.")
    finally:
        formatting()
            
    if menu == 0:
        continueProgram = False
        sucessMessage("Thank you!, come back often!")
        break

    elif menu == 1:
            quantityRegister = 0
            try:
                quantityRegister = int(input("number of registrations to register: "))
            except (ValueError, TypeError, KeyboardInterrupt):
                errorMessage("Error! Please enter a valid number.")
                formatting()
            for c in range (1, quantityRegister+1):
                newId = c
                print()
                print(f"Enter register {c} data: ")
                try:
                    newName = str(input("Insert you name: "))
                    newEmail = str(input("Insert you email: "))
                    newPassword = int(input("You password: "))
                except (TypeError, ValueError, KeyboardInterrupt):
                    errorMessage("Error! Please enter a valid caractere.")
                    formatting()
                newRegister(newId, newName, newEmail, newPassword)
                formatting()

    elif menu == 2:
                viewRegisters()

    elif menu == 3:
                try:
                    searchId = int(input("Insert ID of the product that will be updated: "))
                    nameUpdated = str(input("Inser the new name: "))
                    emailUpdate = str(input("Insert the new email: "))
                    updatePassword = int(input("Insert you new password: "))
                    uptadeRegister(searchId, nameUpdated, emailUpdate, updatePassword)
                except (ValueError,KeyboardInterrupt, TypeError):
                    errorMessage("Error! Enter a valid number.")
                

    elif menu == 4:
            idDel = int(input("Enter the id product to be delete: "))
            deleteRegister(idDel)
