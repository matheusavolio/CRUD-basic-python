from time import sleep
productList = []
productDict = {}

def addProducts(id, name, price):
        productDict = {"Id":id, "Name":name, "Price":price}
        productList.append(productDict)
        return productList

def readProduct():
    if not addProducts:
        print("No products registered.")
    else:
        for product in productList:
            print (
            f'Id of product: {product["Id"]}\n'
            f'Name of product: {product["Name"]}\n'
            f'Price of product: R${product["Price"]:.2f}'
            )
            print()
            sleep(1)
            
def updateProduct(update, nameUpdate, priceUpdate):
    for product in productList:
        if product["Id"] == update: 
            product["Name"] = nameUpdate
            product["Price"] = priceUpdate
        else:
            print("Product Id not found.")