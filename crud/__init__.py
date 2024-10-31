productList = []
productDict = {}

def addProducts(id, name, price):
        productDict = {"Id":id, "name":name, "Price":price}
        productList.append(productDict)
        return productList

def readProduct():
    if not productList:
        print("No products registered.")
    else:
        for product in productList:
            return (f'Id of product: {product["Id"]}\n'
            'Name of product: {product["Name"]}\n'
            'Price of product: R${product["Price"]:.2f}')
            print()
