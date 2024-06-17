def make_pizza(*topings, Base):
    print(topings, Base)


print("Add following toppings to my pizza with the mentioned Base")
make_pizza('olives', 'onion', 'Mushroom', 'Tomato', Base='Thin Crust')
