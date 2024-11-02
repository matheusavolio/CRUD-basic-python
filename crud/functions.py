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
            
# def updateProduct():
