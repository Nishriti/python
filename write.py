import datetime
#Function to display and generate bill
def bill(name, selected, p_quantity, total, free_items, brand):
    try:
        print("\n\n\n")
        print("\t\t       WeCare Store    ")
        print("\t\t  -----------------------   ")
        print("Billed to:")
        print(name, "\n")
        #Generate current date and time
        date=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().month)
        time=str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)
        print(date + "  (" + time + ")")
        print("-" * 65)
        print("Sn \t Product \tBrand \tQuantity ")
        print("-" * 65)
        #Purchased item
        for i in range(len(selected)):
            print(i + 1, "\t", selected[i], "\t", brand[i], "\t", p_quantity[i])
        print("\n")
        print("-" * 20)
        print("Total amount: ", total)
        print("-" * 65)
        #free items
        if free_items != 0:
            print("You got ", free_items, "free products")
            print("-" * 65)

        print("Thank you for your purchase.")
        print("-" * 65)
        print("Products once purchased cannot be returned or exchanged")
        print("-" * 65)
    except Exception as e:
        print("There was an error while writing bill", e)
    #Write bill invoice to file
    w=open(name, "w")
    w.write("\n\n\n")
    w.write("\t\t       WeCare Store    \n")
    w.write("\t\t  -----------------------   \n")
    w.write("Billed to:\n")
    w.write(name + "\n\n")
    w.write(date + "  (" + time + ")\n")
    w.write("-" * 65 + "\n")
    w.write("Sn \t Product \t\tBrand \t\tQuantity\n")
    w.write("-" * 65 + "\n")
    for i in range(len(selected)):
        w.write(str(i+1)+"\t"+str(selected[i])+"\t\t"+str(brand[i])+"\t\t"+str(p_quantity[i]))
        w.write("\n")
    w.write("-" * 20 + "\n")
    w.write("Total amount: " + str(total) + "\n")
    w.write("-" * 60 + "\n")
    if free_items != 0:
        w.write("You got " + str(free_items) + " free products \n")
        w.write("-" * 60 + "\n")
    w.write("Thank you for your purchase.\n")
    w.write("-" * 60 + "\n")
    w.write("Products once purchased cannot be returned or exchanged \n")
    w.write("-" * 60 + "\n")

#Function to generate and write bill
def restock_bill(vendorname, selected, p_quantity, total, brand):
    try:
        #Calculate vat and total
        vat = (total * 0.13)
        grandtotal = total + vat
        print("\n\n\n")
        print("\t\t       WeCare Store    ")
        print("\t\t  -----------------------   ")
        print("Billed to:")
        print(vendorname, "\n")
        #Generate current date and time
        date=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().month)
        time=str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)
        print(date + "  (" + time + ")")
        print("-" * 60)
        print("Sn \t Product \t\tBrand \t\tquantity ")
        print("-" * 60)
        #List restocked items
        for i in range(len(selected)):
            print(i + 1, "\t", selected[i], "\t\t", brand[i], "\t\t", p_quantity[i])
        print("\n")
        print("-" * 20)
        print("Sub Total: ", total)
        print("-" * 20)
        print("Vat=13%")
        print("grand Total: ", grandtotal)
        print("-" * 60)
    except Exception as e:
        print("There was an error", e)
    #Write restock invoice to file
    w=open(vendorname, "w")
    w.write("\n\n\n")
    w.write("\t\t       WeCare Store    \n")
    w.write("\t\t  -----------------------   \n")
    w.write("Billed to:\n")
    w.write(vendorname + "\n")
    w.write(date + "  (" + time + ")\n")
    w.write("-" * 60 + "\n")
    w.write("Sn \t Product \t\tBrand \t\tquantity \n")
    w.write("-" * 60 + "\n")
    for i in range(len(selected)):
        w.write(str(i+1)+"\t"+str(selected[i])+"\t\t"+str(brand[i])+"\t\t"+str( p_quantity[i]))
        w.write("\n")
    w.write("-" * 20 + "\n")
    w.write("Sub Total: " + str(total) + "\n")
    w.write("-" * 20 + "\n")
    w.write("Vat=13%\n")
    w.write("Grand Total: " + str(grandtotal) + "\n")
    w.write("-" * 60 + "\n")
