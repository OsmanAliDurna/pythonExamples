uni = "Istanbul Universitesi"

stringLenght = len(uni)
first10Uni = uni [:10]
last10Uni = uni [-10:]
reverseUni = uni[::-1]

print("Length of uni\t\t: " , stringLenght)
print("First 10 of uni\t\t: ", first10Uni)
print("Last 10 of uni\t\t: ", last10Uni)
print("Reverse of uni\t\t: ", reverseUni)

swapNinUni = uni.replace("n","?")

print("Original uni\t\t: ", uni)
print("Swap n with ? in uni\t: ", swapNinUni)

numberA = "987654"
numberB = 6*numberA     # string olduğu için "987654""987654""987654""987654""987654""987654"
numberC = 6*numberA[0]  # C 6 tane A nın ilk indexinden oluşmaktadır. 999999

print("\n\n")
print("987654987654987654987654987654987654 nın 0-6-12-18-24-32. indexindeki rakamlar\t: ", numberB[::6])     # B nin 0. index ten başlayıp her 6. rakamını almaktadır.
print("987654 ün 0. indexindeki rakamın 6 adet yanyana yazılmış hali\t\t\t: ", numberC)          