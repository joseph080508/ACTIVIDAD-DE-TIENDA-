from register_sales import register_sales
from totals import calculate_totals
from summary import show_summary

def main():
    sales = register_sales()
    total = calculate_totals(sales)
    show_summary(sales, total)

main()
