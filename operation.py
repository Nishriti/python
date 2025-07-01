#Function to display product details
def display(product_display):
    print("-" * 90)
    print("ID \t ProductName \t Brand \t\t Quantity \tPrice \t origin")
    print("-" * 90)

    #Split input into lines for each product
    productList=product_display.split('\n')
    while '' in productList:
        productList.remove('') #remove empty lines

    count=len(productList)

    #Number of products

    pdictionary = {}
    
    #Store product data in dictionary
    for i in range(1, count + 1):
        pdictionary[i] = productList[i - 1].split(",")
        #Display product after calculated price
    for key, value in pdictionary.items():
        print(key, end="\t")
        for i in range(len(value)):
            if i == 3:
                print("\t", int((int(value[i]) * 200) / 100), end='\t')
            elif i == 1:
                print(value[i], end="\t")
            else:
                print(value[i], end="\t")
        print("\n")
    print("-" * 90)
    return pdictionary, count #Return product dictionary and number of items

#Selling products
def sell(pdictionary, count):
    selected = []
    p_quantity = []
    brand = []
    total = 0
    free_items = 0

    while True:
        try:
            product_id = int(input("Please enter the id of the product you would like to purchase: "))
            if product_id <= 0 or product_id > count:
                print("Enter the correct id from list")
                continue
            brandname = input("Enter brand name: ")
            brand.append(brandname)
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                print("Quantity invalid")
                continue
            available = int(pdictionary[product_id][2])#availabe stock 

            if quantity <= available:
                selected.append(pdictionary[product_id][0])
                free = quantity // 3 #apply buy 3 get 1 free
                total_quantity = quantity + free

                if total_quantity > available:
                    pdictionary[product_id][2] = str(available - quantity)
                    total += (quantity - free) * int(pdictionary[product_id][3]) * 2
                    p_quantity.append(quantity)
                else:
                    pdictionary[product_id][2] = str(available - total_quantity)
                    total += quantity * int(pdictionary[product_id][3]) * 2
                    p_quantity.append(total_quantity)
                free_items += free
            else:
                print("Available stock: " + str(available))
                continue
            ask = input("Do you want to buy more products? (y/n): ")
            if ask.lower() == 'n':
                break
        except ValueError:
            print("Please enter number as ID")
            continue

    return selected, p_quantity, total, free_items, brand

#Function to update product file
def update(pdictionary):
    with open("products.txt", "w") as file:
        for value in pdictionary.values():
            line = ",".join(value) + "\n"
            file.write(line)

#Function to restock product
def restock(pdictionary):
    try:
        vendorname = input("Enter vendor's name: ")
        product_id = int(input("Enter product id: "))
        #Check if id exist
        if product_id in pdictionary:
            brand= input("Enter brand name: ")
            qty = int(input("Enter quantity: "))
            if qty < 0:
                print("Quantity invalid")
                return None
            pdictionary[product_id][2] = str(int(pdictionary[product_id][2]) + qty)
            print("\nProduct restocked")
            selected = [pdictionary[product_id][0]]
            p_quantity = [qty]
            price = int(pdictionary[product_id][3]) * 2
            total = qty * price
            return vendorname, selected, p_quantity, total, brand
        else:
            print("Enter correct id")
            return None
    except ValueError:
        print("Enter number as ID")
        return None
