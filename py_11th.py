kurs = "Neler neler var."

deneme = len(kurs)

print(deneme)

deneme2 = kurs[0:8]

print(deneme2)

deneme3 = kurs[-4:-1]
deneme33 = kurs[-4:0]

print(deneme3)

print("2.deneme" + deneme33)

deneme4 = kurs[deneme-4:deneme]

print(deneme4)

# deneme 3 ve deneme 4 ün farkı:
# deneme 3 deki [-4:-1] => -4=12 ve -1=15 tir. deneme 33 deki gibi [-4:0] yazmak ise boş cevap dönemktedir.
# deneme 4 deki [deneme-4:deneme] => deneme-4 = 12 ancak deneme=16 dır.