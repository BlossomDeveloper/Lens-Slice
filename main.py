toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#count how many times shows the $2 slices
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

#find the length of toppings
num_pizzas = len(toppings)

print("We sell ", num_pizzas, " different kinds of pizza!")

#created a new two-dimensional list with toppings and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

#sort pizza_and_prices
pizza_and_prices.sort()
print(pizza_and_prices)

#get the cheapest pizza from the list
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

#get the most expensive pizza on the list
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#remove last item as is out of stock
pizza_and_prices_prices.pop()
print(pizza_and_prices)

#add a new pizza to replace the one sold out
pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices)

#get the 3 cheapest pizzas from the list
three_cheapeast = pizza_and_prices[:3]
print(three_cheapeast)