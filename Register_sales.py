
def register_sales():

    sales = []
    validation = True

    while validation:
        try: 
            
            product = input("Product name: ")
            price = float(input("Unit price: "))
            quantity = int(input("Quantity: "))
            if price < 0 or quantity < 0:
                print("Price and quantity must be non-negative. Please try again.")
                continue
            elif product.isalpha() == False:
                print("Product name must contain only letters. Please try again.")
                continue

            sale = {
                "product": product,
                "price": price,
                "quantity": quantity
            }

            sales.append(sale)

            option = input("Register another sale? (yes/no): ").lower()

            if option == "no":
                validation = False
                return sales
        except ValueError:
            print("Invalid input. Please enter valid data.")
            
            