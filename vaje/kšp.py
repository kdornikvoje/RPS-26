def igra(igra:list):
    while  True:
        vnosa = input("Vnesi a igralca (K/Š/P): ").upper()
        vnosb = input("Vnesi b igralca (K/Š/P): ").upper()
        if vnosa == "" or vnosb =="":
            break
        else:
            igra.append(vnosa)
            igra.append(vnosb)
        
def Rezultati(igra:list):
    zmagala = 0
    zmagalb = 0
    izenaceno = 0
    IgralecAlast = ""
    igralecBlast = ""
    for index  in range(len(igra)):
        

if __name__ =="__main__":
    igraDB = []
    igra(igraDB)