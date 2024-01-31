def gugurt_chopler(son):
    choplar = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  
    gugurt_chopi = 0
    
    while son > 0:
        qoldiq = son % 10
        gugurt_chopi += choplar[qoldiq]
        son //= 10

    return gugurt_chopi

