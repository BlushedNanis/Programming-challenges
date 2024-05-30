a, b = 0, 1
print(a)
print(b)
for i in range(48):
    c = a + b
    a = b
    b = c
    print(i, c)