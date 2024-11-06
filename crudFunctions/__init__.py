from time import sleep
from colors import *
productList = []
productDict = {}

def addProducts(id, name, price):
        productDict = {"Id":id, "Name":name, "Price":price}
        productList.append(productDict)
        productDict.clear
        print(f"{green}Product added sucessfully!{reset}")
        

def readProduct():
        try:
            for product in productList:
                print (
                f'Id of product: {product["Id"]}\n'
                f'Name of product: {product["Name"]}\n'
                f'Price of product: R${product["Price"]:.2f}'
                )
                print()
                sleep(0.5)
        except Exception as e:
            print(f"{red}Error! {e.__cause__} - - {e.__class__} {reset}")  ## erro ao ler lista após id ser removide: KeyError product["Id"]

    
            
def updateProduct(updateId, nameUpdate, priceUpdate):
        for product in productList:
            if product["Id"] == updateId: 
                product["Name"] = nameUpdate
                product["Price"] = priceUpdate
                print(f"{green}Product updated successfully{reset}")
                print()
                sleep(1)
                return
                

def delProduct(Id):
            for product in productList:
                if product["Id"] == Id:
                    productList.remove(product)
                    print(f"{green}Product removed sucessfully!{reset}")
                    sleep(1)
                    return