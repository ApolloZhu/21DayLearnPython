def add(num):
    return 3+num
def sub(num):
    return 3-num
def mul(num):
    return 3*num

if __name__ == "__main__":
    import random
    child = {}
    child['a'] = add
    child['s'] = sub
    child['m'] = mul
    lib = "asm"
    print(child[random.choice(lib)](5))
