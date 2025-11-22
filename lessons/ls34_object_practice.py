"""A demonstration of classes and objects"""

class Pizza:
    "A simple model of a Pizza"
    size: str = "medium"
    extra_cheese: bool = False
    toppings: int = 0

def main() -> None:
    "Entrypoint of Program"
    a_pizza: Pizza = Pizza()
    a_pizza.size = "small"
    a_pizza.toppings = 0
    a_pizza.extra_cheese = True
    print("Size " + a_pizza.size)
    print("Toppings: " + str(a_pizza.toppings))
    print("Price: " + str(price(a_pizza)))

def price(a_pizza: Pizza) -> float:
    "takes in a pizza and returns its price"
    price: float = 7.0
    if a_pizza.size == "medium":
        price = 9.0
    elif a_pizza.size == "large":
        price = 11.0
    if a_pizza.extra_cheese == True:
        price += 1.0
    if a_pizza.toppings > 0:
        price += float(a_pizza.toppings) * 0.75
    return price


if __name__ == "__main__":
    main()