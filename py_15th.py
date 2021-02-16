text = " Beni öldürmeyen şey beni güçlendirir. "

print(text + "Anonim...")
print(text.rstrip() + "Anonim...")
print(text.lstrip() + "Anonim...")
print(text.strip() + "Anonim...")

print(text.strip(". Br"))       # .strip fonksiyonu baştan ve sondan karakterleri siler. 
print(text.strip().swapcase())  # Eğer yandaki gibi içeriği belirtilmemişse üstteki gibi sadece baştaki ve sondaki boşlukları siler.

print(text.count("i"), "adet i harfi bulunmaktadır. Tüm textte")

print(text.count("i",20,len(text)), "adet i harfi bulunmaktadır. 20den sonra")

print(text.endswith("irir."))
print(text.startswith("Beni"))

print(text.endswith(" ") and text.startswith(" "))   # Boşlukla hem başlayıp hem bittiği için T & T = T döner.

print(text.find("öl"))              # Find metodu string i bulursan indexini ver bulamazsan -1 ver şeklinde çalışır.
print(text.find("ölüm",1,2))
print(text.index("öl"))             # Benzer iş yapmasına rağmen index metodu stringin indexini verir string yoksa hata verir.
print(text.index("ölüm"))