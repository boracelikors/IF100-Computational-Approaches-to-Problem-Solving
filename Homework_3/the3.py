db = input("Please enter the database: ")
pieces = db.split(",")
isimler = []
akimlar = []
fiyatlar = []
for i in pieces:
  isim = i.split(":")
  isimler.append(isim[0])
  akim = isim[1].split(";")
  akimlar.append(akim[0])
  fiyatlar.append(akim[1])
aranan_akim = input("Please enter the movement name that you want to purchase: ")
if aranan_akim not in akimlar:
  print(f"There are no paintings belonging to {aranan_akim}.")
else:
  butce = float(input("Please enter the amount of money you have (in million): "))
  eser = input("Please enter the name of the painting that you want to buy: ")
  if eser.count(",") == 0:
    if eser not in isimler:
      print(f"{eser} is not in the database.")
    elif akimlar[isimler.index(eser)] != aranan_akim:
      print(f"{eser} does not belong to {aranan_akim} movement.")
    elif float(fiyatlar[isimler.index(eser)].replace("M","")) > butce:
      print(f"Willing painting(s) value(s) are higher than your current budget.")
    else:
      print(f"You have successfully purchased {eser}.")
  else: 
    eserler = eser.split(",")
    a = len(eserler)
    b = 0
    paracik = 0
    for i in eserler:
      if i not in isimler:
        print(f"{i} is not in the database.")
      elif akimlar[isimler.index(i)] != aranan_akim:
        print(f"{i} does not belong to {aranan_akim} movement.")
      else:
        paracik += float(fiyatlar[isimler.index(i)].replace("M",""))
        b += 1
    if b == a and paracik > butce:
      print("Willing painting(s) value(s) are higher than your current budget.")
    elif b == a:
      print(f"You have successfully purchased {eser}.")

        
       

    


    









