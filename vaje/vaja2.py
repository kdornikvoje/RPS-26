def izpis(s:list):
    print("----------------")
    for index in range(len(s)):
        print(f"({index + 1}) {s[index]}")
        
def vnos(s:list):
    while True:
        izdelek = input("Vnesi: ").lower()
        if izdelek == "":
            break
        s.append(izdelek)

def posodobi(s:list):
    kaj = input("Spremeni: ").lower()
    za = input("Za: ").lower()
    for index in range(len(s)):
        if s[index] == kaj:
            s[index] = za
        


def briši(s:list):
    brisi = input("Briši: ").lower()
    print("Brišem: ", end="")
    while brisi in s:
        s.remove(brisi)
        print("*", end="")
    print()


if __name__ =="__main__":
    db = []
    vnos(db)
    izpis(db)
    briši(db)
    izpis(db)
    posodobi(db)
    izpis(db)