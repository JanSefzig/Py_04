cisla = [100, 2, 300, 10, 11, 3000]
nejvetsi_cislo = cisla[0]
for a in cisla:
    if a > nejvetsi_cislo:
        nejvetsi_cislo = a
print(nejvetsi_cislo)

num = [1, 5, 0, 8, 6]
total = 0
for x in num:
    total += x

print(total)


def multiplyList(list):
    result = 1
    for x in list:
        result = result * x
    return result
list = [-1, 5, 20, 17]
print(multiplyList(list))


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = "honza"
  
print("origo : ", end="")
print(s)
  
print("reverse : ", end="")
print(reverse(s))