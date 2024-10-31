from crud import *
productList = []
productDict = {}
continueProgram = True

while continueProgram == True:

    menu = int(input("Choose one of the options below: \n"
    "[0] - exit. Be careful,"
    "if you leave the program,"
    "you will lose the product data \n"
    "[1] - Create product\n" # Create
    "[2] - Read products \n" # Read
    "[3] - Edit products\n"  # Update
    "[4] - Remove products\n"# Delete
    "You option: "))
    print()


    if menu == 0:
        continueProgram = False
        break

    if menu == 1:
        quantityProducts = int(input("Number of products to register: "))
        for c in range (1, quantityProducts+1):
            idProduct = c
            print   ()
            print(f"Enter product {c} data: ")
            nameProduct = str(input("Insert the name of product: "))
            priceProduct = float(input("Insert the price of product: R$"))
            addProducts(idProduct, nameProduct, priceProduct)
            print()
    elif menu == 2:
        readProduct()