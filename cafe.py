# create a list with 4 items in a cafe
menu = ["pastries", "sandwiches", "coffee", "salad"]
# create a dictionary containing stock values
stock = {'pastries': 30, 'sandwiches': 100, 'coffee': 100, 'salad': 40}
# create a dictionary containing price values
price = {'pastries': 4.50, 'sandwiches': 6.50, 'coffee': 3.50, 'salad': 5.50}
# calculate the total stock value and output it to user
total_stock_worth = 0

for item in menu:
    item_stock = stock[item]
    item_price = price[item]
    item_value = item_stock * item_price
    total_stock_worth += item_value

print("Total Stock Worth in the Cafe: £{:.2f}".format(total_stock_worth))
