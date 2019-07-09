def selamla(isim ="isimsiz"):
    print("merhaba", isim)

def topla(*vals):
    topla = 0
    for val in vals:
        topla = topla + val

    return topla

ciftMi = lambda say : ((say % 2) == 0)
