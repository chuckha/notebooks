import json
import time
import random

random.seed(10)

def generate_items(num_items=10):
    return [
        Item(
            random.randint(10000,900000),
            round(random.randint(1, 20) + random.random(), 2)
        ) for _ in range(num_items)
    ]

class Item():
    def __init__(self, id, price):
        self.id = id
        self.price = price

class User():
    def __init__(self, id):
        self.id = id

def generate_users(num_users=10):
    return [
        User(
            random.randint(100000,83938283),
        ) for _ in range(num_users)
    ]

class Event():
    def __init__(self, name, t, properties):
        self.name = name
        self.timestamp = t
        self.properites = properties

class View(Event):
    def __init__(self, t, properties):
        super().__init__('view', t, properties)

class AddToCart(Event):
    def __init__(self, t, properties):
        super().__init__('add_to_cart', t, properties)

class Checkout(Event):
    def __init__(self, t, properties):
        super().__init__('checkout', t, properties)

class Search(Event):
    def __init__(self, t, properties):
        super().__init__('search', t, properties)

user_profiles = [
    # very good customer
    [Search, View, AddToCart, Search, View, AddToCart, Checkout,],

    # indecisive customer
    [Search, View, View, Search, View, Search, View, View, View, AddToCart, Checkout],

    # browsing
    [Search, View, Search, View, Search, View,],

    # knows what they want
    [Search, View, AddToCart, Checkout,],

    # buys a few times
    [Search, View, AddToCart, Checkout, Search, View, AddToCart, Checkout,],

    # adds a few items to cart and checksout
    [Search, View, AddToCart, Search, View, AddToCart, Checkout,],

    # searching for the unknown
    [Search, Search, Search, Search, Search,],
]

def generate_user_ids(num_users=10):
    return {random.randint(1000000, 8000000) for x in range(num_users)}

terms = [
    'rings',
    'jewelry',
    'shirts',
    'dog toys',
    'cards',
    'glassware',
]

def main():
    num_visits = 20

    items = generate_items()
    users = generate_users()
    # pick a user
    events = []
    for _ in range(num_visits):
        time = 1515212399 + random.randint(0, 5)
        user = random.choice(users)
        profile = random.choice(user_profiles)
        item = None
        cart = []
        for c in profile:
            properties = {
                'user_id': user.id,
            }
            if c == Search:
                properties['query'] = random.choice(terms)
                item = random.choice(items)
                time += random.randint(1, 3)
            elif c == View:
                properties['item_id'] = item.id
                time += random.randint(5, 10)
            elif c == Checkout:
                properties['price'] = sum([item.price for item in cart])
                properties['item_ids'] = [item.id for item in cart]
                time += random.randint(30, 60)
            elif c == AddToCart:
                properties['item_id'] = item.id
                cart.append(item)
                time += 1
            events.append(c(time, properties))

    for event in events:
        print(json.dumps(event.__dict__))

    # assign a profile
#    print([json.dumps(v.__dict__) for _, v in items.items()])


if __name__ == "__main__":
    main()
