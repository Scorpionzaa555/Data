"""Lab1.3"""
def minmax(data):
    """"Lab1.3"""
    mn = data[0]
    mx = data[0]
    for i in data:
        if i <= mn:
            mn = i
        if i >= mx:
            mx = i
    return mn,mx
print(minmax([22,54,7,87,12,9,63,55,48]))
