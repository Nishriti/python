#Function to read file
def product_read():
    try:
        #open file in read mode
        file=open("products.txt", "r")#read data
        product_display=file.read()
        file.close()
        return product_display
    #Handle case when file not found
    except FileNotFoundError:
        print("File not found.")
        return ""
    #Handle other exception
    except Exception as e:
        print("Error reading file", e)
        return 
