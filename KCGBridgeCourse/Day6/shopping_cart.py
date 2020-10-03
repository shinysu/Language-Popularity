cart = []
print(cart)

cart.append('chocolates')
print(cart)
print(len(cart))

cart.extend(['bread', 'butter'])
print(cart)

cart.insert(0, 'ice cream')

cart = ['ice cream', 'chocolates', 'bread', 'butter']
print(cart[3:0:-1])

new_cart = sorted(cart)
print("cart= ",cart)
print("new_cart")

for item in cart:
    print(item)