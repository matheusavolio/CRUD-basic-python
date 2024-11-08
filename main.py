from crudFunctions import *
from time import sleep
from colors import *

continueProgram = True


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
            print("Invalid option! Please enter a number between 0 and 4.")
    except ValueError:
        print(f"{red}Error! Enter a valid number between 0 to 4{reset}")
    except KeyboardInterrupt:
            print(f"{red}Error! Please enter a valid number.{reset}")
    finally:
        sleep(1)
        print()
            
    if menu == 0:
        continueProgram = False
        print(f"{red}Thank you!, come back often!{reset}")
        break

    elif menu == 1:
            quantityRegister = int(input("Number of products to register: "))
            for c in range (1, quantityRegister+1):
                newId = c
                print ()
                print(f"Enter register {c} data: ")
                newName = str(input("Insert you name: "))
                newEmail = str(input("Insert you email: "))
                newPassword = int(input("You password: "))
                newRegister(newId, newName, newEmail, newPassword)
                print()
                sleep(1)

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
                    print(f"{red}Error! Enter a valid number.{reset}")
                

    elif menu == 4:
            idDel = int(input("Enter the id product to be delete: "))
            delRegister(idDel)
