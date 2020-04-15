def reverseArray(a):
    arr_str = str(a[-1])
   
    for i in range(len(a) - 2, -1, -1):
        arr_str = arr_str + ' ' + str(a[i])
    return arr_str

print(reverseArray([1, 2, 4, 3]))