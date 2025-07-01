#Import functions from all modules
from read import product_read
from write import bill, restock_bill
from operation import display, sell, update, restock

#Start main loop
while True:
    #Display option
    print("1. Sell")
    print("2. Restock")
    print("3. Exit")
    try:
        opt = int(input("How would you like to continue (1/2/3): "))
    except ValueError:
        #handle number format
        print("Invalid option")
        continue

    if opt == 1:
        product_display = product_read()
        pdictionary, count = display(product_display)
        selected, p_quantity, total, free_items, brand = sell(pdictionary, count)#Selling process
        name = input("Enter customer name: ")
        bill(name, selected, p_quantity, total, free_items, brand)#Generate and write bill
        update(pdictionary)

    elif opt == 2:
        product_display = product_read()
        pdictionary, count = display(product_display)
        restock_products=restock(pdictionary)
        if restock_products:
            vendorname, selected, p_quantity, total, brand = restock_products
            update(pdictionary)
            restock_bill(vendorname, selected, p_quantity, total, brand)#Generate bill

    elif opt == 3:
        print("Thank you for choosing WeCare")
        break #Exit loop
    else:
        print("Invalid option")
