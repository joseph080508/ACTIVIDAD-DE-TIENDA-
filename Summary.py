def show_summary(sales, total):

    print("SALES SUMMARY")

    for sale in sales:
        print("Product:", sale["product"])
        print("Quantity sold:", sale["quantity"])
        print("Price:", sale["price"])
        print()

    print("Total revenue:", total)