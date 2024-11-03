from time import sleep
from colors import *
productList = []
productDict = {}

def addProducts(id, name, price):
        productDict = {"Id":id, "Name":name, "Price":price}
        productList.append(productDict)
        print(f"{green}Product added sucessfully!{reset}")
        return productList

def readProduct():
    if not productList:
        print(f"{red}No products registered.{reset}")
        print()
        sleep(1)
    else:
        for product in productList:
            print (
            f'Id of product: {product["Id"]}\n'
            f'Name of product: {product["Name"]}\n'
            f'Price of product: R${product["Price"]:.2f}'
            )
            print()
            sleep(1)
            
def updateProduct(updateId, nameUpdate, priceUpdate):
        for product in productList:
            if product["Id"] == updateId: 
                product["Name"] = nameUpdate
                product["Price"] = priceUpdate
                print(f"{green}Product updated successfully{reset}")
            else:
                print(f"{red}Insert a valid product id!{reset}")
                print()
                sleep(1)
                return productList

def delProduct(Id):
    for product in productList:
        if product["Id"] not in productList:
            print(f"{red}Product id not found!{reset}")
            sleep(1)
        else:
            for i, product in enumerate(productList):
                if product["Id"] == Id:
                    del product[i]
                    print(f"{green}Product removed sucessfully!{reset}")
                    sleep(1)
                    return productList
                    