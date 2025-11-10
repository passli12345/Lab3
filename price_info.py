price_list = {
    "apple": 2.0,
    "banana": 1.0,
    "orange": 1.5,
    "grape": 3.0
}

quantity_list = {
    "apple": 3,
    "banana": 5,
    "orange": 2,
    "grape": 1
}

def cost_of_fruit(fruit, quantity):
    if fruit in price_list:
        cost = price_list[fruit] * quantity
        print(f"Cost of {quantity} {fruit}(s): ${cost:.2f}")
        return cost
    else:
        print(f"{fruit} not found in price list.")
        return 0

def total_cost_shopping():
    total = 0
    for fruit in quantity_list:
        if fruit in price_list:
            total += price_list[fruit] * quantity_list[fruit]
    print(f"Total cost of shopping: ${total:.2f}")
    return total

if __name__ == "__main__":
    cost_of_fruit("apple", 4)
    total_cost_shopping()
