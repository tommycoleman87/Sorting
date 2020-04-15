# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    b_pointer = 0
    a_pointer = 0
    merged_arr_pointer = 0
    while merged_arr_pointer < len(merged_arr):
        if a_pointer <  len(arrA) and b_pointer >= len(arrB):
            while a_pointer < len(arrA):
                merged_arr[merged_arr_pointer] = arrA[a_pointer]
                a_pointer += 1
                merged_arr_pointer += 1
        elif a_pointer >= len(arrA) and b_pointer < len(arrB):
            while b_pointer < len(arrB):
                merged_arr[merged_arr_pointer] = arrB[b_pointer]
                b_pointer += 1
                merged_arr_pointer += 1
        elif arrA[a_pointer] < arrB[b_pointer]:
            merged_arr[merged_arr_pointer] = arrA[a_pointer]
            a_pointer += 1
            merged_arr_pointer += 1
        elif arrB[b_pointer] < arrA[a_pointer]:
            merged_arr[merged_arr_pointer] = arrB[b_pointer]
            b_pointer += 1
            merged_arr_pointer += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    while len(arr) > 1:
        mid_point = len(arr) // 2
        left_half = merge_sort(arr[0:mid_point])
        right_half = merge_sort(arr[mid_point:])
        arr = merge(left_half, right_half)
        return arr

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
