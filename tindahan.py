menu = {"Rice" : 15,
        "Adobo": 65,
        "Sisig": 70,
        "Tinola": 65,
        "Hotdog": 25,
        "Burjir": 30,
        "Fries": 30,
        "Sopdrink": 22,
        "Bagnet": 120,
        "Igado": 65,
        }

cart = []
total = 0
print("---------MENU---------")
for key, value in menu.items():
    print(f"{key}: ₱{value:.2f}")
print("----------------------")

while True:
    food = input("Select an item (Q to quit): ").title()
    if food == 'Q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------ORDERS---------")
for food in cart:
    total += menu.get(food)
    print(food,end=", ")


print()
print(f"Total is ₱{total:.2f}")
print("---------TOTAL---------")
