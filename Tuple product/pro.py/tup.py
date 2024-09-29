import tup

def number(tuple):
    result = tup.prod([item for item in tuple])
    return result

tuple1 = (4,3,2,2,-1,19)
tuple2 = (2,4,8,8,3,2,9)

print(number(tuple1))
print(number(tuple2))