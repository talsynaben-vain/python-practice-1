name = input("Name: ")
km = float(input("Distance: "))
cons = float(input("Consumption: "))
price = float(input("Price: "))

litres = km * cons / 100
cost = litres * price
per_km = cost / km

print(name)
print(km)
print(cons)
print(price)

print(litres)
print(cost)
print(per_km)

print(km > 300)
print(cost > 5000)
