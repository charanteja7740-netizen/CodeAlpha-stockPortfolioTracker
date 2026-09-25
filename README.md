# CodeAlpha Stock Portfolio Tracker

## About

This is a simple Stock Portfolio Tracker created as part of the CodeAlpha Python Programming Internship.

The program allows users to enter stock names and quantities and calculates the total investment based on predefined stock prices.

## Features

* Predefined stock prices using a Python dictionary
* Allows users to enter stock names
* Allows users to enter the quantity of stocks
* Calculates individual investment value
* Calculates total investment
* Handles unavailable stock names
* Saves the total investment to a text file

## Technologies Used

* Python
* Dictionary
* Loops
* Conditional statements
* User input
* File handling

## Available Stocks

* AAPL - $180
* TSLA - $250
* GOOGL - $150
* AMZN - $190
* MSFT - $420

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python stock_tracker.py
```

4. Enter the stock name and quantity when prompted.
5. Choose whether to add another stock.
6. The program displays the total investment.
7. The result is saved in `portfolio.txt`.

## Example

```text
Enter stock name: AAPL
Enter quantity: 5
Investment value: 900
Do you want to add another stock? (yes/no): no
Total investment: 900
Portfolio saved to portfolio.txt
```

## Project Files

* `stock_tracker.py` - Main Python program
* `portfolio.txt` - Saved portfolio report
* `README.md` - Project documentation
