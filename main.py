#1.uzdevums
cena=2.35
daudzums=int(input("Ievadi preces daudzumu: "))
maksa=cena*daudzums
if daudzums>2:
  maksa=maksa*0.90
print(maksa)
print("----------------------")