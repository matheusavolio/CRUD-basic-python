from crud.functions import *
from time import sleep
from colors import *

productList = []
productDict = {}

continueProgram = True

try:
    while continueProgram == True:
        try:
            menu = int(input("Choose one of the options below: \n"
                "[0] - exit: Be careful, "
                "if you leave the program,"
                "you will lose the product data \n"
                "[1] - Create product\n" # Create
                "[2] - Read products \n" # Read
                "[3] - Edit products\n"  # Update
                "[4] - Remove products\n"# Delete
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
            print("Thank you!, come back often!")
            break

        elif menu == 1:
            quantityProducts = int(input("Number of products to register: "))
            for c in range (1, quantityProducts+1):
                idProduct = c
                print   ()
                print(f"Enter product {c} data: ")
                nameProduct = str(input("Insert the name of product: "))
                priceProduct = float(input("Insert the price of product: R$"))
                addProducts(idProduct, nameProduct, priceProduct)
                print()
                sleep(1)

        elif menu == 2:
            readProduct()

        elif menu == 3:
            searchId = int(input("Insert ID of the product that will be updated: "))
            nameUpdated = str(input("Inser the new name of product: "))
            priceUpdated = float(input("Insert the new price of product: R$"))
            updateProduct(searchId, nameUpdated, priceUpdated)

except Exception as e:
     print(f"{red}Erro! {e.__class__}{e.__cause__}{reset}")