def hello():
    oddelek = input("Vnesi oddelek: ")
    if oddelek.upper() == "1.RI":       
        print(f"Hello {oddelek} ♥")
    else:
        print(f"Hello {oddelek}")

if __name__ == "__main__":
    hello()