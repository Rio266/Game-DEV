tupple_1 = ("a", "c", 9)
print(tupple_1)

tupple_2 = "b", "d", 8
print(tupple_2)

tupple_3 = ("c", "e", [1, 2], (3, 4))
print(tupple_3[3][0])
print(tupple_3[2][0])
# tupple_3[3][0] = 9
# print(tupple_3)
tupple_3[2][1] = 6
print(tupple_3)

tupple_4 = ("a", "b", "c", 0, "d", 99, "e", 36, "f")
print(tupple_4[1:4])
print(tupple_4[-4:])
print(tupple_4[:])
print(tupple_4[::-1])
