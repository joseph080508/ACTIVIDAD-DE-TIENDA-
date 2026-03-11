# Store Sales Registration System

## Description
This project is a simple Python program that allows a store administrator to register daily sales and generate a summary of the products sold and the total revenue of the day.

The program runs in the terminal and allows the user to enter multiple sales until they decide to stop.

## How the Program Works
The program is divided into different modules to keep the code organized and easy to understand.

### register_sales.py
This module is responsible for registering sales. 
It asks the user for:
- Product name
- Unit price
- Quantity sold

Each sale is stored in a list using a dictionary structure.

### totals.py
This module calculates the total revenue of the day. 
It multiplies the price by the quantity for each sale and adds the results to get the total amount.

### summary.py
This module displays a summary of the sales. 
It shows the product name, the quantity sold, and the total revenue.

### main.py
This is the main file that connects all the modules. 
It calls the functions to register sales, calculate totals, and display the summary.

## Technologies Used
- Python
- Terminal / Command Line

## Conclusion
This program helps automate the process of recording sales and calculating the total revenue of a store in a simple and organized way.
