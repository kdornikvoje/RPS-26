
x = 5
y= 15
z = -10

print(x+y)
print(x-z)
print(x*z)
print(x/z)
print(10 % 3)

print(10**3)

print(10 // 3)

x = 3.14
y = 10.012

print(0.5+0.5 == 1)
print(0.1+0.2 == 0.3)

ime = "Luka"
print(len(ime))
st = "22"
print(st*100)
print(int(st)*100)

naslov = "Kidričeva 55   "
print(len(naslov))
print(naslov.upper())
print(naslov.lower())

naslov = naslov.strip()
print(len(naslov))

ime = "klemen Dornik"
imeUpper = ime.upper()
splIme = ime.split()
print(splIme)

print(type(splIme))
ime = splIme[0][0]

priimek = splIme[1][0]

inicialke = f"{ime} . {priimek}"
print(inicialke)


