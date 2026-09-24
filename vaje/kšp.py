def igra(igra):
    while True:
        a = input("Igralec A (K/Š/P): ").upper()
        b = input("Igralec B (K/Š/P): ").upper()

        if a == "" or b == "":
            break

        if a != "K" and a != "Š" and a != "P":
            print("Napačen vnos!")
            continue

        if b != "K" and b != "Š" and b != "P":
            print("Napačen vnos!")
            continue

        igra.append(a)
        igra.append(b)

    return igra


def rezultati(igra):
    A = 0
    B = 0
    izenaceno = 0

    for i in range(0, len(igra), 2):
        a = igra[i]
        b = igra[i + 1]

        if a == b:
            izenaceno = izenaceno + 1

        elif (a == "K" and b == "Š") or \
             (a == "Š" and b == "P") or \
             (a == "P" and b == "K"):
            A = A + 1

        else:
            B = B + 1

    return A, B, izenaceno


def main():
    igraDB = []

    igra(igraDB)

    A, B, izenaceno = rezultati(igraDB)

    print("Rezultati:")
    print("Igralec A:", A)
    print("Igralec B:", B)
    print("Izenaceno:", izenaceno)


if __name__ == "__main__":
    main()