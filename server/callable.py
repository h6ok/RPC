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
        
        for s in range(params[0]):
            if s not in params[1]:
                return False
        return True
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


callable_map = {
    'floor': floor(),
    'nroot': nroot(),
    'reverse': reverse(),
    'validAnagram': validAnagram(),
    'sort': sort()
}