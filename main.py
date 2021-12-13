# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

első = int(input("Írj be egy számot!"))
második = int(input("Írj be egy számot!"))
harmadik = int(input("Írj be egy számot!"))

if első < második < harmadik:
  print(első, 'kisebb')
elif második > harmadik > első:
  print(második, 'kisebb')
else:
  print(harmadik, 'kisebb')