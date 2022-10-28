# a = 20_000_000 # int
# b = 5.999999 # float
# c = True # bool
# d = "545" # str

# print(a, int(b), int(c), int(d))
# print(type(str()))

# list 
_list = [1, 2.2, True, True, "some text"]
print(_list)

# tuple
_tuple = (10, False, 20.7)
print(_tuple[2])

# set
_set = {10, 30.6, "text", 5, 10}
print(_set)

# dict
_dict = {
    10: "text",
    20: "world"
}
_dict.setdefault(30, True)
print(_dict)

print(len(_dict))