price = [57.8, 46.51, 97, 23.35, 1.66, 4.78, 2.98, 33.45, 12.63, 9.99, 0.88, 12.45, 25, 70, 88.11]

print(id(price))

price.sort()

print(id(price))

for i in price:
  price_rub = int(i)
  price_kop = (i - price_rub) * 100
  
  print(f'{price_rub} руб. {price_kop:02.0f} коп.')

new_price = price
new_price.sort(reverse=True)
print(sorted(new_price)[-5:])