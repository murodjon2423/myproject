def orta_geometrik_arifmetik_tekshir(son1, son2):
    og = (son1 * son2) ** 0.5
    oa = (son1 + son2) / 2
    if og > oa:
        print(">")
    elif og < oa:
        print("<")
    else:
        print("=")


son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
orta_geometrik_arifmetik_tekshir(son1, son2)
