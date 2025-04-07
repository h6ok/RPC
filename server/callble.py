def floor(x: float):
    return 10 * x / 10

def nroot(x: int, y: int):
    return pow(y, 1/x)

def reverse(s: str):
    return s[::-1]

def validAnagram(s1: str, s2: str):

    for s in range(s1):
        if s not in s2:
            return False
    
    return True

def sort(strArr: list[str]):
    return merge_sort(strArr)

def merge_sort(arr):
    if len(arr) == 1:
        return arr[0]
    
    left = merge_sort(arr[0: len(arr)/2])
    right = merge_sort(arr[len(arr)/2+1: len(arr)])

    lindex = 0
    rindex = 0
    result = []
    while lindex < len(left) and rindex < len(right):
        if left[lindex] < right[rindex]:
            result.push(left[lindex])
            lindex += 1

        else:
            result.push(right[rindex])
            rindex += 1

    if lindex < len(left):
        for ls in range(left[lindex: len(left)]):
            result.push(ls)

    if rindex < len(right):
        for rs in range(right[rindex: len(right)]):
            result.push(rs)
    
    return result