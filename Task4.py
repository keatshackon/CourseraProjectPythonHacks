#Type Hinting

def f(param_1:set,
    param_2:set,
    param_3:set) -> set:
    a = param_1 - param_2
    b = param_2 & param_3
    c = param_1 | b
    return c

a:set = {1,2,4}
b:set = {4,12,3}
c:set = {11,21,41}
r:set = f(a,b,c)
print(r)
