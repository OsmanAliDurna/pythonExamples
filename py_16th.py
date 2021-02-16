deneme = "denemelik text"

print(deneme.isalpha())
print(deneme.isdigit())
print(deneme.replace(" ","").isalpha())

print(deneme.center(30,"-"))
print(deneme.rjust(30,"-"))
print(deneme.ljust(30,"-"))

print(deneme.split())
print(deneme.split()[0])
print(deneme.split()[1])
print(deneme.split()[-1])
print(deneme.split()[-2])
print(deneme.split()[2])