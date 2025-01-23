def viJaFurzis():
    print("Kial vi pensis, ke mi furzis?")
    eniri1 = input()
    if eniri1 == "Mi ne scias":
        print("Vi ja scias, sed vi ne parolas ĝin al mi!")
    else:
        print("Bone, foriru")

print("Saluton! Kiel vi nomiĝas?")
nomo = input()
if nomo == "Kial vi furzis?":
    print("Mi neniam furzas")
else:
    print("Mi ŝatas "+nomo+". Ĝi estas bona nomo!")

print("Kio estas via favorata koloro?")
koloro = input()
if koloro == "ruĝa":
  print("Mi ne povas paroli")
elif koloro == "oranĝa":
  print("Mi tre ŝatas ĉi tiun koloron!")
elif koloro == "flava":
  print("Ĉi tiu koloro estas aĉa.")
elif koloro == "verda":
  print("Verda - la koloro de Esperanto - ĝi estas bonega!")
elif koloro == "blua":
  print("Ĉi tiu koloro estas aĉa.")
elif koloro == "violkolora":
  print("Ĉi tiu koloro estas aĉa.")
elif koloro == "Vi ja furzis":
    print("Neniel! Mi ne furzis")
    viJaFurzis()
else:
  print(koloro,"estas mia favorata koloro(!)")
