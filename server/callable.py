import util

# floor method
def floor():
    def func(params):
        if len(params) > 1:
            raise ValueError('params has more than 2 params. if you invoke floor(x: int), you need 1 param of int')
        
        if not util.confirmAllType([util.try_float(x) for x in params], float):
            raise TypeError('param type does not match needed')
        
        return int(float(params[0]))
    return func

# root method
def nroot():
    def func(params):
        if len(params) > 2:
            raise ValueError('params has more than 3 params. if you invoke nroot(x: int, y: int), you need 2 param of int')
        
        if not util.confirmAllType([util.try_int(x) for x in params], int):
            raise TypeError('param type does not match needed')
        
        return pow(int(params[1]), 1 / int(params[0]))
    return func

# reverse method
def reverse():
    def func(params):
        if len(params) > 1:
            raise ValueError('params has more than 2 params. if you invoke reverse(s: str), you need 1 param of str')
        
        if not util.confirmAllType(params, str):
            raise TypeError('param type does not match needed')
        
        return params[0][::-1]
    return func

# validAnagram method
def validAnagram():
    def func(params):
        if len(params) > 2:
            raise ValueError('params has more than 3 params. if you invoke validAnagram(s1: str, s2: str), you need 2 param of str')
        
        if not util.confirmAllType(params, str):
            raise TypeError('param type does not match needed')
        
        if len(params[0]) is not len(params[1]):
            return False

        tempArr = []
        for s in params[0]:
            for i in range(len(params[1])):
                if (s == params[1][i] and i not in tempArr):
                    tempArr.append(i)
                    break
        return len(params[0]) == len(tempArr)
    return func


# sort method
def sort():
    def func(params):
        if type(params) != list:
            raise TypeError('param type does not match needed')
        
        if not util.confirmAllType(params, str):
            raise TypeError('param type does not match needed')
            
        return merge_sort(params)
    return func

def merge_sort(arr):
    if len(arr) == 1:
        return arr[0]
    
    left = merge_sort(arr[0: len(arr)//2])
    right = merge_sort(arr[len(arr)//2: len(arr)])

    lindex = 0
    rindex = 0
    result = []
    while lindex < len(left) and rindex < len(right):
        if left[lindex] < right[rindex]:
            result.append(left[lindex])
            lindex += 1

        else:
            result.append(right[rindex])
            rindex += 1

    if lindex < len(left):
        for ls in left[lindex: len(left)]:
            result.append(ls)

    if rindex < len(right):
        for rs in right[rindex: len(right)]:
            result.append(rs)
    
    return result


callable_map = {
    'floor': floor(),
    'nroot': nroot(),
    'reverse': reverse(),
    'validAnagram': validAnagram(),
    'sort': sort()
}