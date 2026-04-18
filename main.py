def soz_uzunligi(matnlar):
    uzunliklar = []
    for matn in matnlar:
        sozlar = matn.split()
        soz_uzunliklari = [len(soz) for soz in sozlar]
        uzunliklar.append(soz_uzunliklari)
    return uzunliklar

matnlar = ["Men yaxshi dasturchiman", "Python dasturlash tili juda qulay"]
print(soz_uzunligi(matnlar))
