# a = (10, 4, 5.5, (10.5, True), "some")
# b = {
#     10: True,
#     True: 6.6,
#     ("some", False): 10
# }
# for i, j in b.items():
#     # if isinstance(i, str):
#     print(i)

# i, j, k = 10, 5, 6

def summ(*args):
    result = ""
    for element in args:
        result += str(element)
    return result


print(summ("some", True, "hello"))
print(summ(30, "text", False))

d = [
    [1, 3, 30, 10, 20, 11111111111], 
    [2, 4, 4]
]
i = 0
for _ in d:
    j = 0
    for __ in _:
        print(d[i][j])
        j += 1
    i += 1

# print(d)