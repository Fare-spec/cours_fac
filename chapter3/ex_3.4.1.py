# 1
i = 0
while i != 10:
    print(i)
    i += 1

# 2
i = 10
while i != 0:
    print(i)
    i -= 1
# 3
i = 0
while i != 20:
    print(i)
    i += 2
# 4
i = 0
while i < 30:
    print(i)
    i = +3
# 5
i = 1
while i <= 300:
    print(i)
    i *= 3
# 6
i = int(input("entier: "))
while i > 0:
    print(i)
    i = int(input("entier: "))
# 7
i = input("lettre: ")
while i in "aeiouy":
    print(i)
    i = input("lettre: ")
# 8

i = input("lettre: ")
while i not in "aeiouy":
    print(i)
    i = input("lettre: ")
# 9
i = float("note: ")
while 0 < i < 20:
    print(i)
    i = int(input("note: "))
# 10
i = 1
while i < 10:
    print(i**2)
    i += 1
