def hello():
    oddelek = input("Vnesi oddelek: ")
    if oddelek.upper() == "1.RI":       
        print(f"Hello {oddelek} ♥")
    else:
        print(f"Hello {oddelek}")

def postevanka():
    stevilo = int(input("Vnesi število: "))

    for i in range(1,11):
        print(f"{stevilo} x {i} = {stevilo * i}")


if __name__ == "__main__":
    #hello()
    postevanka()