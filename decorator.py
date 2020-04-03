def dec(f):
    print('test decrator function')

    return f
@dec
def test(a):
    print('tst')

lst = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4,4]
print (set(lst))
print(max(lst, key=lst.count))