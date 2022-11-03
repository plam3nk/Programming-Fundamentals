products = input().split()
searching_products = input().split()
stock = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index+1]
    stock[key] = value

for item in searching_products:
    if item in stock.keys():
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
