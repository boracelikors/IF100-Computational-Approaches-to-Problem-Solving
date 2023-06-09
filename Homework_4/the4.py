while True:
  yil = int(input("Enter the year: "))
  if yil == 2017 or yil == 2018:
    break
if yil == 2018:
  while True:
    ay = int(input("Enter the month: "))
    if ay == 1:
      break
elif yil == 2017:
  while True:
    ay = int(input("Enter the month: "))
    if ay in range(1,13):
      break

filem = open("turkiye_spotify_data.txt","r")
db = filem.readlines()
filem.close()

db.pop(0)
db2 = []
dbay = []
isim_link = {}
isim_stream = {}
isim_stream_toplam = {}
dilan = []
dilanım = []

#tr ve boşluğu çıkar
for i in db:
  x = i.strip()
  db2.append(x)

#aylara ayır
for i in db2: 
  inlist = i.split("-")
  ayı = int(inlist[-2])
  if ayı == ay and inlist[-3][-1] == str(yil)[-1]:
    dbay.append(i)


"""
buraya kadar sorunsuz
"""





for i in dbay:
  bora = i.split("\t")
  if f"{bora[1]}, {bora[2]}" not in isim_stream:
    isim_stream[f"{bora[1]}, {bora[2]}"] = int(bora[3])
  else:
    isim_stream[f"{bora[1]}, {bora[2]}"] += int(bora[3])
  isim_link[f"{bora[1]}, {bora[2]}"] =bora[4]




sorted_dict = sorted(isim_stream.items(), key=lambda x:x[1], reverse=True)

for i,j in sorted_dict:
  dilan.append(i)
  dilanım.append(j)




print(f"NEW SUGGESTION: {dilan[0]} (Total stream number in this month: {dilanım[0]})")



while True:
  imha = input("Do you want to listen this song (enter either yes or no): ").lower()
  if imha == "no":
    dilan.pop(0)
    dilanım.pop(0)
    print(f"NEW SUGGESTION: {dilan[0]} (Total stream number in this month: {dilanım[0]})")
  
  
  if imha == "yes":
    print(f"Enjoy {dilan[0]}. Here is the url for you: {isim_link[dilan[0]]}")
    break
  
  
  
    
  

  





