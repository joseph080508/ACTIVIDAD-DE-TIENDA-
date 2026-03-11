def register_sales():

    sales = []
    validation = True

    while validation:

        product = input("Product name: ")
        price = float(input("Unit price: "))
        quantity = int(input("Quantity: "))

        sale = {
            "product": product,
            "price": price,
            "quantity": quantity
        }

        sales.append(sale)

        option = input("Register another sale? (yes/no): ")

        if option == "no":
           validation = False
