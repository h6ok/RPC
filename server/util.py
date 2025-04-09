def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x
    
def try_float(x):
    try:
        return float(x)
    except ValueError:
        return x

def confirmAllType(arr, typeArg):
    for v in arr:
        if type(v) != typeArg:
            return False
        
    return True